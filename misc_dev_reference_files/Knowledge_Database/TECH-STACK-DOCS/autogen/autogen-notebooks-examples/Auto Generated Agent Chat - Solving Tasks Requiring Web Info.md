  
  

# Auto Generated Agent Chat: Solving Tasks Requiring Web Info

  

AutoGen offers conversable agents powered by LLM, tool, or human, which can be used to perform tasks collectively via automated chat. This framework allows tool use and human participation through multi-agent conversation.

Please find documentation about this feature [here](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat).

  

In this notebook, we demonstrate how to use `AssistantAgent` and `UserProxyAgent` to perform tasks which require acquiring info from the web:

* discuss a paper based on its URL.

* discuss about the stock market.

  

Here `AssistantAgent` is an LLM-based agent that can write Python code (in a Python coding block) for a user to execute for a given task. `UserProxyAgent` is an agent which serves as a proxy for a user to execute the code written by `AssistantAgent`. By setting `human_input_mode` properly, the `UserProxyAgent` can also prompt the user for feedback to `AssistantAgent`. For example, when `human_input_mode` is set to "TERMINATE", the `UserProxyAgent` will execute the code written by `AssistantAgent` directly and return the execution results (success or failure and corresponding outputs) to `AssistantAgent`, and prompt the user for feedback when the task is finished. When user feedback is provided, the `UserProxyAgent` will directly pass the feedback to `AssistantAgent`.

  

## Requirements

  

AutoGen requires `Python>=3.8`. To run this notebook example, please install pyautogen and docker:

```bash

pip install pyautogen docker

```

  
  

```python

# %pip install pyautogen~=0.1.0 docker

```

  

## Set your API Endpoint

  


## Construct Agents

  

We construct the assistant agent and the user proxy agent. We specify `human_input_mode` as "TERMINATE" in the user proxy agent, which will ask for human feedback when it receives a "TERMINATE" signal from the assistant agent.

  
  

```python

# create an AssistantAgent instance named "assistant"

assistant = autogen.AssistantAgent(

    name="assistant",

    llm_config=llm_config,

)

# create a UserProxyAgent instance named "user_proxy"

user_proxy = autogen.UserProxyAgent(

    name="user_proxy",

    human_input_mode="TERMINATE",

    max_consecutive_auto_reply=10,

    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),

    code_execution_config={"work_dir": "web"},

    llm_config=llm_config,

    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.

Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""

)

```

  

## Example Task: Paper Talk from URL

  

We invoke the `initiate_chat()` method of the user proxy agent to start the conversation. When you run the cell below, you will be prompted to provide feedback after the assistant agent sends a "TERMINATE" signal at the end of the message. If you don't provide any feedback (by pressing Enter directly), the conversation will finish. Before the "TERMINATE" signal, the user proxy agent will try to execute the code suggested by the assistant agent on behalf of the user.

  
  

```python

# the assistant receives a message from the user, which contains the task description

user_proxy.initiate_chat(

    assistant,

    message="""

Who should read this paper: https://arxiv.org/abs/2308.08155

""",

)

```

  

## Example Task: Chat about Stock Market

  
  

```python

user_proxy.initiate_chat(

    assistant,

    message="""Show me the YTD gain of 10 largest technology companies as of today.""",

)

```