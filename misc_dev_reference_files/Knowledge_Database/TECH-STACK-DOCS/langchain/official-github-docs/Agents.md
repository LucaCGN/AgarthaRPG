# Agents - Make OpenAI Do Things For you

*[Source](https://langchain.readthedocs.io/en/latest/modules/agents/getting_started.html)*
* **Agent** - Agents use an LLM to determine which actions to take and in what order. An action can either be using a tool and observing its output, or returning to the user.

Parameters when creating an agent:
* **Tool:** A function that performs a specific duty. This can be things like: Google Search, Database lookup, Python REPL, other chains. The interface for a tool is currently a function that is expected to have a string as an input, with a string as an output.
* **LLM:** The language model powering the agent.
* **Agent:** The agent to use. This should be a string that references a support agent class. Because this notebook focuses on the simplest, highest level API, this only covers using the standard supported agents. If you want to implement a custom agent, see the documentation for custom agents (coming soon).

```python

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

```

### List of Tools
1. **python_repl -** A Python shell. Use this to execute python commands. Input should be a valid python command. If you expect output it should be printed out.
2. **serpapi [Complete] -** A search engine. Useful for when you need to answer questions about current events. Input should be a search query.
3. **wolfram-alpha [Complete] -** A wolfram alpha search engine. Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Input should be a search query.
4. **requests -** A portal to the internet. Use this when you need to get specific content from a site. Input should be a specific url, and the output will be all the text on that page.
5. **terminal -** Executes commands in a terminal. Input should be valid commands, and the output will be any output from running that command.
6. **pal-math -** A language model that is excellent at solving complex word math problems. Input should be a fully worded hard word math problem.
7. **pal-colored-objects -** A language model that is wonderful at reasoning about position and the color attributes of objects. Input should be a fully worded hard reasoning problem. Make sure to include all information about the objects AND the final question you want to answer.
8. **llm-math -** Useful for when you need to answer questions about math.
9. **open-meteo-api -** Useful for when you want to get weather information from the OpenMeteo API. The input should be a question in natural language that this API can answer.
10. **news-api -** Use this when you want to get information about the top headlines of current news stories. The input should be a question in natural language that this API can answer.
11. **tmdb-api -** Useful for when you want to get information from The Movie Database. The input should be a question in natural language that this API can answer.
12. **google-search -** A wrapper around Google Search. Useful for when you need to answer questions about current events. Input should be a search query.


### 2. SERP API

```python

from langchain.agents import load_tools

# import os
# os.environ['OPENAI_API_KEY'] = "..."
# os.environ['SERPAPI_API_KEY'] = "..."

```

```python

llm = OpenAI(temperature=0)

```

```python

tool_names = ["serpapi"]
tools = load_tools(tool_names)

```

```python

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

```

```python

agent.run("What is LangChain?")

```

```python

# Input should be a search query.
agent.run("who is the ceo of pipe?")

```

### 3. Wolfram Alpha

```python

from langchain.agents import load_tools

# import os
# pip install wolframalpha
# os.environ['OPENAI_API_KEY'] = "..."
# os.environ['WOLFRAM_ALPHA_APPID'] = ".."

```

```python

llm = OpenAI(temperature=0)

```

```python

tool_names = ["wolfram-alpha"]
tools = load_tools(tool_names)

```

```python

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

```

```python

# Input should be a search query.

agent.run("What is the asthenosphere?")

```

```python



```