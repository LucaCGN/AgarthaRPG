🦜🔗 Langchain

## Introduction

The core idea of agents is to use an LLM to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

### Terminology:

- **AgentAction**: This is a dataclass that represents the action an agent should take. It has a `tool` property (which is the name of the tool that should be invoked) and a `tool_input` property (the input to that tool).
  
- **AgentFinish**: This is a dataclass that signifies that the agent has finished and should return to the user. It has a `return_values` parameter, which is a dictionary to return. It often only has one key - `output` - that is a string, and so often it is just this key that is returned.
  
- **intermediate_steps**: These represent previous agent actions and corresponding outputs that are passed around. These are important to pass to future iteration so the agent knows what work it has already done. This is typed as a `List[Tuple[AgentAction, Any]]`.

### Key Components:

- **Agent**: This is the chain responsible for deciding what step to take next. It is powered by a language model and a prompt. The inputs to this chain are: List of available tools, User input, Any previously executed steps (`intermediate_steps`). This chain then returns either the next action to take or the final response to send to the user (`AgentAction` or `AgentFinish`).

- **Tools**: Tools are functions that an agent calls. There are two important considerations here: Giving the agent access to the right tools and Describing the tools in a way that is most helpful to the agent.

- **Toolkits**: Often the set of tools an agent has access to is more important than a single tool. For this LangChain provides the concept of toolkits - groups of tools needed to accomplish specific objectives.

- **AgentExecutor**: The agent executor is the runtime for an agent. This is what actually calls the agent and executes the actions it chooses.

### Next Steps:

- Check out all the different agent types supported.
- Learn all the controls for AgentExecutor.
- See a full list of all the off-the-shelf toolkits provided.
- Explore all the individual tools supported.
