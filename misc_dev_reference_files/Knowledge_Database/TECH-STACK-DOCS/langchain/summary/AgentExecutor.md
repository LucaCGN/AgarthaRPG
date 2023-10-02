🦜🔗 Langchain

## Overview

The `AgentExecutor` class is the main agent runtime supported by LangChain. However, there are other, more experimental runtimes we also support. These include: Plan-and-execute Agent, Baby AGI, Auto GPT.

### How it Works:

1. The agent executor is the runtime for an agent. This is what actually calls the agent and executes the actions it chooses.
2. Pseudocode for this runtime is:
   ```python
   next_action = agent.get_action(...)
   while next_action != AgentFinish:
       observation = run(next_action)
       next_action = agent.get_action(..., next_action, observation)
   return next_action```

While this may seem simple, there are several complexities this runtime handles for you, including:
- Handling cases where the agent selects a non-existent tool.
- Handling cases where the tool errors.
- Handling cases where the agent produces output that cannot be parsed into a tool invocation.
- Logging and observability at all levels (agent decisions, tool calls) either to stdout or LangSmith.

### Other Types of Agent Runtimes:

The `AgentExecutor` class is the main agent runtime supported by LangChain. However, there are other, more experimental runtimes we also support. These include:
- Plan-and-execute Agent
- Baby AGI
- Auto GPT

### Getting Started:

This section will guide you on how to get started building an agent. It covers the process of setting up the agent, defining custom tools, and running the agent in a custom loop. It also provides insights on how to add memory to the agent for enhanced functionality.

### Next Steps:

- Dive deeper into the different agent types supported.
- Explore the controls for `AgentExecutor`.
- Check out the list of off-the-shelf toolkits provided.
- Discover all the individual tools supported by LangChain.
