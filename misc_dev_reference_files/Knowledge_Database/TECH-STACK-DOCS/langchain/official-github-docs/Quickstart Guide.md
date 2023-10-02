## Quickstart Guide
https://langchain.readthedocs.io/en/latest/getting_started/getting_started.html

```python

pip install langchain

```

```

Requirement already satisfied: langchain in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (0.0.75)
Requirement already satisfied: PyYAML<7,>=6 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (6.0)
Requirement already satisfied: dataclasses-json<0.6.0,>=0.5.7 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (0.5.7)
Requirement already satisfied: numpy<2,>=1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (1.21.5)
Requirement already satisfied: SQLAlchemy<2,>=1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (1.4.39)
Requirement already satisfied: pydantic<2,>=1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (1.10.4)
Requirement already satisfied: requests<3,>=2 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from langchain) (2.28.1)
Requirement already satisfied: marshmallow<4.0.0,>=3.3.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain) (3.19.0)
Requirement already satisfied: marshmallow-enum<2.0.0,>=1.5.1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain) (1.5.1)
Requirement already satisfied: typing-inspect>=0.4.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain) (0.8.0)
Requirement already satisfied: typing-extensions>=4.2.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from pydantic<2,>=1->langchain) (4.3.0)
Requirement already satisfied: certifi>=2017.4.17 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests<3,>=2->langchain) (2022.9.24)
Requirement already satisfied: charset-normalizer<3,>=2 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests<3,>=2->langchain) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests<3,>=2->langchain) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests<3,>=2->langchain) (1.26.11)
Requirement already satisfied: greenlet!=0.4.17 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from SQLAlchemy<2,>=1->langchain) (1.1.1)
Requirement already satisfied: packaging>=17.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from marshmallow<4.0.0,>=3.3.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (21.3)
Requirement already satisfied: mypy-extensions>=0.3.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from typing-inspect>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (0.4.3)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from packaging>=17.0->marshmallow<4.0.0,>=3.3.0->dataclasses-json<0.6.0,>=0.5.7->langchain) (3.0.9)
Note: you may need to restart the kernel to use updated packages.

```

```python

pip install openai

```

```

Requirement already satisfied: openai in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (0.26.3)
Requirement already satisfied: tqdm in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from openai) (4.64.1)
Requirement already satisfied: aiohttp in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from openai) (3.8.3)
Requirement already satisfied: requests>=2.20 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from openai) (2.28.1)
Requirement already satisfied: idna<4,>=2.5 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests>=2.20->openai) (3.3)
Requirement already satisfied: charset-normalizer<3,>=2 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests>=2.20->openai) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests>=2.20->openai) (2022.9.24)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from requests>=2.20->openai) (1.26.11)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (1.8.2)
Requirement already satisfied: attrs>=17.3.0 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (21.4.0)
Requirement already satisfied: frozenlist>=1.1.1 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (1.3.3)
Requirement already satisfied: aiosignal>=1.1.2 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (1.3.1)
Requirement already satisfied: multidict<7.0,>=4.5 in /Users/gregorykamradt/opt/anaconda3/lib/python3.9/site-packages (from aiohttp->openai) (6.0.4)
Note: you may need to restart the kernel to use updated packages.

```

```python

import os
# os.environ["OPENAI_API_KEY"] = ""

```

# Building A Language Model Application
### LLMS: Get predictions from a language model

```python

from langchain.llms import OpenAI

```

```python

llm = OpenAI(temperature=0.9)

```

```python

text = "What are 5 vacation destinations for someone who likes to eat pasta?"
print(llm(text))

```

```

1. Rome, Italy 
2. Bologna, Italy 
3. Venice, Italy
4. Amalfi Coast, Italy
5. Sicily, Italy

```

### Prompt Templates: Manage prompts for LLMs

```python

from langchain.prompts import PromptTemplate

```

```python

prompt = PromptTemplate(
    input_variables=["food"],
    template="What are 5 vacation destinations for someone who likes to eat {food}?",
)

```

```python

print(prompt.format(food="dessert"))

```

```

What are 5 vacation destinations for someone who likes to eat dessert?

```

```python

print(llm(prompt.format(food="dessert")))

```

```

1. New York City, USA
2. Tokyo, Japan
3. Paris, France
4. San Francisco, USA
5. Vancouver, Canada

```

### Chains: Combine LLMs and prompts in multi-step workflows

```python

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

```

```python

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["food"],
    template="What are 5 vacation destinations for someone who likes to eat {food}?",
)

```

```python

chain = LLMChain(llm=llm, prompt=prompt)

```

```python

print(chain.run("fruit"))

```

```

1. Costa Rica 
2. Hawaii 
3. Malaysia 
4. India 
5. Thailand

```

### Agents: Dynamically call chains based on user input

```python

pip install google-search-results

```

```python

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

```

```python

# Load the model
llm = OpenAI(temperature=0)

```

```python

# Load in some tools to use

# os.environ["SERPAPI_API_KEY"] = "..."

tools = load_tools(["serpapi", "llm-math"], llm=llm)

```

```python

# Finally, let's initialize an agent with:
# 1. The tools
# 2. The language model
# 3. The type of agent we want to use.

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

```

See list of agents types [here](https://python.langchain.com/docs/modules/agents/agent_types/)

```python

# Now let's test it out!
agent.run("Who is the current leader of Japan? What is the largest prime number that is smaller than their age?")

```

```

[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m I need to find out who the leader of Japan is and then calculate the largest prime number that is smaller than their age.
Action: Search
Action Input: "current leader of Japan"[0m
Observation: [36;1m[1;3mFumio Kishida[0m
Thought:[32;1m[1;3m I need to find out the age of the leader of Japan
Action: Search
Action Input: "age of Fumio Kishida"[0m
Observation: [36;1m[1;3m65 years[0m
Thought:[32;1m[1;3m I need to calculate the largest prime number that is smaller than 65
Action: Calculator
Action Input: 65[0m
Observation: [33;1m[1;3mAnswer: 65[0m
Thought:[32;1m[1;3m I now know the final answer
Final Answer: The current leader of Japan is Fumio Kishida and the largest prime number that is smaller than their age is 61.[0m

[1m> Finished chain.[0m

```

### Memory: Add state to chains and agents

```python

from langchain import OpenAI, ConversationChain

```

```python

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

```

```python

conversation.predict(input="Hi there!")

```

```

[1m> Entering new ConversationChain chain...[0m
Prompt after formatting:
[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi there!
AI:[0m

[1m> Finished chain.[0m

```

```python

conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

```

```

[1m> Entering new ConversationChain chain...[0m
Prompt after formatting:
[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi there!
AI:  Hi there! It's nice to meet you. How can I help you today?
Human: I'm doing well! Just having a conversation with an AI.
AI:[0m

[1m> Finished chain.[0m

```

```python

conversation.predict(input="What was the first thing I said to you?")

```

```

[1m> Entering new ConversationChain chain...[0m
Prompt after formatting:
[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi there!
AI:  Hi there! It's nice to meet you. How can I help you today?
Human: I'm doing well! Just having a conversation with an AI.
AI:  That's great! It's always nice to have a conversation with someone new. What would you like to talk about?
Human: What was the first thing I said to you?
AI:[0m

[1m> Finished chain.[0m

```

```python

conversation.predict(input="what is an alternative phrase for the first thing I said to you?")

```

```

[1m> Entering new ConversationChain chain...[0m
Prompt after formatting:
[32;1m[1;3mThe following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi there!
AI:  Hi there! It's nice to meet you. How can I help you today?
Human: I'm doing well! Just having a conversation with an AI.
AI:  That's great! It's always nice to have a conversation with someone new. What would you like to talk about?
Human: What was the first thing I said to you?
AI:  You said "Hi there!"
Human: what is an alternative phrase for the first thing I said to you?
AI:[0m

[1m> Finished chain.[0m

```

```python



```