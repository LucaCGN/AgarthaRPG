# Building RAG Chatbots with LangChain

In this example, we'll work on building an AI chatbot from start-to-finish. We will be using LangChain, OpenAI, and Pinecone vector DB, to build a chatbot capable of learning from the external world using **R**etrieval **A**ugmented **G**eneration (RAG).

We will be using a dataset sourced from the Llama 2 ArXiv paper and other related papers to help our chatbot answer questions about the latest and greatest in the world of GenAI.

By the end of the example we'll have a functioning chatbot and RAG pipeline that can hold a conversation and provide informative responses based on a knowledge base.

### Before you begin

You'll need to get an [OpenAI API key](https://platform.openai.com/account/api-keys) and [Pinecone API key](https://app.pinecone.io).

### Prerequisites

Before we start building our chatbot, we need to install some Python libraries. Here's a brief overview of what each library does:

- **langchain**: This is a library for GenAI. We'll use it to chain together different language models and components for our chatbot.
- **openai**: This is the official OpenAI Python client. We'll use it to interact with the OpenAI API and generate responses for our chatbot.
- **datasets**: This library provides a vast array of datasets for machine learning. We'll use it to load our knowledge base for the chatbot.
- **pinecone-client**: This is the official Pinecone Python client. We'll use it to interact with the Pinecone API and store our chatbot's knowledge base in a vector database.

You can install these libraries using pip like so:

```python

!pip install -qU \
    langchain==0.0.292 \
    openai==0.28.0 \
    datasets==2.10.1 \
    pinecone-client==2.2.4 \
    tiktoken==0.5.1

```

### Building a Chatbot (no RAG)

We will be relying heavily on the LangChain library to bring together the different components needed for our chatbot. To begin, we'll create a simple chatbot without any retrieval augmentation. We do this by initializing a `ChatOpenAI` object. For this we do need an [OpenAI API key](https://platform.openai.com/account/api-keys).

```python

import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"

chat = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model='gpt-3.5-turbo'
)

```

Chats with OpenAI's `gpt-3.5-turbo` and `gpt-4` chat models are typically structured (in plain text) like this:

```
System: You are a helpful assistant.

User: Hi AI, how are you today?

Assistant: I'm great thank you. How can I help you?

User: I'd like to understand string theory.

Assistant:
```

The final `"Assistant:"` without a response is what would prompt the model to continue the comversation. In the official OpenAI `ChatCompletion` endpoint these would be passed to the model in a format like:

```python
[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hi AI, how are you today?"},
    {"role": "assistant", "content": "I'm great thank you. How can I help you?"}
    {"role": "user", "content": "I'd like to understand string theory."}
]
```

In LangChain there is a slightly different format. We use three _message_ objects like so:

```python

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?"),
    AIMessage(content="I'm great thank you. How can I help you?"),
    HumanMessage(content="I'd like to understand string theory.")
]

```

The format is very similar, we're just swapped the role of `"user"` for `HumanMessage`, and the role of `"assistant"` for `AIMessage`.

We generate the next response from the AI by passing these messages to the `ChatOpenAI` object.

```python

res = chat(messages)
res

```

In response we get another AI message object. We can print it more clearly like so:

```python

print(res.content)

```

```

String theory is a theoretical framework in physics that aims to provide a unified description of the fundamental particles and forces in the universe. It suggests that at the most fundamental level, particles are not point-like entities but instead tiny, vibrating strings.

Here are some key points to understand about string theory:

1. Building blocks: According to string theory, the basic building blocks of the universe are not particles but rather tiny, one-dimensional strings. These strings can vibrate in different ways, and the different modes of vibration give rise to different particle properties, such as mass and charge.

2. Extra dimensions: Unlike traditional theories, string theory requires more than the usual three dimensions of space and one dimension of time. It suggests the presence of additional, compactified dimensions that are too small for us to detect directly. These extra dimensions play a crucial role in shaping the behavior of the strings and can help explain certain fundamental aspects of the universe.

3. Quantum mechanics and gravity: String theory combines quantum mechanics and general relativity, the theory of gravity. It provides a framework for understanding how gravity can be described in terms of microscopic vibrating strings, resolving some of the conceptual conflicts between quantum mechanics and general relativity.

4. Multiple versions: There are various versions of string theory, including Type I, Type IIA, Type IIB, heterotic SO(32), and heterotic E8×E8. These different versions arise from different assumptions about the properties of the strings and their interactions.

5. Unification of forces: One of the significant achievements of string theory is its potential to unify the fundamental forces of nature – gravity, electromagnetism, the strong nuclear force, and the weak nuclear force. In string theory, these forces emerge as different vibrational modes of the strings, providing a unified description of all interactions.

It's important to note that string theory remains a highly theoretical and mathematically complex field. It is still being actively researched, and many aspects of the theory are not yet fully understood or experimentally confirmed. Nonetheless, it offers intriguing possibilities for understanding the fundamental nature of the universe.

```

Because `res` is just another `AIMessage` object, we can append it to `messages`, add another `HumanMessage`, and generate the next response in the conversation.

```python

# add latest AI response to messages
messages.append(res)

# now create a new user prompt
prompt = HumanMessage(
    content="Why do physicists believe it can produce a 'unified theory'?"
)
# add to messages
messages.append(prompt)

# send to chat-gpt
res = chat(messages)

print(res.content)

```

```

Physicists believe that string theory has the potential to produce a unified theory because of several reasons:

1. Consistency with known physics: String theory incorporates and extends the principles of quantum mechanics and general relativity, two highly successful theories in their respective domains. It provides a framework that can naturally accommodate both quantum mechanics and gravity, which have been challenging to reconcile in other approaches.

2. Explanation of particle properties: String theory offers a way to explain the properties of particles, such as their masses and charges, in terms of the vibrations and interactions of the tiny strings. It provides a more fundamental and elegant description compared to the ad hoc assignments of properties in other theories.

3. Grand unification of forces: In the standard model of particle physics, the three fundamental forces (electromagnetism, weak nuclear force, and strong nuclear force) are described independently and have different strengths. String theory suggests that these forces can be unified into a single framework. The different vibrational modes of the strings correspond to the different forces, allowing for a unified description of all interactions.

4. Extra dimensions and symmetry: String theory requires the existence of extra dimensions beyond the usual four dimensions of space and time. These extra dimensions can help explain certain features of the universe, such as the hierarchy problem (why the gravitational force is so much weaker than the other forces) and the existence of different particle generations. The mathematical symmetries inherent in string theory also provide a basis for unification.

5. Mathematical elegance: String theory is highly mathematically consistent and elegant. It relies on sophisticated mathematical techniques, such as conformal field theory and algebraic geometry, which have been extensively studied and developed over many decades. The mathematical beauty and internal consistency of the theory give physicists confidence in its potential for a unified description.

It's worth noting that while string theory shows promise, it has not yet been experimentally confirmed. Further research and experimental data are needed to verify its predictions and determine its applicability to the physical world.

```

### Dealing with Hallucinations

We have our chatbot, but as mentioned — the knowledge of LLMs can be limited. The reason for this is that LLMs learn all they know during training. An LLM essentially compresses the "world" as seen in the training data into the internal parameters of the model. We call this knowledge the _parametric knowledge_ of the model.

By default, LLMs have no access to the external world.

The result of this is very clear when we ask LLMs about more recent information, like about the new (and very popular) Llama 2 LLM.

```python

# add latest AI response to messages
messages.append(res)

# now create a new user prompt
prompt = HumanMessage(
    content="What is so special about Llama 2?"
)
# add to messages
messages.append(prompt)

# send to OpenAI
res = chat(messages)

```

```python

print(res.content)

```

```

I apologize, but I'm not familiar with Llama 2. Could you please provide more context or clarify what you are referring to? That way, I can try to assist you better.

```

Our chatbot can no longer help us, it doesn't contain the information we need to answer the question. It was very clear from this answer that the LLM doesn't know the informaiton, but sometimes an LLM may respond like it _does_ know the answer — and this can be very hard to detect.

OpenAI have since adjusted the behavior for this particular example as we can see below:

```python

# add latest AI response to messages
messages.append(res)

# now create a new user prompt
prompt = HumanMessage(
    content="Can you tell me about the LLMChain in LangChain?"
)
# add to messages
messages.append(prompt)

# send to OpenAI
res = chat(messages)

```

```python

print(res.content)

```

```

I'm sorry, but I couldn't find any specific information about LLMChain in LangChain. It's possible that it may be a specific term or concept related to a particular project or technology that is not widely known or documented. Without more context or information, it's difficult for me to provide a detailed explanation. 

If you can provide more details or clarify the context in which LLMChain is mentioned, I'll do my best to assist you further.

```

There is another way of feeding knowledge into LLMs. It is called _source knowledge_ and it refers to any information fed into the LLM via the prompt. We can try that with the LLMChain question. We can take a description of this object from the LangChain documentation.

```python

llmchain_information = [
    "A LLMChain is the most common type of chain. It consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser. This chain takes multiple input variables, uses the PromptTemplate to format them into a prompt. It then passes that to the model. Finally, it uses the OutputParser (if provided) to parse the output of the LLM into a final format.",
    "Chains is an incredibly generic concept which returns to a sequence of modular components (or other chains) combined in a particular way to accomplish a common use case.",
    "LangChain is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model via an api, but will also: (1) Be data-aware: connect a language model to other sources of data, (2) Be agentic: Allow a language model to interact with its environment. As such, the LangChain framework is designed with the objective in mind to enable those types of applications."
]

source_knowledge = "\n".join(llmchain_information)

```

We can feed this additional knowledge into our prompt with some instructions telling the LLM how we'd like it to use this information alongside our original query.

```python

query = "Can you tell me about the LLMChain in LangChain?"

augmented_prompt = f"""Using the contexts below, answer the query.

Contexts:
{source_knowledge}

Query: {query}"""

```

Now we feed this into our chatbot as we were before.

```python

# create a new user prompt
prompt = HumanMessage(
    content=augmented_prompt
)
# add to messages
messages.append(prompt)

# send to OpenAI
res = chat(messages)

```

```python

print(res.content)

```

```

LLMChain, as described in the provided context, is a type of chain within the LangChain framework. Chains in LangChain refer to sequences of modular components or other chains that are combined in a specific way to achieve a common purpose.

The LLMChain, specifically, is a common type of chain within LangChain. It consists of three main components: a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser.

When using an LLMChain, multiple input variables are taken and formatted into a prompt using the PromptTemplate. This formatted prompt is then passed to the language model (either an LLM or a ChatModel) within the chain. Finally, the output of the language model is processed by the OutputParser (if provided) to transform it into a final format.

The LangChain framework itself aims to go beyond simply calling a language model via an API. It emphasizes two key aspects: being data-aware and being agentic. Being data-aware means connecting the language model to other sources of data, allowing for a richer understanding and integration of information. Being agentic refers to enabling the language model to interact with its environment, making it more capable of dynamic and interactive applications.

In summary, the LLMChain is a specific type of chain within the LangChain framework that facilitates the use of language models by combining prompts, models, and output parsers to process and format inputs and outputs in a desired manner.

```

The quality of this answer is phenomenal. This is made possible thanks to the idea of augmented our query with external knowledge (source knowledge). There's just one problem — how do we get this information in the first place?

We learned in the previous chapters about Pinecone and vector databases. Well, they can help us here too. But first, we'll need a dataset.

### Importing the Data

In this task, we will be importing our data. We will be using the Hugging Face Datasets library to load our data. Specifically, we will be using the `"jamescalam/llama-2-arxiv-papers"` dataset. This dataset contains a collection of ArXiv papers which will serve as the external knowledge base for our chatbot.

```python

from datasets import load_dataset

dataset = load_dataset(
    "jamescalam/llama-2-arxiv-papers-chunked",
    split="train"
)

dataset

```

```python

dataset[0]

```

#### Dataset Overview

The dataset we are using is sourced from the Llama 2 ArXiv papers. It is a collection of academic papers from ArXiv, a repository of electronic preprints approved for publication after moderation. Each entry in the dataset represents a "chunk" of text from these papers.

Because most **L**arge **L**anguage **M**odels (LLMs) only contain knowledge of the world as it was during training, they cannot answer our questions about Llama 2 — at least not without this data.

### Task 4: Building the Knowledge Base

We now have a dataset that can serve as our chatbot knowledge base. Our next task is to transform that dataset into the knowledge base that our chatbot can use. To do this we must use an embedding model and vector database.

We begin by initializing our connection to Pinecone, this requires a [free API key](https://app.pinecone.io).

```python

import pinecone

# get API key from app.pinecone.io and environment from console
pinecone.init(
    api_key=os.environ.get('PINECONE_API_KEY') or 'YOUR_API_KEY',
    environment=os.environ.get('PINECONE_ENVIRONMENT') or 'YOUR_ENV'
)

```

Then we initialize the index. We will be using OpenAI's `text-embedding-ada-002` model for creating the embeddings, so we set the `dimension` to `1536`.

```python

import time

index_name = 'llama-2-rag'

if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        index_name,
        dimension=1536,
        metric='cosine'
    )
    # wait for index to finish initialization
    while not pinecone.describe_index(index_name).status['ready']:
        time.sleep(1)

index = pinecone.Index(index_name)

```

Then we connect to the index:

```python

index.describe_index_stats()

```

Our index is now ready but it's empty. It is a vector index, so it needs vectors. As mentioned, to create these vector embeddings we will OpenAI's `text-embedding-ada-002` model — we can access it via LangChain like so:

```python

from langchain.embeddings.openai import OpenAIEmbeddings

embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")

```

Using this model we can create embeddings like so:

```python

texts = [
    'this is the first chunk of text',
    'then another second chunk of text is here'
]

res = embed_model.embed_documents(texts)
len(res), len(res[0])

```

From this we get two (aligning to our two chunks of text) 1536-dimensional embeddings.

We're now ready to embed and index all our our data! We do this by looping through our dataset and embedding and inserting everything in batches.

```python

from tqdm.auto import tqdm  # for progress bar

data = dataset.to_pandas()  # this makes it easier to iterate over the dataset

batch_size = 100

for i in tqdm(range(0, len(data), batch_size)):
    i_end = min(len(data), i+batch_size)
    # get batch of data
    batch = data.iloc[i:i_end]
    # generate unique ids for each chunk
    ids = [f"{x['doi']}-{x['chunk-id']}" for i, x in batch.iterrows()]
    # get text to embed
    texts = [x['chunk'] for _, x in batch.iterrows()]
    # embed text
    embeds = embed_model.embed_documents(texts)
    # get metadata to store in Pinecone
    metadata = [
        {'text': x['chunk'],
         'source': x['source'],
         'title': x['title']} for i, x in batch.iterrows()
    ]
    # add to Pinecone
    index.upsert(vectors=zip(ids, embeds, metadata))

```

```

0%|          | 0/49 [00:00<?, ?it/s]

```

We can check that the vector index has been populated using `describe_index_stats` like before:

```python

index.describe_index_stats()

```

#### Retrieval Augmented Generation

We've built a fully-fledged knowledge base. Now it's time to connect that knowledge base to our chatbot. To do that we'll be diving back into LangChain and reusing our template prompt from earlier.

To use LangChain here we need to load the LangChain abstraction for a vector index, called a `vectorstore`. We pass in our vector `index` to initialize the object.

```python

from langchain.vectorstores import Pinecone

text_field = "text"  # the metadata field that contains our text

# initialize the vector store object
vectorstore = Pinecone(
    index, embed_model.embed_query, text_field
)

```

Using this `vectorstore` we can already query the index and see if we have any relevant information given our question about Llama 2.

```python

query = "What is so special about Llama 2?"

vectorstore.similarity_search(query, k=3)

```

We return a lot of text here and it's not that clear what we need or what is relevant. Fortunately, our LLM will be able to parse this information much faster than us. All we need is to connect the output from our `vectorstore` to our `chat` chatbot. To do that we can use the same logic as we used earlier.

```python

def augment_prompt(query: str):
    # get top 3 results from knowledge base
    results = vectorstore.similarity_search(query, k=3)
    # get the text from the results
    source_knowledge = "\n".join([x.page_content for x in results])
    # feed into an augmented prompt
    augmented_prompt = f"""Using the contexts below, answer the query.

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augmented_prompt

```

Using this we produce an augmented prompt:

```python

print(augment_prompt(query))

```

```

Using the contexts below, answer the query.

    Contexts:
    Alan Schelten Ruan Silva Eric Michael Smith Ranjan Subramanian Xiaoqing Ellen Tan Binh Tang
Ross Taylor Adina Williams Jian Xiang Kuan Puxin Xu Zheng Yan Iliyan Zarov Yuchen Zhang
Angela Fan Melanie Kambadur Sharan Narang Aurelien Rodriguez Robert Stojnic
Sergey Edunov Thomas Scialom
GenAI, Meta
Abstract
In this work, we develop and release Llama 2, a collection of pretrained and ﬁne-tuned
large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters.
Our ﬁne-tuned LLMs, called L/l.sc/a.sc/m.sc/a.sc /two.taboldstyle-C/h.sc/a.sc/t.sc , are optimized for dialogue use cases. Our
models outperform open-source chat models on most benchmarks we tested, and based on
ourhumanevaluationsforhelpfulnessandsafety,maybeasuitablesubstituteforclosedsource models. We provide a detailed description of our approach to ﬁne-tuning and safety
asChatGPT,BARD,andClaude. TheseclosedproductLLMsareheavilyﬁne-tunedtoalignwithhuman
preferences, which greatly enhances their usability and safety. This step can require signiﬁcant costs in
computeandhumanannotation,andisoftennottransparentoreasilyreproducible,limitingprogresswithin
the community to advance AI alignment research.
In this work, we develop and release Llama 2, a family of pretrained and ﬁne-tuned LLMs, L/l.sc/a.sc/m.sc/a.sc /two.taboldstyle and
L/l.sc/a.sc/m.sc/a.sc /two.taboldstyle-C/h.sc/a.sc/t.sc , at scales up to 70B parameters. On the series of helpfulness and safety benchmarks we tested,
L/l.sc/a.sc/m.sc/a.sc /two.taboldstyle-C/h.sc/a.sc/t.sc models generally perform better than existing open-source models. They also appear to
be on par with some of the closed-source models, at least on the human evaluations we performed (see
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aur’elien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. Llama: Open and eﬃcient foundation language models. arXiv preprint
arXiv:2302.13971 , 2023.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser,
and Illia Polosukhin. Attention is all you need, 2017.
Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki, Michaël Mathieu, Andrew Dudzik, Junyoung Chung,
David H Choi, Richard Powell, Timo Ewalds, Petko Georgiev, et al. Grandmaster level in starcraft ii using
multi-agent reinforcement learning. Nature, 575(7782):350–354, 2019.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and HannanehHajishirzi. Self-instruct: Aligninglanguagemodel withselfgeneratedinstructions. arXivpreprint

    Query: What is so special about Llama 2?

```

There is still a lot of text here, so let's pass it onto our chat model to see how it performs.

```python

# create a new user prompt
prompt = HumanMessage(
    content=augment_prompt(query)
)
# add to messages
messages.append(prompt)

res = chat(messages)

print(res.content)

```

```

Llama 2 is a collection of pretrained and fine-tuned large language models (LLMs) that range in scale from 7 billion to 70 billion parameters. These LLMs, such as L/l.sc/a.sc/m.sc/a.sc/t.sc and L/l.sc/a.sc/m.sc/a.sc/t.sc-C/h.sc/a.sc/t.sc, are specifically optimized for dialogue use cases.

The special aspect of Llama 2 is that its fine-tuned LLMs outperform open-source chat models on various benchmarks, demonstrating superior performance. In fact, based on humane evaluations for helpfulness and safety, Llama 2 models are considered as potential substitutes for closed-source models. Closed-source models like ChatGPT, BARD, and Claude are heavily fine-tuned to align with human preferences, enhancing usability and safety.

The development and release of Llama 2 contribute to the progress of AI alignment research, as it provides transparent and reproducible approaches to fine-tuning and safety. This is in contrast to closed-source models, which often lack transparency and hinder community advancements in the field.

Overall, the special features of Llama 2 lie in its large-scale pretrained and fine-tuned LLMs that excel in dialogue applications and its commitment to transparency and reproducibility in research.

```

We can continue with more Llama 2 questions. Let's try _without_ RAG first:

```python

prompt = HumanMessage(
    content="what safety measures were used in the development of llama 2?"
)

res = chat(messages + [prompt])
print(res.content)

```

```

According to the provided context, the paper mentions that they provide a detailed description of their approach to fine-tuning and safety, similar to other closed-source models like ChatGPT, BARD, and Claude. However, the specific safety measures used in the development of Llama 2 are not mentioned in the given context. To obtain more detailed information about the safety measures employed in Llama 2, it would be necessary to refer to the original paper or additional sources related to Llama 2.

```

The chatbot is able to respond about Llama 2 thanks to it's conversational history stored in `messages`. However, it doesn't know anything about the safety measures themselves as we have not provided it with that information via the RAG pipeline. Let's try again but with RAG.

```python

prompt = HumanMessage(
    content=augment_prompt(
        "what safety measures were used in the development of llama 2?"
    )
)

res = chat(messages + [prompt])
print(res.content)

```

```

The safety measures used in the development of Llama 2 include safety-specific data annotation and tuning, conducting red-teaming, and employing iterative evaluations. These measures were taken to increase the safety of the models and ensure responsible development. The paper also provides a thorough description of the fine-tuning methodology and approach to improving LLM safety. By sharing these details and being open about the process, the aim is to enable the community to reproduce fine-tuned LLMs and continue to improve their safety, promoting responsible development in the field.

```

We get a much more informed response that includes several items missing in the previous non-RAG response, such as "red-teaming", "iterative evaluations", and the intention of the researchers to share this research to help "improve their safety, promoting responsible development in the field".