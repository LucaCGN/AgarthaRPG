## Quickstart Guide
https://langchain.readthedocs.io/en/latest/getting_started/getting_started.html

```python

pip install langchain

```


```python

pip install openai

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


```python

conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

```


```python

conversation.predict(input="What was the first thing I said to you?")

```


```python

conversation.predict(input="what is an alternative phrase for the first thing I said to you?")

```

