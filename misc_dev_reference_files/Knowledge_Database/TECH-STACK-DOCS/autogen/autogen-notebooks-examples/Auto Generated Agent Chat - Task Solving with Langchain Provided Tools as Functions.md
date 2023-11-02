  

# Auto Generated Agent Chat - Task Solving with Langchain Provided Tools as Functions

  

AutoGen offers conversable agents powered by LLM, tool, or human, which can be used to perform tasks collectively via automated chat. This framework allows tool use and human participants through multi-agent conversation. Please find documentation about this feature [here](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat).

  

In this notebook, we demonstrate how to use `AssistantAgent` and `UserProxyAgent` to make function calls with the new feature of OpenAI models (in model version 0613) with a set of Langchain-provided tools and toolkits, to demonstrate how to leverage the 35+ tools available.

A specified prompt and function configs must be passed to `AssistantAgent` to initialize the agent. The corresponding functions must be passed to `UserProxyAgent`, which will execute any function calls made by `AssistantAgent`. Besides this requirement of matching descriptions with functions, we recommend checking the system message in the `AssistantAgent` to ensure the instructions align with the function call descriptions.

  

## Requirements

  

AutoGen requires `Python>=3.8`. To run this notebook example, please install the [mathchat] option since we will import functions from `MathUserProxyAgent`:

```bash

pip install "pyautogen[mathchat]"

```

```bash

%pip install Langchain

```

  
  

```python

%pip install "pyautogen[mathchat]~=0.1.0"

```

  

## Set your API Endpoint

  

The [`config_list_from_models`](https://microsoft.github.io/autogen/docs/reference/oai/openai_utils#config_list_from_models) function tries to create a list of configurations using Azure OpenAI endpoints and OpenAI endpoints for the provided list of models. It assumes the api keys and api bases are stored in the corresponding environment variables or local txt files:

  

- OpenAI API key: os.environ["OPENAI_API_KEY"] or `openai_api_key_file="key_openai.txt"`.

- Azure OpenAI API key: os.environ["AZURE_OPENAI_API_KEY"] or `aoai_api_key_file="key_aoai.txt"`. Multiple keys can be stored, one per line.

- Azure OpenAI API base: os.environ["AZURE_OPENAI_API_BASE"] or `aoai_api_base_file="base_aoai.txt"`. Multiple bases can be stored, one per line.

  

It's OK to have only the OpenAI API key, or only the Azure OpenAI API key + base.

If you open this notebook in google colab, you can upload your files by clicking the file icon on the left panel and then choosing "upload file" icon.

  

The following code excludes Azure OpenAI endpoints from the config list because some endpoints don't support functions yet. Remove the `exclude` argument if they do.

  
  

```python

import autogen

  

config_list = autogen.config_list_from_models(model_list=["gpt-4", "gpt-3.5-turbo", "gpt-3.5-turbo-16k"], exclude="aoai", openai_api_key_file="key_openai.txt")

  

```

  

## Making Function Calls

  

In this example, we demonstrate function call execution with `AssistantAgent` and `UserProxyAgent`. With the default system prompt of `AssistantAgent`, we allow the LLM assistant to perform tasks with code, and the `UserProxyAgent` would extract code blocks from the LLM response and execute them. With the new "function_call" feature, we define functions and specify the description of the function in the OpenAI config for the `AssistantAgent`. Then we register the functions in `UserProxyAgent`.

  
  
  

```python

%pip install Langchain

```

  
  

```python

# Import things that are needed generically

from langchain.pydantic_v1 import BaseModel, Field

from langchain.tools import BaseTool

from typing import Optional, Type

import math

  

class CircumferenceToolInput(BaseModel):

    radius: float = Field()

  

class CircumferenceTool(BaseTool):

    name = "circumference_calculator"

    description = "Use this tool when you need to calculate a circumference using the radius of a circle"

    args_schema: Type[BaseModel] = CircumferenceToolInput

  

    def _run(self, radius: float):

        return float(radius) * 2.0 * math.pi

```

  
  

```python

from langchain.tools.file_management.read import ReadFileTool

  

# Define a function to generate llm_config from a LangChain tool

def generate_llm_config(tool):

    # Define the function schema based on the tool's args_schema

    function_schema = {

        "name": tool.name.lower().replace (' ', '_'),

        "description": tool.description,

        "parameters": {

            "type": "object",

            "properties": {},

            "required": [],

        },

    }

  

    if tool.args is not None:

      function_schema["parameters"]["properties"] = tool.args

  

    return function_schema

  

# Instantiate the ReadFileTool

read_file_tool = ReadFileTool()

custom_tool = CircumferenceTool()

  

# Construct the llm_config

llm_config = {

  #Generate functions config for the Tool

  "functions":[

      generate_llm_config(custom_tool),

      generate_llm_config(read_file_tool),

  ],

  "config_list": config_list,  # Assuming you have this defined elsewhere

  "request_timeout": 120,

}

  

user_proxy = autogen.UserProxyAgent(

    name="user_proxy",

    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),

    human_input_mode="NEVER",

    max_consecutive_auto_reply=10,

    code_execution_config={"work_dir": "coding"},

)

  

# Register the tool and start the conversation

user_proxy.register_function(

    function_map={

        custom_tool.name: custom_tool._run,

        read_file_tool.name: read_file_tool._run,

    }

)

  

chatbot = autogen.AssistantAgent(

    name="chatbot",

    system_message="For coding tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done.",

    llm_config=llm_config,

)

  

user_proxy.initiate_chat(

    chatbot,

    message="Read the file with the path 'Test.txt', then calculate the circumference of a circle that has a radius of that files contents.", #" 7.81mm" in the file

    llm_config=llm_config,

)

```

  

# A PySpark Example

  
  

```python

%pip install pyspark

```

  
  

```python

#Starndard Langchain example

from langchain.agents import create_spark_sql_agent

from langchain.agents.agent_toolkits import SparkSQLToolkit

from langchain.chat_models import ChatOpenAI

from langchain.utilities.spark_sql import SparkSQL

from pyspark.sql import SparkSession

  

spark = SparkSession.builder.getOrCreate()

schema = "langchain_example"

spark.sql(f"CREATE DATABASE IF NOT EXISTS {schema}")

spark.sql(f"USE {schema}")

csv_file_path = "./sample_data/california_housing_train.csv"

table = "california_housing_train"

spark.read.csv(csv_file_path, header=True, inferSchema=True).write.option("path", "file:/content/spark-warehouse/langchain_example.db/california_housing_train").mode("overwrite").saveAsTable(table)

spark.table(table).show()

```

  
  

```python

# Note, you can also connect to Spark via Spark connect. For example:

# db = SparkSQL.from_uri("sc://localhost:15002", schema=schema)

spark_sql = SparkSQL(schema=schema)

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k")

toolkit = SparkSQLToolkit(db=spark_sql, llm=llm)

agent_executor = create_spark_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

```

  
  

```python

#Starndard Langchain example

agent_executor.run("Describe the california_housing_train table")

```

  
  

```python

# LangChain direct tool usage instead of toolkit example

# from langchain.tools.spark_sql.tool import (

#     InfoSparkSQLTool,

#     ListSparkSQLTool,

#     QueryCheckerTool,

#     QuerySparkSQLTool,

# )

# debug_toolkit = [

#   QuerySparkSQLTool(db=spark_sql),

#   InfoSparkSQLTool(db=spark_sql),

#   ListSparkSQLTool(db=spark_sql),

#   QueryCheckerTool(db=spark_sql, llm=llm),

#]

```

  
  

```python

  

# Now use AutoGen with Langchain Tool Bridgre

tools = []

function_map = {}

  

for tool in toolkit.get_tools(): #debug_toolkit if you want to use tools directly

    tool_schema = generate_llm_config(tool)

    print(tool_schema)

    tools.append(tool_schema)

    function_map[tool.name] = tool._run

  

# Construct the llm_config

llm_config = {

  "functions": tools,

  "config_list": config_list,  # Assuming you have this defined elsewhere

  "request_timeout": 120,

}

  

user_proxy = autogen.UserProxyAgent(

    name="user_proxy",

    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),

    human_input_mode="NEVER",

    max_consecutive_auto_reply=10,

    code_execution_config={"work_dir": "coding"},

)

  

print(function_map)

  

# Register the tool and start the conversation

user_proxy.register_function(

    function_map = function_map

)

  

chatbot = autogen.AssistantAgent(

    name="chatbot",

    system_message="For coding tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done.",

    llm_config=llm_config,

)

  

user_proxy.initiate_chat(

    chatbot,

    message="Describe the table names california_housing_train",

    llm_config=llm_config,

)

```