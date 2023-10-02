# LangChain Cookbook 👨‍🍳👩‍🍳

*This cookbook is based off the [LangChain Conceptual Documentation](https://docs.langchain.com/docs/)*

**Goal:** Provide an introductory understanding of the components and use cases of LangChain via [ELI5](https://www.dictionary.com/e/slang/eli5/#:~:text=ELI5%20is%20short%20for%20%E2%80%9CExplain,a%20complicated%20question%20or%20problem.) examples and code snippets. For use cases check out [part 2](./LangChain%20Cookbook%20Part%202%20-%20Use%20Cases.ipynb).


**Links:**
* [LC Conceptual Documentation](https://docs.langchain.com/docs/)
* [LC Python Documentation](https://python.langchain.com/en/latest/)
* [LC Javascript/Typescript Documentation](https://js.langchain.com/docs/)
* [LC Discord](https://discord.gg/6adMQxSpJS)
* [www.langchain.com](https://langchain.com/)
* [LC Twitter](https://twitter.com/LangChainAI)


### **What is LangChain?**
> LangChain is a framework for developing applications powered by language models.

**~~TL~~DR**: LangChain makes the complicated parts of working & building with AI models easier. It helps do this in two ways:

1. **Integration** - Bring external data, such as your files, other applications, and api data, to your LLMs
2. **Agency** - Allow your LLMs to interact with it's environment via decision making. Use LLMs to help decide which action to take next

### **Why LangChain?**
1. **Components** - LangChain makes it easy to swap out abstractions and components necessary to work with language models.

2. **Customized Chains** - LangChain provides out of the box support for using and customizing 'chains' - a series of actions strung together.

3. **Speed 🚢** - This team ships insanely fast. You'll be up to date with the latest LLM features.

4. **Community 👥** - Wonderful discord and community support, meet ups, hackathons, etc.

Though LLMs can be straightforward (text-in, text-out) you'll quickly run into friction points that LangChain helps with once you develop more complicated applications.

*Note: This cookbook will not cover all aspects of LangChain. It's contents have been curated to get you to building & impact as quick as possible. For more, please check out [LangChain Conceptual Documentation](https://docs.langchain.com/docs/)*

```python

openai_api_key='YourAPIKey'

```

# LangChain Components

## Schema - Nuts and Bolts of working with LLMs

### **Text**
The natural language way to interact with LLMs

```python

# You'll be working with simple strings (that'll soon grow in complexity!)
my_text = "What day comes after Friday?"

```

### **Chat Messages**
Like text, but specified with a message type (System, Human, AI)

* **System** - Helpful background context that tell the AI what to do
* **Human** - Messages that are intented to represent the user
* **AI** - Messages that show what the AI responded with

For more, see OpenAI's [documentation](https://platform.openai.com/docs/guides/chat/introduction)

```python

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=.7, openai_api_key=openai_api_key)

```

```python

chat(
    [
        SystemMessage(content="You are a nice AI bot that helps a user figure out what to eat in one short sentence"),
        HumanMessage(content="I like tomatoes, what should I eat?")
    ]
)

```

You can also pass more chat history w/ responses from the AI

```python

chat(
    [
        SystemMessage(content="You are a nice AI bot that helps a user figure out where to travel in one short sentence"),
        HumanMessage(content="I like the beaches where should I go?"),
        AIMessage(content="You should go to Nice, France"),
        HumanMessage(content="What else should I do when I'm there?")
    ]
)

```

### **Documents**
An object that holds a piece of text and metadata (more information about that text)

```python

from langchain.schema import Document

```

```python

Document(page_content="This is my document. It is full of text that I've gathered from other places",
         metadata={
             'my_document_id' : 234234,
             'my_document_source' : "The LangChain Papers",
             'my_document_create_time' : 1680013019
         })

```

## Models - The interface to the AI brains

###  **Language Model**
A model that does text in ➡️ text out!

*Check out how I changed the model I was using from the default one to ada-001. See more models [here](https://platform.openai.com/docs/models)*

```python

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", openai_api_key=openai_api_key)

```

```python

llm("What day comes after Friday?")

```

### **Chat Model**
A model that takes a series of messages and returns a message output

```python

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=1, openai_api_key=openai_api_key)

```

```python

chat(
    [
        SystemMessage(content="You are an unhelpful AI bot that makes a joke at whatever the user says"),
        HumanMessage(content="I would like to go to New York, how should I do this?")
    ]
)

```

### **Text Embedding Model**
Change your text into a vector (a series of numbers that hold the semantic 'meaning' of your text). Mainly used when comparing two pieces of text together.

*BTW: Semantic means 'relating to meaning in language or logic.'*

```python

from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

```

```python

text = "Hi! It's time for the beach"

```

```python

text_embedding = embeddings.embed_query(text)
print (f"Your embedding is length {len(text_embedding)}")
print (f"Here's a sample: {text_embedding[:5]}...")

```

```

Your embedding is length 1536
Here's a sample: [-0.00020583387231454253, -0.003205398330464959, -0.0008301587076857686, -0.01946892775595188, -0.015162716619670391]...

```

## Prompts - Text generally used as instructions to your model

### **Prompt**
What you'll pass to the underlying model

```python

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)

# I like to use three double quotation marks for my prompts because it's easier to read
prompt = """
Today is Monday, tomorrow is Wednesday.

What is wrong with that statement?
"""

llm(prompt)

```

### **Prompt Template**
An object that helps create prompts based on a combination of user input, other non-static information and a fixed template string.

Think of it as an [f-string](https://realpython.com/python-f-strings/) in python but for prompts

```python

from langchain.llms import OpenAI
from langchain import PromptTemplate

llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)

# Notice "location" below, that is a placeholder for another value later
template = """
I really want to travel to {location}. What should I do there?

Respond in one short sentence
"""

prompt = PromptTemplate(
    input_variables=["location"],
    template=template,
)

final_prompt = prompt.format(location='Rome')

print (f"Final Prompt: {final_prompt}")
print ("-----------")
print (f"LLM Output: {llm(final_prompt)}")

```

```

Final Prompt: 
I really want to travel to Rome. What should I do there?

Respond in one short sentence

-----------
LLM Output: 
Explore the Colosseum, the Roman Forum, the Pantheon, and the Trevi Fountain.

```

### **Example Selectors**
An easy way to select from a series of examples that allow you to dynamic place in-context information into your prompt. Often used when your task is nuanced or you have a large list of examples.

Check out different types of example selectors [here](https://python.langchain.com/docs/modules/model_io/prompts/example_selectors/)

If you want an overview on why examples are important (prompt engineering), check out [this video](https://www.youtube.com/watch?v=dOxUroR57xs)

```python

from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Example Input: {input}\nExample Output: {output}",
)

# Examples of locations that nouns are found
examples = [
    {"input": "pirate", "output": "ship"},
    {"input": "pilot", "output": "plane"},
    {"input": "driver", "output": "car"},
    {"input": "tree", "output": "ground"},
    {"input": "bird", "output": "nest"},
]

```

```python

# SemanticSimilarityExampleSelector will select examples that are similar to your input by semantic meaning

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples, 
    
    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(openai_api_key=openai_api_key), 
    
    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    FAISS, 
    
    # This is the number of examples to produce.
    k=2
)

```

```python

similar_prompt = FewShotPromptTemplate(
    # The object that will help select examples
    example_selector=example_selector,
    
    # Your prompt
    example_prompt=example_prompt,
    
    # Customizations that will be added to the top and bottom of your prompt
    prefix="Give the location an item is usually found in",
    suffix="Input: {noun}\nOutput:",
    
    # What inputs your prompt will receive
    input_variables=["noun"],
)

```

```python

# Select a noun!
my_noun = "student"

print(similar_prompt.format(noun=my_noun))

```

```

Give the location an item is usually found in

Example Input: driver
Example Output: car

Example Input: pilot
Example Output: plane

Input: student
Output:

```

```python

llm(similar_prompt.format(noun=my_noun))

```

### **Output Parsers**
A helpful way to format the output of a model. Usually used for structured output.

Two big concepts:

**1. Format Instructions** - A autogenerated prompt that tells the LLM how to format it's response based off your desired result

**2. Parser** - A method which will extract your model's text output into a desired structure (usually json)

```python

from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI

```

```python

llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)

```

```python

# How you would like your response structured. This is basically a fancy prompt template
response_schemas = [
    ResponseSchema(name="bad_string", description="This a poorly formatted user input string"),
    ResponseSchema(name="good_string", description="This is your response, a reformatted response")
]

# How you would like to parse your output
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

```

```python

# See the prompt template you created for formatting
format_instructions = output_parser.get_format_instructions()
print (format_instructions)

```

```

The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json
{
	"bad_string": string  // This a poorly formatted user input string
	"good_string": string  // This is your response, a reformatted response
}
```

```

```python

template = """
You will be given a poorly formatted string from a user.
Reformat it and make sure all the words are spelled correctly

{format_instructions}

% USER INPUT:
{user_input}

YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["user_input"],
    partial_variables={"format_instructions": format_instructions},
    template=template
)

promptValue = prompt.format(user_input="welcom to califonya!")

print(promptValue)

```

```

You will be given a poorly formatted string from a user.
Reformat it and make sure all the words are spelled correctly

The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

```json
{
	"bad_string": string  // This a poorly formatted user input string
	"good_string": string  // This is your response, a reformatted response
}
```

% USER INPUT:
welcom to califonya!

YOUR RESPONSE:

```

```python

llm_output = llm(promptValue)
llm_output

```

```python

output_parser.parse(llm_output)

```

## Indexes - Structuring documents to LLMs can work with them

### **Document Loaders**
Easy ways to import data from other sources. Shared functionality with [OpenAI Plugins](https://openai.com/blog/chatgpt-plugins) [specifically retrieval plugins](https://github.com/openai/chatgpt-retrieval-plugin)

See a [big list](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html) of document loaders here. A bunch more on [Llama Index](https://llamahub.ai/) as well.

```python

from langchain.document_loaders import HNLoader

```

```python

loader = HNLoader("https://news.ycombinator.com/item?id=34422627")

```

```python

data = loader.load()

```

```python

print (f"Found {len(data)} comments")
print (f"Here's a sample:\n\n{''.join([x.page_content[:150] for x in data[:2]])}")

```

```

Found 76 comments
Here's a sample:

Ozzie_osman 3 months ago  
             | next [–] 

LangChain is awesome. For people not sure what it's doing, large language models (LLMs) are very Ozzie_osman 3 months ago  
             | parent | next [–] 

Also, another library to check out is GPT Index (https://github.com/jerryjliu/gpt_index)

```

### **Text Splitters**
Often times your document is too long (like a book) for your LLM. You need to split it up into chunks. Text splitters help with this.

There are many ways you could split your text into chunks, experiment with [different ones](https://python.langchain.com/en/latest/modules/indexes/text_splitters.html) to see which is best for you.

```python

from langchain.text_splitter import RecursiveCharacterTextSplitter

```

```python

# This is a long document we can split up.
with open('data/PaulGrahamEssays/worked.txt') as f:
    pg_work = f.read()
    
print (f"You have {len([pg_work])} document")

```

```

You have 1 document

```

```python

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 150,
    chunk_overlap  = 20,
)

texts = text_splitter.create_documents([pg_work])

```

```python

print (f"You have {len(texts)} documents")

```

```

You have 606 documents

```

```python

print ("Preview:")
print (texts[0].page_content, "\n")
print (texts[1].page_content)

```

```

Preview:
February 2021Before college the two main things I worked on, outside of school,
were writing and programming. I didn't write essays. I wrote what 

beginning writers were supposed to write then, and probably still
are: short stories. My stories were awful. They had hardly any plot,

```

### **Retrievers**
Easy way to combine documents with language models.

There are many different types of retrievers, the most widely supported is the VectoreStoreRetriever

```python

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = TextLoader('data/PaulGrahamEssays/worked.txt')
documents = loader.load()

```

```python

# Get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

# Split your docs into texts
texts = text_splitter.split_documents(documents)

# Get embedding engine ready
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Embedd your texts
db = FAISS.from_documents(texts, embeddings)

```

```python

# Init your retriever. Asking for just 1 document back
retriever = db.as_retriever()

```

```python

retriever

```

```python

docs = retriever.get_relevant_documents("what types of things did the author want to build?")

```

```python

print("\n\n".join([x.page_content[:200] for x in docs[:2]]))

```

```

standards; what was the point? No one else wanted one either, so
off they went. That was what happened to systems work.I wanted not just to build things, but to build things that would
last.In this di

much of it in grad school.Computer Science is an uneasy alliance between two halves, theory
and systems. The theory people prove things, and the systems people
build things. I wanted to build things.

```

### **VectorStores**
Databases to store vectors. Most popular ones are [Pinecone](https://www.pinecone.io/) & [Weaviate](https://weaviate.io/). More examples on OpenAIs [retriever documentation](https://github.com/openai/chatgpt-retrieval-plugin#choosing-a-vector-database). [Chroma](https://www.trychroma.com/) & [FAISS](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/) are easy to work with locally.

Conceptually, think of them as tables w/ a column for embeddings (vectors) and a column for metadata.

Example

| Embedding      | Metadata |
| ----------- | ----------- |
| [-0.00015641732898075134, -0.003165106289088726, ...]      | {'date' : '1/2/23}       |
| [-0.00035465431654651654, 1.4654131651654516546, ...]   | {'date' : '1/3/23}        |

```python

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = TextLoader('data/PaulGrahamEssays/worked.txt')
documents = loader.load()

# Get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

# Split your docs into texts
texts = text_splitter.split_documents(documents)

# Get embedding engine ready
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

```

```python

print (f"You have {len(texts)} documents")

```

```

You have 78 documents

```

```python

embedding_list = embeddings.embed_documents([text.page_content for text in texts])

```

```python

print (f"You have {len(embedding_list)} embeddings")
print (f"Here's a sample of one: {embedding_list[0][:3]}...")

```

```

You have 78 embeddings
Here's a sample of one: [-0.0011257503838977907, -0.011114791224843646, -0.012860921430454107]...

```

Your vectorstore store your embeddings (☝️) and make them easily searchable

## Memory
Helping LLMs remember information.

Memory is a bit of a loose term. It could be as simple as remembering information you've chatted about in the past or more complicated information retrieval.

We'll keep it towards the Chat Message use case. This would be used for chat bots.

There are many types of memory, explore [the documentation](https://python.langchain.com/en/latest/modules/memory/how_to_guides.html) to see which one fits your use case.

### Chat Message History

```python

from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

history = ChatMessageHistory()

history.add_ai_message("hi!")

history.add_user_message("what is the capital of france?")

```

```python

history.messages

```

```python

ai_response = chat(history.messages)
ai_response

```

```python

history.add_ai_message(ai_response.content)
history.messages

```

## Chains ⛓️⛓️⛓️
Combining different LLM calls and action automatically

Ex: Summary #1, Summary #2, Summary #3 > Final Summary

Check out [this video](https://www.youtube.com/watch?v=f9_BWhCI4Zo&t=2s) explaining different summarization chain types

There are [many applications of chains](https://python.langchain.com/en/latest/modules/chains/how_to_guides.html) search to see which are best for your use case.

We'll cover two of them:

### 1. Simple Sequential Chains

Easy chains where you can use the output of an LLM as an input into another. Good for breaking up tasks (and keeping your LLM focused)

```python

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

llm = OpenAI(temperature=1, openai_api_key=openai_api_key)

```

```python

template = """Your job is to come up with a classic dish from the area that the users suggests.
% USER LOCATION
{user_location}

YOUR RESPONSE:
"""
prompt_template = PromptTemplate(input_variables=["user_location"], template=template)

# Holds my 'location' chain
location_chain = LLMChain(llm=llm, prompt=prompt_template)

```

```python

template = """Given a meal, give a short and simple recipe on how to make that dish at home.
% MEAL
{user_meal}

YOUR RESPONSE:
"""
prompt_template = PromptTemplate(input_variables=["user_meal"], template=template)

# Holds my 'meal' chain
meal_chain = LLMChain(llm=llm, prompt=prompt_template)

```

```python

overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain], verbose=True)

```

```python

review = overall_chain.run("Rome")

```

```

[1m> Entering new SimpleSequentialChain chain...[0m
[36;1m[1;3mA classic dish from Rome is Spaghetti alla Carbonara. This dish is a creamy pasta made with eggs, cured pork, Pecorino Romano cheese, black pepper, and Olive oil.[0m
[33;1m[1;3m1. Bring a large pot of salted water to a boil.
2. Add about a pound of spaghetti noodles and cook for 8-10 minutes, stirring occasionally.
3. Drain noodles and set aside.
4. In a separate bowl, whisk together 2 eggs and ½ cup of Pecorino Romano cheese.
5. In a large skillet, heat 2 tablespoons of olive oil over medium heat.
6. Add 4 ounces of cubed pancetta or guanciale and cook until lightly browned, stirring often.
7. Reduce heat to low and add the spaghetti noodles.
8. Pour the egg mixture over the noodles and vigorously stir together.
9. Remove from heat, stir in a pinch of black pepper and serve.[0m

[1m> Finished chain.[0m

```

### 2. Summarization Chain

Easily run through long numerous documents and get a summary. Check out [this video](https://www.youtube.com/watch?v=f9_BWhCI4Zo) for other chain types besides map-reduce

```python

from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = TextLoader('data/PaulGrahamEssays/disc.txt')
documents = loader.load()

# Get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)

# Split your docs into texts
texts = text_splitter.split_documents(documents)

# There is a lot of complexity hidden in this one line. I encourage you to check out the video above for more detail
chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
chain.run(texts)

```

```

[1m> Entering new MapReduceDocumentsChain chain...[0m


[1m> Entering new LLMChain chain...[0m
Prompt after formatting:
[32;1m[1;3mWrite a concise summary of the following:


"January 2017Because biographies of famous scientists tend to 
edit out their mistakes, we underestimate the 
degree of risk they were willing to take.
And because anything a famous scientist did that
wasn't a mistake has probably now become the
conventional wisdom, those choices don't
seem risky either.Biographies of Newton, for example, understandably focus
more on physics than alchemy or theology.
The impression we get is that his unerring judgment
led him straight to truths no one else had noticed.
How to explain all the time he spent on alchemy
and theology?  Well, smart people are often kind of
crazy.But maybe there is a simpler explanation. Maybe"


CONCISE SUMMARY:[0m
Prompt after formatting:
[32;1m[1;3mWrite a concise summary of the following:


"the smartness and the craziness were not as separate
as we think. Physics seems to us a promising thing
to work on, and alchemy and theology obvious wastes
of time. But that's because we know how things
turned out. In Newton's day the three problems 
seemed roughly equally promising. No one knew yet
what the payoff would be for inventing what we
now call physics; if they had, more people would 
have been working on it. And alchemy and theology
were still then in the category Marc Andreessen would 
describe as "huge, if true."Newton made three bets. One of them worked. But 
they were all risky."


CONCISE SUMMARY:[0m

[1m> Finished chain.[0m


[1m> Entering new StuffDocumentsChain chain...[0m


[1m> Entering new LLMChain chain...[0m
Prompt after formatting:
[32;1m[1;3mWrite a concise summary of the following:


" Biographies of famous scientists fail to show the risks they took and the mistakes they made, leading to an unbalanced impression. Explaining the detours taken in their exploration of topics such as alchemy and theology, smart people are often thought of as crazy; however, there may be a simpler explanation.

 In Newton's day, no one knew how successful inventing physics, alchemy, and theology would be. But Newton made the decision to pursue all three topics, and one of them was a success. Even though our current view is that physics is the superior venture and alchemy and theology are waste of time, Newton's risky decision shows that these things were once considered equally important."


CONCISE SUMMARY:[0m

[1m> Finished chain.[0m

[1m> Finished chain.[0m

[1m> Finished chain.[0m

```

## Agents 🤖🤖

Official LangChain Documentation describes agents perfectly (emphasis mine):
> Some applications will require not just a predetermined chain of calls to LLMs/other tools, but potentially an **unknown chain** that depends on the user's input. In these types of chains, there is a “agent” which has access to a suite of tools. Depending on the user input, the agent can then **decide which, if any, of these tools to call**.


Basically you use the LLM not just for text output, but also for decision making. The coolness and power of this functionality can't be overstated enough.

Sam Altman emphasizes that the LLMs are good '[reasoning engine](https://www.youtube.com/watch?v=L_Guz73e6fw&t=867s)'. Agent take advantage of this.

### Agents

The language model that drives decision making.

More specifically, an agent takes in an input and returns a response corresponding to an action to take along with an action input. You can see different types of agents (which are better for different use cases) [here](https://python.langchain.com/en/latest/modules/agents/agent_types.html).

### Tools

A 'capability' of an agent. This is an abstraction on top of a function that makes it easy for LLMs (and agents) to interact with it. Ex: Google search.

This area shares commonalities with [OpenAI plugins](https://platform.openai.com/docs/plugins/introduction).

### Toolkit

Groups of tools that your agent can select from

Let's bring them all together:

```python

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import json

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

```python

serpapi_api_key='...'

```

```python

toolkit = load_tools(["serpapi"], llm=llm, serpapi_api_key=serpapi_api_key)

```

```python

agent = initialize_agent(toolkit, llm, agent="zero-shot-react-description", verbose=True, return_intermediate_steps=True)

```

```python

response = agent({"input":"what was the first album of the" 
                    "band that Natalie Bergman is a part of?"})

```

```

[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m I should try to find out what band Natalie Bergman is a part of.
Action: Search
Action Input: "Natalie Bergman band"[0m
Observation: [36;1m[1;3mNatalie Bergman is an American singer-songwriter. She is one half of the duo Wild Belle, along with her brother Elliot Bergman. Her debut solo album, Mercy, was released on Third Man Records on May 7, 2021. She is based in Los Angeles.[0m
Thought:[32;1m[1;3m I should search for the debut album of Wild Belle.
Action: Search
Action Input: "Wild Belle debut album"[0m
Observation: [36;1m[1;3mIsles[0m
Thought:[32;1m[1;3m I now know the final answer.
Final Answer: Isles is the debut album of Wild Belle, the band that Natalie Bergman is a part of.[0m

[1m> Finished chain.[0m

```

```python

print(json.dumps(response["intermediate_steps"], indent=2))

```

```

[
  [
    [
      "Search",
      "Natalie Bergman band",
      " I should try to find out what band Natalie Bergman is a part of.\nAction: Search\nAction Input: \"Natalie Bergman band\""
    ],
    "Natalie Bergman is an American singer-songwriter. She is one half of the duo Wild Belle, along with her brother Elliot Bergman. Her debut solo album, Mercy, was released on Third Man Records on May 7, 2021. She is based in Los Angeles."
  ],
  [
    [
      "Search",
      "Wild Belle debut album",
      " I should search for the debut album of Wild Belle.\nAction: Search\nAction Input: \"Wild Belle debut album\""
    ],
    "Isles"
  ]
]

```

![Wild Belle](data/WildBelle1.png)

🎵Enjoy🎵
https://open.spotify.com/track/1eREJIBdqeCcqNCB1pbz7w?si=c014293b63c7478c

```python



```