# LangChain-Powered RPG Chatbot Schema for AGARTHA.AI

## **1. User Input Processing**
- **Input**: User sends a message.
- **Validation**: Check if the input is a valid game action.

## **2. Decision Making (First Agent)**
- **Context Identification**: Determine the context of the user's message.
- **Action Implication**: Decide if the action implies a test or check.
- **Tool/Agent Selection**: Based on the context, select the necessary tools or agents to handle the action.

## **3. Game Mechanics Processing (Sub-Agents)**
### **3.1. Deception Check (Example)**
- **Identification**: Recognize the action as a deception.
- **Dice Roller Tool**: Roll a dice (e.g., d20) to determine the outcome.
- **LLM Processing**: Process the dice roll result and determine the NPC's reaction.
- **Memory Update**: If the NPC is significant, update the NPC's memory in Firestore.

### **3.2. Combat Mechanics**
- **Combat Initiation**: Determine if combat has started.
- **Combat Tools**: Use tools to handle combat actions, rolls, and outcomes.
- **Combat End**: Determine the end of combat and update game state.

### **3.3. Magic System**
- **Spell Identification**: Recognize if a user is casting a spell.
- **Spell Tools**: Handle spell effects, costs, and outcomes.
- **Spell End**: Update game state post-spell.

### **3.4. Setting Detailing & Consistency**
- **Setting Tools**: Ensure the game world remains consistent in its details.
- **World Update**: Update any changes to the game world in Firestore.

## **4. Output Generation**
- **LLM Processing**: Use LLM to generate a coherent and contextually relevant response.
- **Send Response**: Send the generated response back to the user.

## **5. Game State Management**
- **Firestore Integration**: Update game variables, content, chat modes, prompts, in-game time, etc., in Firestore.
- **Pinecone Integration**: Update and retrieve vectors related to game mechanics and NPC interactions.

## **6. Agent Tree System**
- **Performance vs. Cost**: Decide on the trade-off between performance and cost for the number of agents and levels in the tree system.
- **Agent Hierarchy**: Design a hierarchy of agents, where each agent can call upon sub-agents or tools based on the game context.

## **7. Memory Decision Agent**
- **Purpose**: Determines how to manage and utilize the chatbot's memory based on the context and the type of information.
- **Summarization Chain**: Every message in the dialogue between the user and player is summarized to focus on game actions.
- **Firestore Database Memory**: When information is fetched from Firestore, the agent analyzes and updates a fixed 4000-token game context box with relevant details.
- **Vector Database Memory (RAG)**: Fixed world contexts like city names, lore, and trade routes are loaded into the vector database and included by the first agent using RAG when deemed necessary.
- **Long-Term Specific Memory**: Users can alter the content in Firestore and fetch it as needed for detailed context.

## **8. Type of Memory**
- **Short-Term Memory**: Managed by the summarization chain and the 4000-token game context box. Focuses on recent interactions, NPC reactions, current quests, and recently used items.
- **Long-Term Fixed Memory**: Managed by the vector database. Contains static world information like city names, lore, and trade routes.
- **Long-Term Specific Memory**: Managed by Firestore. Users can alter and fetch this memory for specific, detailed context.

## **Technical & Practical Section (Based on Documentation)**

### **ChatOpenAI**
- **Initialization**: Initialize the ChatOpenAI model with the necessary parameters.
  ```python
  from langchain.chat_models.openai import ChatOpenAI
  chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")```
- **Sending Messages**: Use the `send_messages` method to process user input and get a response.
    ```python
    `response = chat_model.send_messages(messages=[{"role": "user", "content": "User message here"}])`
    ```

### **LLMChain**

- **Initialization**: Initialize the LLMChain with the required parameters.
    
    ``` python   
    `from langchain.chains.llm import LLMChain llm_chain = LLMChain(chat_model=chat_model, max_tokens=4000)`
    ```
    
- **Processing**: Use the `process` method to handle user input and generate a response using the LLM.
    
   ``` python
    
    `llm_response = llm_chain.process(user_input="User message here")`
    ```
