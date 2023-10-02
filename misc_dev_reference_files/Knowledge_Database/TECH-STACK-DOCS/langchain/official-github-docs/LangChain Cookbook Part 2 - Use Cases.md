# LangChain Cookbook Part 2: Use Cases👨‍🍳👩‍🍳

*This cookbook is based on the [LangChain Conceptual Documentation](https://docs.langchain.com/docs/)*

**Goals:**

1. Inspire you to build
2. Provide an introductory understanding of the main use cases of LangChain via [ELI5](https://www.dictionary.com/e/slang/eli5/#:~:text=ELI5%20is%20short%20for%20%E2%80%9CExplain,a%20complicated%20question%20or%20problem.) examples and code snippets. For an introduction to the *fundamentals* of LangChain check out [Cookbook Part 1: Fundamentals](https://github.com/gkamradt/langchain-tutorials/blob/main/LangChain%20Cookbook%20Part%201%20-%20Fundamentals.ipynb).

**LangChain Links:**
* [LC Conceptual Documentation](https://docs.langchain.com/docs/)
* [LC Python Documentation](https://python.langchain.com/en/latest/)
* [LC Javascript/Typescript Documentation](https://js.langchain.com/docs/)
* [LC Discord](https://discord.gg/6adMQxSpJS)
* [www.langchain.com](https://langchain.com/)
* [LC Twitter](https://twitter.com/LangChainAI)


### **What is LangChain?**
> LangChain is a framework for developing applications powered by language models.
*[Source](https://blog.langchain.dev/announcing-our-10m-seed-round-led-by-benchmark/#:~:text=LangChain%20is%20a%20framework%20for%20developing%20applications%20powered%20by%20language%20models)*

**TLDR**: LangChain makes the complicated parts of working & building with AI models easier. It helps do this in two ways:

1. **Integration** - Bring external data, such as your files, other applications, and api data, to your LLMs
2. **Agency** - Allow your LLMs to interact with its environment via decision making. Use LLMs to help decide which action to take next

### **Why LangChain?**
1. **Components** - LangChain makes it easy to swap out abstractions and components necessary to work with language models.

2. **Customized Chains** - LangChain provides out of the box support for using and customizing 'chains' - a series of actions strung together.

3. **Speed 🚢** - This team ships insanely fast. You'll be up to date with the latest LLM features.

4. **Community 👥** - Wonderful [discord](https://discord.gg/6adMQxSpJS) and community support, meet ups, hackathons, etc.

Though LLMs can be straightforward (text-in, text-out) you'll quickly run into friction points that LangChain helps with once you develop more complicated applications.

### **Main Use Cases**

* **Summarization** - Express the most important facts about a body of text or chat interaction
* **Question and Answering Over Documents** - Use information held within documents to answer questions or query
* **Extraction** - Pull structured data from a body of text or an user query
* **Evaluation** - Understand the quality of output from your application
* **Querying Tabular Data** - Pull data from databases or other tabular source
* **Code Understanding** - Reason about and digest code
* **Interacting with APIs** - Query APIs and interact with the outside world
* **Chatbots** - A framework to have a back and forth interaction with a user combined with memory in a chat interface
* **Agents** - Use LLMs to make decisions about what to do next. Enable these decisions with tools.

Want to see live examples of these use cases? Head over to the [LangChain Project Gallery](https://github.com/gkamradt/langchain-tutorials)

#### **Authors Note:**

* This cookbook will not cover all aspects of LangChain. It's contents have been curated to get you to building & impact as quick as possible. For more, please check out [LangChain Technical Documentation](https://python.langchain.com/en/latest/index.html)
* This notebook assumes is that you've seen part 1 of this series [Fundamentals](https://github.com/gkamradt/langchain-tutorials/blob/main/LangChain%20Cookbook%20Part%201%20-%20Fundamentals.ipynb). This notebook is focused on what to do and how to apply those fundamentals.
* You'll notice I repeat import statements throughout the notebook. My intention is to lean on the side of clarity and help you see the full code block in one spot. No need to go back and forth to see when we imported a package.
* We use the default models throughout the notebook, at the time of writing they were davinci-003 and gpt-3.5-turbo. You would no doubt get better results with GPT4

Let's get started

Throughout this tutorial we will use OpenAI's various [models](https://platform.openai.com/docs/models/overview). LangChain makes it easy to [subsistute LLMs](https://langchain.com/integrations.html#:~:text=integrations%20LangChain%20provides.-,LLMs,-LLM%20Provider) so you can BYO-LLM if you want

```python

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY', 'YourAPIKeyIfNotSet')

```

```python

# Run this cell if you want to make your display wider
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

```

```

<IPython.core.display.HTML object>

```

# LangChain Use Cases

## Summarization

One of the most common use cases for LangChain and LLMs is summarization. You can summarize any piece of text, but use cases span from summarizing calls, articles, books, academic papers, legal documents, user history, a table, or financial documents. It's super helpful to have a tool which can summarize information quickly.

* **Deep Dive** - (Coming Soon)
* **Examples** - [Summarizing B2B Sales Calls](https://www.youtube.com/watch?v=DIw4rbpI9ic)
* **Use Cases** - Summarize Articles, Transcripts, Chat History, Slack/Discord, Customer Interactions, Medical Papers, Legal Documents, Podcasts, Tweet Threads, Code Bases, Product Reviews, Financial Documents

### Summaries Of Short Text

For summaries of short texts, the method is straightforward, in fact you don't need to do anything fancy other than simple prompting with instructions

```python

from langchain.llms import OpenAI
from langchain import PromptTemplate

# Note, the default model is already 'text-davinci-003' but I call it out here explicitly so you know where to change it later if you want
llm = OpenAI(temperature=0, model_name='text-davinci-003', openai_api_key=openai_api_key)

# Create our template
template = """
%INSTRUCTIONS:
Please summarize the following piece of text.
Respond in a manner that a 5 year old would understand.

%TEXT:
{text}
"""

# Create a LangChain prompt template that we can insert values to later
prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

```

Let's let's find a confusing text online. *[Source](https://www.smithsonianmag.com/smart-news/long-before-trees-overtook-the-land-earth-was-covered-by-giant-mushrooms-13709647/)*

```python

confusing_text = """
For the next 130 years, debate raged.
Some scientists called Prototaxites a lichen, others a fungus, and still others clung to the notion that it was some kind of tree.
“The problem is that when you look up close at the anatomy, it’s evocative of a lot of different things, but it’s diagnostic of nothing,” says Boyce, an associate professor in geophysical sciences and the Committee on Evolutionary Biology.
“And it’s so damn big that when whenever someone says it’s something, everyone else’s hackles get up: ‘How could you have a lichen 20 feet tall?’”
"""

```

Let's take a look at what prompt will be sent to the LLM

```python

print ("------- Prompt Begin -------")

final_prompt = prompt.format(text=confusing_text)
print(final_prompt)

print ("------- Prompt End -------")

```

```

------- Prompt Begin -------

%INSTRUCTIONS:
Please summarize the following piece of text.
Respond in a manner that a 5 year old would understand.

%TEXT:

For the next 130 years, debate raged.
Some scientists called Prototaxites a lichen, others a fungus, and still others clung to the notion that it was some kind of tree.
“The problem is that when you look up close at the anatomy, it’s evocative of a lot of different things, but it’s diagnostic of nothing,” says Boyce, an associate professor in geophysical sciences and the Committee on Evolutionary Biology.
“And it’s so damn big that when whenever someone says it’s something, everyone else’s hackles get up: ‘How could you have a lichen 20 feet tall?’”


------- Prompt End -------

```

Finally let's pass it through the LLM

```python

output = llm(final_prompt)
print (output)

```

```

For 130 years, people argued about what Prototaxites was. Some thought it was a lichen, some thought it was a fungus, and some thought it was a tree. But no one could agree. It was so big that it was hard to figure out what it was.

```

This method works fine, but for longer text, it can become a pain to manage and you'll run into token limits. Luckily LangChain has out of the box support for different methods to summarize via their [load_summarize_chain](https://python.langchain.com/en/latest/use_cases/summarization.html).

### Summaries Of Longer Text

*Note: This method will also work for short text too*

```python

from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

Let's load up a longer document

```python

with open('data/PaulGrahamEssays/good.txt', 'r') as file:
    text = file.read()

# Printing the first 285 characters as a preview
print (text[:285])

```

```

April 2008(This essay is derived from a talk at the 2008 Startup School.)About a month after we started Y Combinator we came up with the
phrase that became our motto: Make something people want.  We've
learned a lot since then, but if I were choosing now that's still
the one I'd pick.

```

Then let's check how many tokens are in this document. [get_num_tokens](https://python.langchain.com/en/latest/reference/modules/llms.html#langchain.llms.OpenAI.get_num_tokens) is a nice method for this.

```python

num_tokens = llm.get_num_tokens(text)

print (f"There are {num_tokens} tokens in your file")

```

```

There are 3970 tokens in your file

```

While you could likely stuff this text in your prompt, let's act like it's too big and needs another method.

First we'll need to split it up. This process is called 'chunking' or 'splitting' your text into smaller pieces. I like the [RecursiveCharacterTextSplitter](https://python.langchain.com/en/latest/modules/indexes/text_splitters/examples/recursive_text_splitter.html) because it's easy to control but there are a [bunch](https://python.langchain.com/en/latest/modules/indexes/text_splitters.html) you can try

```python

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=5000, chunk_overlap=350)
docs = text_splitter.create_documents([text])

print (f"You now have {len(docs)} docs intead of 1 piece of text")

```

```

You now have 4 docs intead of 1 piece of text

```

Next we need to load up a chain which will make successive calls to the LLM for us. Want to see the prompt being used in the chain below? Check out the [LangChain documentation](https://github.com/hwchase17/langchain/blob/master/langchain/chains/summarize/map_reduce_prompt.py)

For information on the difference between chain types, check out this video on [token limit workarounds](https://youtu.be/f9_BWhCI4Zo)

*Note: You could also get fancy and make the first 4 calls of the map_reduce run in parallel too*

```python

# Get your chain ready to use
chain = load_summarize_chain(llm=llm, chain_type='map_reduce') # verbose=True optional to see what is getting sent to the LLM

```

```python

# Use it. This will run through the 4 documents, summarize the chunks, then get a summary of the summary.
output = chain.run(docs)
print (output)

```

```

This essay looks at the idea of benevolence in startups, and how it can help them succeed. It explains how benevolence can improve morale, make people want to help, and help startups be decisive. It also looks at how markets have evolved to value potential dividends and potential earnings, and how users dislike their new operating system. The author argues that starting a company with benevolent aims is currently undervalued, and that Y Combinator's motto of "Make something people want" is a powerful concept.

```

## Question & Answering Using Documents As Context

*[LangChain Question & Answer Docs](https://python.langchain.com/en/latest/use_cases/question_answering.html)*

In order to use LLMs for question and answer we must:

1. Pass the LLM relevant context it needs to answer a question
2. Pass it our question that we want answered

Simplified, this process looks like this "llm(your context + your question) = your answer"

* **Deep Dive** - [Question A Book](https://youtu.be/h0DHDp1FbmQ), [Ask Questions To Your Custom Files](https://youtu.be/EnT-ZTrcPrg), [Chat Your Data JS (1000 pages of Financial Reports)](https://www.youtube.com/watch?v=Ix9WIZpArm0&t=1051s), [LangChain Q&A webinar](https://www.crowdcast.io/c/rh66hcwivly0)
* **Examples** - [ChatPDF](https://www.chatpdf.com/)
* **Use Cases** - Chat your documents, ask questions to academic papers, create study guides, reference medical information

### Simple Q&A Example

Here let's review the convention of `llm(your context + your question) = your answer`

```python

from langchain.llms import OpenAI

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

```python

context = """
Rachel is 30 years old
Bob is 45 years old
Kevin is 65 years old
"""

question = "Who is under 40 years old?"

```

Then combine them.

```python

output = llm(context + question)

# I strip the text to remove the leading and trailing whitespace
print (output.strip())

```

```

Rachel is under 40 years old.

```

As we ramp up our sophistication, we'll take advantage of this convention more.

The hard part comes in when you need to be selective about *which* data you put in your context. This field of study is called "[document retrieval](https://python.langchain.com/en/latest/modules/indexes/retrievers.html)" and tightly coupled with AI Memory.

### Using Embeddings

I informally call what were about to go through as "The VectorStore Dance". It's the process of splitting your text, embedding the chunks, putting the embeddings in a DB, and then querying them. For a full video on this check out [How To Question A Book](https://www.youtube.com/watch?v=h0DHDp1FbmQ)

The goal is to select relevant chunks of our long text, but which chunks do we pull? The most popular method is to pull *similar* texts based off comparing vector embeddings.

```python

from langchain import OpenAI

# The vectorstore we'll be using
from langchain.vectorstores import FAISS

# The LangChain component we'll use to get the documents
from langchain.chains import RetrievalQA

# The easy document loader for text
from langchain.document_loaders import TextLoader

# The embedding engine that will convert our text to vectors
from langchain.embeddings.openai import OpenAIEmbeddings

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

Let's load up a longer document

```python

loader = TextLoader('data/PaulGrahamEssays/worked.txt')
doc = loader.load()
print (f"You have {len(doc)} document")
print (f"You have {len(doc[0].page_content)} characters in that document")

```

```

You have 1 document
You have 74663 characters in that document

```

Now let's split our long doc into smaller pieces

```python

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
docs = text_splitter.split_documents(doc)

```

```python

# Get the total number of characters so we can see the average later
num_total_characters = sum([len(x.page_content) for x in docs])

print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")

```

```

Now you have 29 documents that have an average of 2,930 characters (smaller pieces)

```

```python

# Get your embeddings engine ready
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Embed your documents and combine with the raw text in a pseudo db. Note: This will make an API call to OpenAI
docsearch = FAISS.from_documents(docs, embeddings)

```

Create your retrieval engine

```python

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

```

Now it's time to ask a question. The retriever will go get the similar documents and combine with your question for the LLM to reason through.

Note: It may not seem like much, but the magic here is that we didn't have to pass in our full original document.

```python

query = "What does the author describe as good work?"
qa.run(query)

```

If you wanted to do more you would hook this up to a cloud vector database, use a tool like metal and start managing your documents, with external data sources

## Extraction
*[LangChain Extraction Docs](https://python.langchain.com/en/latest/use_cases/extraction.html)*

Extraction is the process of parsing data from a piece of text. This is commonly used with output parsing in order to *structure* our data.

* **Deep Dive** - [Use LLMs to Extract Data From Text (Expert Level Text Extraction](https://youtu.be/xZzvwR9jdPA), [Structured Output From OpenAI (Clean Dirty Data)](https://youtu.be/KwAXfey-xQk)
* **Examples** - [OpeningAttributes](https://twitter.com/GregKamradt/status/1646500373837008897)
* **Use Cases:** Extract a structured row from a sentence to insert into a database, extract multiple rows from a long document to insert into a database, extracting parameters from a user query to make an API call

A popular library for extraction is [Kor](https://eyurtsev.github.io/kor/). We won't cover it today but I highly suggest checking it out for advanced extraction.

```python

# To help construct our Chat Messages
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

# We will be using a chat model, defaults to gpt-3.5-turbo
from langchain.chat_models import ChatOpenAI

# To parse outputs and get structured data back
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

chat_model = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

```

### Vanilla Extraction

Let's start off with an easy example. Here I simply supply a prompt with instructions with the type of output I want.

```python

instructions = """
You will be given a sentence with fruit names, extract those fruit names and assign an emoji to them
Return the fruit name and emojis in a python dictionary
"""

fruit_names = """
Apple, Pear, this is an kiwi
"""

```

```python

# Make your prompt which combines the instructions w/ the fruit names
prompt = (instructions + fruit_names)

# Call the LLM
output = chat_model([HumanMessage(content=prompt)])

print (output.content)
print (type(output.content))

```

```

{'Apple': '🍎', 'Pear': '🍐', 'kiwi': '🥝'}
<class 'str'>

```

Let's turn this into a proper python dictionary

```python

output_dict = eval(output.content)

print (output_dict)
print (type(output_dict))

```

```

{'Apple': '🍎', 'Pear': '🍐', 'kiwi': '🥝'}
<class 'dict'>

```

While this worked this time, it's not a long term reliable method for more advanced use cases

### Using LangChain's Response Schema

LangChain's response schema will does two things for us: 

1. Autogenerate the a prompt with bonafide format instructions. This is great because I don't need to worry about the prompt engineering side, I'll leave that up to LangChain!

2. Read the output from the LLM and turn it into a proper python object for me

Here I define the schema I want. I'm going to pull out the song and artist that a user wants to play from a pseudo chat message.

```python

# The schema I want out
response_schemas = [
    ResponseSchema(name="artist", description="The name of the musical artist"),
    ResponseSchema(name="song", description="The name of the song that the artist plays")
]

# The parser that will look for the LLM output in my schema and return it back to me
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

```

```python

# The format instructions that LangChain makes. Let's look at them
format_instructions = output_parser.get_format_instructions()
print(format_instructions)

```

```

The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json
{
	"artist": string  // The name of the musical artist
	"song": string  // The name of the song that the artist plays
}
```

```

```python

# The prompt template that brings it all together
# Note: This is a different prompt template than before because we are using a Chat Model

prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("Given a command from the user, extract the artist and song names \n \
                                                    {format_instructions}\n{user_prompt}")  
    ],
    input_variables=["user_prompt"],
    partial_variables={"format_instructions": format_instructions}
)

```

```python

fruit_query = prompt.format_prompt(user_prompt="I really like So Young by Portugal. The Man")
print (fruit_query.messages[0].content)

```

```

Given a command from the user, extract the artist and song names 
                                                     The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json
{
	"artist": string  // The name of the musical artist
	"song": string  // The name of the song that the artist plays
}
```
I really like So Young by Portugal. The Man

```

```python

fruit_output = chat_model(fruit_query.to_messages())
output = output_parser.parse(fruit_output.content)

print (output)
print (type(output))

```

```

{'artist': 'Portugal. The Man', 'song': 'So Young'}
<class 'dict'>

```

Awesome, now we have a dictionary that we can use later down the line

<span style="background:#fff5d6">Warning:</span> The parser looks for an output from the LLM in a specific format. Your model may not output the same format every time. Make sure to handle errors with this one. GPT4 and future iterations will be more reliable.

For more advanced parsing check out [Kor](https://eyurtsev.github.io/kor/)

## Evaluation

*[LangChain Evaluation Docs](https://python.langchain.com/en/latest/use_cases/evaluation.html)*

Evaluation is the process of doing quality checks on the output of your applications. Normal, deterministic, code has tests we can run, but judging the output of LLMs is more difficult because of the unpredictableness and variability of natural language. LangChain provides tools that aid us in this journey.

* **Deep Dive** - Coming Soon
* **Examples** - [Lance Martin's Advanced](https://twitter.com/RLanceMartin) [Auto-Evaluator](https://github.com/rlancemartin/auto-evaluator)
* **Use Cases:** Run quality checks on your summarization or Question & Answer pipelines, check the output of you summarization pipeline

```python

# Embeddings, store, and retrieval
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Model and doc loader
from langchain import OpenAI
from langchain.document_loaders import TextLoader

# Eval!
from langchain.evaluation.qa import QAEvalChain

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

```python

# Our long essay from before
loader = TextLoader('data/PaulGrahamEssays/worked.txt')
doc = loader.load()

print (f"You have {len(doc)} document")
print (f"You have {len(doc[0].page_content)} characters in that document")

```

```

You have 1 document
You have 74663 characters in that document

```

First let's do the Vectorestore dance so we can do question and answers

```python

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
docs = text_splitter.split_documents(doc)

# Get the total number of characters so we can see the average later
num_total_characters = sum([len(x.page_content) for x in docs])

print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")

```

```

Now you have 29 documents that have an average of 2,930 characters (smaller pieces)

```

```python

# Embeddings and docstore
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
docsearch = FAISS.from_documents(docs, embeddings)

```

Make your retrieval chain. Notice how I have an `input_key` parameter now. This tells the chain which key from a dictionary I supply has my prompt/query in it. I specify `question` to match the question in the dict below

```python

chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(), input_key="question")

```

Now I'll pass a list of questions and ground truth answers to the LLM that I know are correct (I validated them as a human).

```python

question_answers = [
    {'question' : "Which company sold the microcomputer kit that his friend built himself?", 'answer' : 'Healthkit'},
    {'question' : "What was the small city he talked about in the city that is the financial capital of USA?", 'answer' : 'Yorkville, NY'}
]

```

I'll use `chain.apply` to run both my questions one by one separately.

One of the cool parts is that I'll get my list of question and answers dictionaries back, but there'll be another key in the dictionary `result` which will be the output from the LLM.

Note: I specifically made my 2nd question ambigious and tough to answer in one pass so the LLM would get it incorrect

```python

predictions = chain.apply(question_answers)
predictions

```

We then have the LLM compare my ground truth answer (the `answer` key) with the result from the LLM (`result` key).

Or simply, we are asking the LLM to grade itself. What a wild world we live in.

```python

# Start your eval chain
eval_chain = QAEvalChain.from_llm(llm)

# Have it grade itself. The code below helps the eval_chain know where the different parts are
graded_outputs = eval_chain.evaluate(question_answers,
                                     predictions,
                                     question_key="question",
                                     prediction_key="result",
                                     answer_key='answer')

```

```python

graded_outputs

```

This is correct! Notice how the answer in question #1 was "Healthkit" and the prediction was "The microcomputer kit was sold by Heathkit." The LLM knew that the answer and result were the same and gave us a "correct" label. Awesome.

For #2 it knew they were not the same and gave us an "incorrect" label

## Querying Tabular Data

*[LangChain Querying Tabular Data Docs](https://python.langchain.com/en/latest/use_cases/tabular.html)*

The most common type of data in the world sits in tabular form (ok, ok, besides unstructured data). It is super powerful to be able to query this data with LangChain and pass it through to an LLM 

* **Deep Dive** - Coming Soon
* **Examples** - TBD
* **Use Cases:** Use LLMs to query data about users, do data analysis, get real time information from your DBs

For futher reading check out "Agents + Tabular Data" ([Pandas](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/pandas.html), [SQL](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/sql_database.html), [CSV](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html))

Let's query an SQLite DB with natural language. We'll look at the [San Francisco Trees](https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq) dataset.

```python

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

We'll start off by specifying where our data is and get the connection ready

```python

sqlite_db_path = 'data/San_Francisco_Trees.db'
db = SQLDatabase.from_uri(f"sqlite:///{sqlite_db_path}")

```

Then we'll create a chain that take our LLM, and DB. I'm setting `verbose=True` so you can see what is happening underneath the hood.

```python

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

```

```

/Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages/langchain/chains/sql_database/base.py:63: UserWarning: Directly instantiating an SQLDatabaseChain with an llm is deprecated. Please instantiate with llm_chain argument or using the from_llm class method.
  warnings.warn(

```

```python

db_chain.run("How many Species of trees are there in San Francisco?")

```

```

[1m> Entering new SQLDatabaseChain chain...[0m
How many Species of trees are there in San Francisco?
SQLQuery:[32;1m[1;3mSELECT COUNT(DISTINCT "qSpecies") FROM "SFTrees";[0m
SQLResult: [33;1m[1;3m[(578,)][0m
Answer:[32;1m[1;3mThere are 578 Species of trees in San Francisco.[0m
[1m> Finished chain.[0m

```

This is awesome! There are actually a few steps going on here.

**Steps:**
1. Find which table to use
2. Find which column to use
3. Construct the correct sql query
4. Execute that query
5. Get the result
6. Return a natural language reponse back

Let's confirm via pandas

```python

import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect(sqlite_db_path)

# Define your SQL query
query = "SELECT count(distinct qSpecies) FROM SFTrees"

# Read the SQL query into a Pandas DataFrame
df = pd.read_sql_query(query, connection)

# Close the connection
connection.close()

```

```python

# Display the result in the first column first cell
print(df.iloc[0,0])

```

```

578

```

Nice! The answers match.

## Code Understanding

*[LangChain Code Understanding Docs](https://python.langchain.com/en/latest/use_cases/code.html)*

One of the most exciting abilities of LLMs is code undestanding. People around the world are leveling up their output in both speed & quality due to AI help. A big part of this is having a LLM that can understand code and help you with a particular task.

* **Deep Dive** - Coming Soon
* **Examples** - TBD
* **Use Cases:** Co-Pilot-esque functionality that can help answer questions from a specific library, help you generate new code

```python

# Helper to read local files
import os

# Vector Support
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

# Model and chain
from langchain.chat_models import ChatOpenAI

# Text splitters
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api_key)

```

We will do the Vectorstore dance again

```python

embeddings = OpenAIEmbeddings(disallowed_special=(), openai_api_key=openai_api_key)

```

I put a small python package [The Fuzz](https://github.com/seatgeek/thefuzz) (personal indie favorite) in the data folder of this repo.

The loop below will go through each file in the library and load it up as a doc

```python

root_dir = 'data/thefuzz'
docs = []

# Go through each folder
for dirpath, dirnames, filenames in os.walk(root_dir):
    
    # Go through each file
    for file in filenames:
        try: 
            # Load up the file as a doc and split
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e: 
            pass

```

Let's look at an example of a document. It's just code!

```python

print (f"You have {len(docs)} documents\n")
print ("------ Start Document ------")
print (docs[0].page_content[:300])

```

```

You have 175 documents

------ Start Document ------
import unittest
import re
import pycodestyle

from thefuzz import fuzz
from thefuzz import process
from thefuzz import utils
from thefuzz.string_processing import StringProcessor


class StringProcessingTest(unittest.TestCase):
    def test_replace_non_letters_non_numbers_with_whitespace(self):

```

Embed and store them in a docstore. This will make an API call to OpenAI

```python

docsearch = FAISS.from_documents(docs, embeddings)

```

```python

# Get our retriever ready
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

```

```python

query = "What function do I use if I want to find the most similar item in a list of items?"
output = qa.run(query)

```

```python

print (output)

```

```

You can use the `process.extractOne()` function from `thefuzz` package to find the most similar item in a list of items. Here's an example:

```
from thefuzz import process

choices = ["apple", "banana", "orange", "pear"]
query = "pineapple"

best_match = process.extractOne(query, choices)
print(best_match)
```

This would output `(u'apple', 36)`, which means that the most similar item to "pineapple" in the list of choices is "apple", with a similarity score of 36.

```

```python

query = "Can you write the code to use the process.extractOne() function? Only respond with code. No other text or explanation"
output = qa.run(query)

```

```python

print (output)

```

```

import fuzzywuzzy.process as process

choices = [
    "new york mets vs chicago cubs",
    "chicago cubs at new york mets",
    "atlanta braves vs pittsbugh pirates",
    "new york yankees vs boston red sox"
]

query = "new york mets at chicago cubs"

best = process.extractOne(query, choices)
print(best[0])

```

[¡Shibby!](https://thumbs.gfycat.com/WateryBeneficialDeermouse-size_restricted.gif)

## Interacting with APIs

*[LangChain API Interaction Docs](https://python.langchain.com/en/latest/use_cases/apis.html)*

If the data or action you need is behind an API, you'll need your LLM to interact with APIs

* **Deep Dive** - Coming Soon
* **Examples** - TBD
* **Use Cases:** Understand a request from a user and carry out an action, be able to automate more real-world workflows

This topic is closely related to Agents and Plugins, though we'll look at a simple use case for this section. For more information, check out [LangChain + plugins](https://python.langchain.com/en/latest/use_cases/agents/custom_agent_with_plugin_retrieval_using_plugnplai.html) documentation.

```python

from langchain.chains import APIChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

LangChain's APIChain has the ability to read API documentation and understand which endpoint it needs to call.

In this case I wrote (purposefully sloppy) API documentation to demonstrate how this works

```python

api_docs = """

BASE URL: https://restcountries.com/

API Documentation:

The API endpoint /v3.1/name/{name} Used to find informatin about a country. All URL parameters are listed below:
    - name: Name of country - Ex: italy, france
    
The API endpoint /v3.1/currency/{currency} Uesd to find information about a region. All URL parameters are listed below:
    - currency: 3 letter currency. Example: USD, COP
    
Woo! This is my documentation
"""

chain_new = APIChain.from_llm_and_api_docs(llm, api_docs, verbose=True)

```

Let's try to make an API call that is meant for the country endpoint

```python

chain_new.run('Can you tell me information about france?')

```

```

[1m> Entering new APIChain chain...[0m
[32;1m[1;3m https://restcountries.com/v3.1/name/france[0m
[33;1m[1;3m[{"name":{"common":"France","official":"French Republic","nativeName":{"fra":{"official":"République française","common":"France"}}},"tld":[".fr"],"cca2":"FR","ccn3":"250","cca3":"FRA","cioc":"FRA","independent":true,"status":"officially-assigned","unMember":true,"currencies":{"EUR":{"name":"Euro","symbol":"€"}},"idd":{"root":"+3","suffixes":["3"]},"capital":["Paris"],"altSpellings":["FR","French Republic","République française"],"region":"Europe","subregion":"Western Europe","languages":{"fra":"French"},"translations":{"ara":{"official":"الجمهورية الفرنسية","common":"فرنسا"},"bre":{"official":"Republik Frañs","common":"Frañs"},"ces":{"official":"Francouzská republika","common":"Francie"},"cym":{"official":"French Republic","common":"France"},"deu":{"official":"Französische Republik","common":"Frankreich"},"est":{"official":"Prantsuse Vabariik","common":"Prantsusmaa"},"fin":{"official":"Ranskan tasavalta","common":"Ranska"},"fra":{"official":"République française","common":"France"},"hrv":{"official":"Francuska Republika","common":"Francuska"},"hun":{"official":"Francia Köztársaság","common":"Franciaország"},"ita":{"official":"Repubblica francese","common":"Francia"},"jpn":{"official":"フランス共和国","common":"フランス"},"kor":{"official":"프랑스 공화국","common":"프랑스"},"nld":{"official":"Franse Republiek","common":"Frankrijk"},"per":{"official":"جمهوری فرانسه","common":"فرانسه"},"pol":{"official":"Republika Francuska","common":"Francja"},"por":{"official":"República Francesa","common":"França"},"rus":{"official":"Французская Республика","common":"Франция"},"slk":{"official":"Francúzska republika","common":"Francúzsko"},"spa":{"official":"República francés","common":"Francia"},"srp":{"official":"Француска Република","common":"Француска"},"swe":{"official":"Republiken Frankrike","common":"Frankrike"},"tur":{"official":"Fransa Cumhuriyeti","common":"Fransa"},"urd":{"official":"جمہوریہ فرانس","common":"فرانس"},"zho":{"official":"法兰西共和国","common":"法国"}},"latlng":[46.0,2.0],"landlocked":false,"borders":["AND","BEL","DEU","ITA","LUX","MCO","ESP","CHE"],"area":551695.0,"demonyms":{"eng":{"f":"French","m":"French"},"fra":{"f":"Française","m":"Français"}},"flag":"\uD83C\uDDEB\uD83C\uDDF7","maps":{"googleMaps":"https://goo.gl/maps/g7QxxSFsWyTPKuzd7","openStreetMaps":"https://www.openstreetmap.org/relation/1403916"},"population":67391582,"gini":{"2018":32.4},"fifa":"FRA","car":{"signs":["F"],"side":"right"},"timezones":["UTC-10:00","UTC-09:30","UTC-09:00","UTC-08:00","UTC-04:00","UTC-03:00","UTC+01:00","UTC+02:00","UTC+03:00","UTC+04:00","UTC+05:00","UTC+10:00","UTC+11:00","UTC+12:00"],"continents":["Europe"],"flags":{"png":"https://flagcdn.com/w320/fr.png","svg":"https://flagcdn.com/fr.svg","alt":"The flag of France is composed of three equal vertical bands of blue, white and red."},"coatOfArms":{"png":"https://mainfacts.com/media/images/coats_of_arms/fr.png","svg":"https://mainfacts.com/media/images/coats_of_arms/fr.svg"},"startOfWeek":"monday","capitalInfo":{"latlng":[48.87,2.33]},"postalCode":{"format":"#####","regex":"^(\\d{5})$"}}][0m

[1m> Finished chain.[0m

```

Let's try to make an API call that is meant for the currency endpoint

```python

chain_new.run('Can you tell me about the currency COP?')

```

```

[1m> Entering new APIChain chain...[0m
[32;1m[1;3m https://restcountries.com/v3.1/currency/COP[0m
[33;1m[1;3m[{"name":{"common":"Colombia","official":"Republic of Colombia","nativeName":{"spa":{"official":"República de Colombia","common":"Colombia"}}},"tld":[".co"],"cca2":"CO","ccn3":"170","cca3":"COL","cioc":"COL","independent":true,"status":"officially-assigned","unMember":true,"currencies":{"COP":{"name":"Colombian peso","symbol":"$"}},"idd":{"root":"+5","suffixes":["7"]},"capital":["Bogotá"],"altSpellings":["CO","Republic of Colombia","República de Colombia"],"region":"Americas","subregion":"South America","languages":{"spa":"Spanish"},"translations":{"ara":{"official":"جمهورية كولومبيا","common":"كولومبيا"},"bre":{"official":"Republik Kolombia","common":"Kolombia"},"ces":{"official":"Kolumbijská republika","common":"Kolumbie"},"cym":{"official":"Gweriniaeth Colombia","common":"Colombia"},"deu":{"official":"Republik Kolumbien","common":"Kolumbien"},"est":{"official":"Colombia Vabariik","common":"Colombia"},"fin":{"official":"Kolumbian tasavalta","common":"Kolumbia"},"fra":{"official":"République de Colombie","common":"Colombie"},"hrv":{"official":"Republika Kolumbija","common":"Kolumbija"},"hun":{"official":"Kolumbiai Köztársaság","common":"Kolumbia"},"ita":{"official":"Repubblica di Colombia","common":"Colombia"},"jpn":{"official":"コロンビア共和国","common":"コロンビア"},"kor":{"official":"콜롬비아 공화국","common":"콜롬비아"},"nld":{"official":"Republiek Colombia","common":"Colombia"},"per":{"official":"جمهوری کلمبیا","common":"کلمبیا"},"pol":{"official":"Republika Kolumbii","common":"Kolumbia"},"por":{"official":"República da Colômbia","common":"Colômbia"},"rus":{"official":"Республика Колумбия","common":"Колумбия"},"slk":{"official":"Kolumbijská republika","common":"Kolumbia"},"spa":{"official":"República de Colombia","common":"Colombia"},"srp":{"official":"Република Колумбија","common":"Колумбија"},"swe":{"official":"Republiken Colombia","common":"Colombia"},"tur":{"official":"Kolombiya Cumhuriyeti","common":"Kolombiya"},"urd":{"official":"جمہوریہ کولمبیا","common":"کولمبیا"},"zho":{"official":"哥伦比亚共和国","common":"哥伦比亚"}},"latlng":[4.0,-72.0],"landlocked":false,"borders":["BRA","ECU","PAN","PER","VEN"],"area":1141748.0,"demonyms":{"eng":{"f":"Colombian","m":"Colombian"},"fra":{"f":"Colombienne","m":"Colombien"}},"flag":"\uD83C\uDDE8\uD83C\uDDF4","maps":{"googleMaps":"https://goo.gl/maps/RdwTG8e7gPwS62oR6","openStreetMaps":"https://www.openstreetmap.org/relation/120027"},"population":50882884,"gini":{"2019":51.3},"fifa":"COL","car":{"signs":["CO"],"side":"right"},"timezones":["UTC-05:00"],"continents":["South America"],"flags":{"png":"https://flagcdn.com/w320/co.png","svg":"https://flagcdn.com/co.svg","alt":"The flag of Colombia is composed of three horizontal bands of yellow, blue and red, with the yellow band twice the height of the other two bands."},"coatOfArms":{"png":"https://mainfacts.com/media/images/coats_of_arms/co.png","svg":"https://mainfacts.com/media/images/coats_of_arms/co.svg"},"startOfWeek":"monday","capitalInfo":{"latlng":[4.71,-74.07]}}][0m

[1m> Finished chain.[0m

```

In both cases the APIChain read the instructions and understood which API call it needed to make.

Once the response returned, it was parsed and then my question was answered. Awesome 🐒

## Chatbots

*[LangChain Chatbot Docs](https://python.langchain.com/en/latest/use_cases/chatbots.html)*

Chatbots use many of the tools we've already looked at with the addition of an important topic: Memory. There are a ton of different [types of memory](https://python.langchain.com/en/latest/modules/memory/how_to_guides.html), tinker to see which is best for you.

* **Deep Dive** - Coming Soon
* **Examples** - [ChatBase](https://www.chatbase.co/?via=greg) (Affiliate link), [NexusGPT](https://twitter.com/achammah1/status/1649482899253501958?s=20), [ChatPDF](https://www.chatpdf.com/)
* **Use Cases:** Have a real time interaction with a user, provide an approachable UI for users to ask natural language questions

```python

from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate

# Chat specific components
from langchain.memory import ConversationBufferMemory

```

For this use case I'm going to show you how to customize the context that is given to a chatbot.

You could pass instructions on how the bot should respond, but also any additional relevant information it needs.

```python

template = """
You are a chatbot that is unhelpful.
Your goal is to not help the user but only make jokes.
Take what the user is saying and make a joke out of it

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], 
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

```

```python

llm_chain = LLMChain(
    llm=OpenAI(openai_api_key=openai_api_key), 
    prompt=prompt, 
    verbose=True, 
    memory=memory
)

```

```python

llm_chain.predict(human_input="Is an pear a fruit or vegetable?")

```

```

[1m> Entering new LLMChain chain...[0m
Prompt after formatting:
[32;1m[1;3m
You are a chatbot that is unhelpful.
Your goal is to not help the user but only make jokes.
Take what the user is saying and make a joke out of it


Human: Is an pear a fruit or vegetable?
Chatbot:[0m

[1m> Finished chain.[0m

```

```python

llm_chain.predict(human_input="What was one of the fruits I first asked you about?")

```

```

[1m> Entering new LLMChain chain...[0m
Prompt after formatting:
[32;1m[1;3m
You are a chatbot that is unhelpful.
Your goal is to not help the user but only make jokes.
Take what the user is saying and make a joke out of it

Human: Is an pear a fruit or vegetable?
AI:  Yes, an pear is a fruit of confusion!
Human: What was one of the fruits I first asked you about?
Chatbot:[0m

[1m> Finished chain.[0m

```

Notice how my 1st interaction was put into the prompt of my 2nd interaction. This is the memory piece at work.

There are many ways to structure a conversation, check out the different ways on the [docs](https://python.langchain.com/en/latest/use_cases/chatbots.html)

## Agents

*[LangChain Agent Docs](https://python.langchain.com/en/latest/modules/agents.html)*

Agents are one of the hottest [🔥](https://media.tenor.com/IH7C6xNbkuoAAAAC/so-hot-right-now-trending.gif) topics in LLMs. Agents are the decision makers that can look a data, reason about what the next action should be, and execute that action for you via tools

* **Deep Dive** - [Introduction to agents](https://youtu.be/2xxziIWmaSA?t=1972), [LangChain Agents Webinar](https://www.crowdcast.io/c/46erbpbz609r), much deeper dive coming soon
* **Examples** - TBD
* **Use Cases:** Run programs autonomously without the need for human input

Examples of advanced uses of agents appear in [BabyAGI](https://github.com/yoheinakajima/babyagi) and [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT)


```python

# Helpers
import os
import json

from langchain.llms import OpenAI

# Agent imports
from langchain.agents import load_tools
from langchain.agents import initialize_agent

# Tool imports
from langchain.agents import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.utilities import TextRequestsWrapper

```

For this example I'm going to pull google search results. You may want to do this if you need a list of websites for a research project.

You can sign up for both of these keys at the urls below

[GOOGLE_API_KEY](https://console.cloud.google.com/apis/credentials)
[GOOGLE_CSE_ID](https://programmablesearchengine.google.com/controlpanel/create)

```python

GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID', 'YourAPIKeyIfNotSet')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'YourAPIKeyIfNotSet')

```

```python

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

Initialize both the tools you'll be using. For this example we'll search google and also give the LLM the ability to execute python code

```python

search = GoogleSearchAPIWrapper(google_api_key=GOOGLE_API_KEY, google_cse_id=GOOGLE_CSE_ID)

requests = TextRequestsWrapper()

```

Put both your tools in a toolkit

```python

toolkit = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to search google to answer questions about current events"
    ),
    Tool(
        name = "Requests",
        func=requests.get,
        description="Useful for when you to make a request to a URL"
    ),
]

```

Create your agent by giving it the tools, LLM and the type of agent that it should be

```python

agent = initialize_agent(toolkit, llm, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

```

Now ask it a question, I'm going to give it one that it should go to Google for

```python

response = agent({"input":"What is the capital of canada?"})
response['output']

```

```

[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m I need to find out what the capital of Canada is.
Action: Search
Action Input: "capital of Canada"[0m
Observation: [36;1m[1;3mLooking to build credit or earn rewards? Compare our rewards, Guaranteed secured and other Guaranteed credit cards. Canada's capital is Ottawa and its three largest metropolitan areas are Toronto, Montreal, and Vancouver. Canada. A vertical triband design (red, white, red) ... Browse available job openings at Capital One - CA. ... Together, we will build one of Canada's leading information-based technology companies – join us, ... Ottawa is the capital city of Canada. It is located in the southern portion of the province of Ontario, at the confluence of the Ottawa River and the Rideau ... Shopify Capital offers small business funding in the form of merchant cash advances to eligible merchants in Canada. If you live in Canada and need ... Download Capital One Canada and enjoy it on your iPhone, iPad and iPod touch. ... Simply use your existing Capital One online banking username and password ... A leader in the alternative asset space, TPG was built for a distinctive approach, managing assets through a principled focus on innovation. We're Canada's largest credit union by membership because we prioritize people, not profits. Let's build the right plan to reach your financial goals, together. The national capital is Ottawa, Canada's fourth largest city. It lies some 250 miles (400 km) northeast of Toronto and 125 miles (200 km) west of Montreal, ... Finding Value Across the Capital Structure: Limited Recourse Capital Notes. Limited Recourse Capital Notes are an evolving segment of the Canadian fixed-income ...[0m
Thought:[32;1m[1;3m I now know the final answer
Final Answer: Ottawa is the capital of Canada.[0m

[1m> Finished chain.[0m

```

Great, that's correct. Now let's ask a question that requires listing the currect directory

```python

response = agent({"input":"Tell me what the comments are about on this webpage https://news.ycombinator.com/item?id=34425779"})
response['output']

```

```

[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m I need to find out what the comments are about
Action: Search
Action Input: "comments on https://news.ycombinator.com/item?id=34425779"[0m
Observation: [36;1m[1;3mAbout a month after we started Y Combinator we came up with the phrase that ... Action Input: "comments on https://news.ycombinator.com/item?id=34425779" .[0m
Thought:[32;1m[1;3m I now know the comments are about Y Combinator
Final Answer: The comments on the webpage are about Y Combinator.[0m

[1m> Finished chain.[0m

```

## FIN

Wow! You made it all the way down to the bottom.

Where do you go from here?

The world of AI is massive and use cases will continue to grow. I'm personally most excited about the idea of use cases we don't know about yet.

What else should we add to this list?

Check out this [repo's ReadMe](https://github.com/gkamradt/langchain-tutorials) for more inspiration
Check out more tutorials on [YouTube](https://www.youtube.com/@DataIndependent)

I'd love to see what projects you build. Tag me on [Twitter](https://twitter.com/GregKamradt)!

Have something you'd like to edit? See our [contribution guide](https://github.com/gkamradt/langchain-tutorials) and throw up a PR