# Auto Generated Agent Chat - Performs Research with Multi-Agent Group Chat

  

AutoGen offers conversable agents powered by LLM, tool, or human, which can be used to perform tasks collectively via automated chat. This framework allows tool use and human participation through multi-agent conversation.

Please find documentation about this feature [here](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat).

  

## Requirements

  

AutoGen requires `Python>=3.8`. To run this notebook example, please install:

```bash

pip install pyautogen

```

  
  

```python

%%capture --no-stderr

# %pip install pyautogen~=0.1.0

```

  

## Set your API Endpoint

  

The [`config_list_from_json`](https://microsoft.github.io/autogen/docs/reference/oai/openai_utils#config_list_from_json) function loads a list of configurations from an environment variable or a json file.

  
  

```python

import autogen

  

config_list_gpt4 = autogen.config_list_from_json(

    "OAI_CONFIG_LIST",

    filter_dict={

        "model": ["gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],

    },

)

```

  

It first looks for environment variable "OAI_CONFIG_LIST" which needs to be a valid json string. If that variable is not found, it then looks for a json file named "OAI_CONFIG_LIST". It filters the configs by models (you can filter by other keys as well).

  

The config list looks like the following:

```python

config_list = [

    {

        'model': 'gpt-4-32k',

        'api_key': '<your OpenAI API key here>',

    },

    {

        'model': 'gpt-4-32k',

        'api_key': '<your Azure OpenAI API key here>',

        'api_base': '<your Azure OpenAI API base here>',

        'api_type': 'azure',

        'api_version': '2023-06-01-preview',

    },

    {

        'model': 'gpt-4-32k-0314',

        'api_key': '<your Azure OpenAI API key here>',

        'api_base': '<your Azure OpenAI API base here>',

        'api_type': 'azure',

        'api_version': '2023-06-01-preview',

    },

]

```

  

If you open this notebook in colab, you can upload your files by clicking the file icon on the left panel and then choosing "upload file" icon.

  

You can set the value of config_list in other ways you prefer, e.g., loading from a YAML file.

  

## Construct Agents

  
  

```python

gpt4_config = {

    "seed": 42,  # change the seed for different trials

    "temperature": 0,

    "config_list": config_list_gpt4,

    "request_timeout": 120,

}

user_proxy = autogen.UserProxyAgent(

   name="Admin",

   system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",

   code_execution_config=False,

)

engineer = autogen.AssistantAgent(

    name="Engineer",

    llm_config=gpt4_config,

    system_message='''Engineer. You follow an approved plan. You write python/shell code to solve tasks. Wrap the code in a code block that specifies the script type. The user can't modify your code. So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor.

Don't include multiple code blocks in one response. Do not ask others to copy and paste the result. Check the execution result returned by the executor.

If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.

''',

)

scientist = autogen.AssistantAgent(

    name="Scientist",

    llm_config=gpt4_config,

    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their abstracts printed. You don't write code."""

)

planner = autogen.AssistantAgent(

    name="Planner",

    system_message='''Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.

The plan may involve an engineer who can write code and a scientist who doesn't write code.

Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.

''',

    llm_config=gpt4_config,

)

executor = autogen.UserProxyAgent(

    name="Executor",

    system_message="Executor. Execute the code written by the engineer and report the result.",

    human_input_mode="NEVER",

    code_execution_config={"last_n_messages": 3, "work_dir": "paper"},

)

critic = autogen.AssistantAgent(

    name="Critic",

    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the plan includes adding verifiable info such as source URL.",

    llm_config=gpt4_config,

)

groupchat = autogen.GroupChat(agents=[user_proxy, engineer, scientist, planner, executor, critic], messages=[], max_round=50)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

```

  

## Start Chat

  
  

```python

user_proxy.initiate_chat(

    manager,

    message="""

find papers on LLM applications from arxiv in the last week, create a markdown table of different domains.

""",

)

```

  

## Create Group Chat without Critic for Comparison

  
  

```python

groupchat_nocritic = autogen.GroupChat(agents=[user_proxy, engineer, scientist, planner, executor], messages=[], max_round=50)

for agent in groupchat.agents:

    agent.reset()

manager_nocritic = autogen.GroupChatManager(groupchat=groupchat_nocritic, llm_config=gpt4_config)

user_proxy.initiate_chat(

    manager_nocritic,

    message="""

find papers on LLM applications from arxiv in the last week, create a markdown table of different domains.

""",

)

```