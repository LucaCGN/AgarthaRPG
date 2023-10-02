```python

# pip install langchain --upgrade
# Version: 0.0.164

# !pip install pypdf

```

```python

# PDF Loaders. If unstructured gives you a hard time, try PyPDFLoader
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

```

### Load your data

```python

loader = PyPDFLoader("../data/field-guide-to-data-science.pdf")

## Other options for loaders 
# loader = UnstructuredPDFLoader("../data/field-guide-to-data-science.pdf")
# loader = OnlinePDFLoader("https://wolfpaulus.com/wp-content/uploads/2017/05/field-guide-to-data-science.pdf")

```

```python

data = loader.load()

```

```python

# Note: If you're using PyPDFLoader then it will split by page for you already
print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[30].page_content)} characters in your document')

```

```

You have 126 document(s) in your data
There are 2812 characters in your document

```

### Chunk your data up into smaller documents

```python

# Note: If you're using PyPDFLoader then we'll be splitting for the 2nd time.
# This is optional, test out on your own data.

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

```

```python

print (f'Now you have {len(texts)} documents')

```

```

Now you have 162 documents

```

### Create embeddings of your documents to get ready for semantic search

```python

from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

```

```

/Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages/pinecone/index.py:4: TqdmExperimentalWarning: Using `tqdm.autonotebook.tqdm` in notebook mode. Use `tqdm.tqdm` instead to force console mode (e.g. in jupyter console)
  from tqdm.autonotebook import tqdm

```

```python

# Check to see if there is an environment variable with you API keys, if not, use what you put below
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'YourAPIKey')

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', 'YourAPIKey')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-east1-gcp') # You may need to switch with your env

```

```python

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

```

```python

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)
index_name = "langchaintest" # put in the name of your pinecone index here

```

```python

docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

```

```python

query = "What are examples of good data science teams?"
docs = docsearch.similarity_search(query)

```

```python

# Here's an example of the first document that was returned
print(docs[0].page_content[:450])

```

```

Intelligence and cloud infrastructure development  
work. We saw the need for a  
new approach to distill value 
from our clients’ data. We 
approached the problem 
with a multidisciplinary 
team of computer scientists, 
mathematicians and domain 
experts. They immediately 
produced new insights and 
analysis paths, solidifying the 
validity of the approach. Since 
that time, our Data Science  
team has grown to 250 staff 
supporting dozens of cl

```

### Query those docs to get your answer back

```python

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

```

```python

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

```

```python

query = "What is the collect stage of data maturity?"
docs = docsearch.similarity_search(query)

```

```python

chain.run(input_documents=docs, question=query)

```