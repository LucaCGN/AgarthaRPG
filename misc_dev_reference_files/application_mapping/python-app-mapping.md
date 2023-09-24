# Game Application Documentation with Langchain Integration

## Table of Contents
1. [Application Flow](#application-flow)
2. [Base Chat Logic](#base-chat-logic)
3. [Prompt Chaining Logic](#prompt-chaining-logic)
4. [Resource Modules](#resource-modules)
5. [Infrastructure Modules](#infrastructure-modules)
6. [User Experience](#user-experience)
7. [Engine Summary](#engine-summary)
8. [Application Engine Demonstration](#application-engine-demonstration)

---

## Application Flow

### Blocks
Each block represents a distinct phase or quest in the game, starting from user login to completing specific quests.

#### `block0`: **Login on Firestore**
- Authenticates the user and initializes their session.
- **Langchain Component**: Use Langchain's `Retrieval` module to fetch user data from Firestore.

#### `block1`: **Create New Character**
- Allows the user to create and customize their game character.
- **Langchain Component**: Utilize Langchain's `Memory` module to persist character data.

#### `block2`: **Act0-Quest1-Hut**
- The first quest, focused on familiarizing the player with their immediate surroundings.
- **Langchain Component**: Use Langchain's `Chains` to construct sequences of calls for quest logic.

#### `block3`: **Act0-Quest2-Beach**
- Introduces combat mechanics and NPC interactions.
- **Langchain Component**: Use Langchain's `Agents` to manage NPC interactions.

#### `block4`: **Act0-Quest3-Village**
- Expands the game world and introduces time-based objectives.
- **Langchain Component**: Utilize Langchain's `Memory` module to track time-based objectives.

#### `block5`: **Act0-Quest4-Boat**
- Adds more complexity with NPC interactions and a surprise event.
- **Langchain Component**: Use Langchain's `Chains` for complex quest logic.

#### `block6`: **Element Affinity Roll**
- Determines the player's elemental affinity, affecting their abilities.
- **Langchain Component**: Use Langchain's `Model I/O` to interface with the LLM for affinity determination.

#### `block7`: **Act0-Quest5-Cave**
- A dungeon quest that introduces multiple game mechanics.
- **Langchain Component**: Use Langchain's `Agents` and `Chains` for dungeon mechanics.

---

## Base Chat Logic
1. **Initial Context to LLM**: Sets the stage for the Language Logic Model (LLM), providing it with the necessary background to generate appropriate responses.
   - **Langchain Component**: Use Langchain's `Model I/O` to set the initial context for the LLM.

2. **Fixed GameMaster Messages**: The first set of GameMaster messages are predetermined to set the tone and context.
   - **Langchain Component**: Use Langchain's `Memory` module to store these fixed messages.

3. **Initial Conversation Context**: Establishes the basic setting, characters, and objectives for the player.
   - **Langchain Component**: Use Langchain's `Memory` and `Model I/O` modules to manage conversation context.

4. **Prompt Chaining Mechanics**: Mechanism to link multiple prompts together for a cohesive narrative.
   - **Langchain Component**: Use Langchain's `Chains` to construct sequences of calls for prompt chaining.

5. **Module Interaction**: Allows the LLM to interact with various game modules like dice rolling, inventory management, etc.
   - **Langchain Component**: Use Langchain's `Agents` to manage module interactions.


---

## Prompt Chaining Logic
This section outlines how different quests are linked together to form a continuous narrative.

- **Act0-Quest1-Hut**: The player starts in a hut, and the objective is to explore and interact with objects.
  
- **Act0-Quest2-Beach**: The player moves to a beach setting, where they encounter NPCs and engage in combat.
  
- **Act0-Quest3-Village**: The player explores a village, interacts with multiple NPCs, and has time-based objectives.
  
- **Act0-Quest4-Boat**: A boat journey with NPCs that ends in an unexpected event.
  
- **Act0-Quest5-Cave**: A dungeon-crawling quest with traps, treasures, and combat.

---

## Resource Modules
These modules provide various utilities and functionalities needed during gameplay.

- **Dice Rolling**: Simulates dice rolls for various game events.
  
- **Read Commands Collection**: A set of commands that the LLM can use to fetch data from the database.
  
- **Write Commands Collection**: Commands for updating the database, like saving game state.
  
- **Summarize System Output**: Condenses lengthy system messages for easier consumption by the player.

---

## Infrastructure Modules
These modules handle the backend logic and data management.

- **Memory Context Management**: Manages the game state and player choices.
  
- **Manual and Lore Simple Chat Bot**: Provides lore and manual information upon player request.
  
- **Character/Inventory Management**: Manages player's character stats, inventory, and other persistent data.

---

## User Experience
Detailed steps from user login to quest completion, including character creation and elemental affinity determination, are outlined in the original document.

---

## Engine Summary

### Components
- **System Input**: Initial data and settings loaded into the game engine.
  
- **User Input**: Commands and choices made by the player.
  
- **User Message Processing**: How the LLM processes and interprets user input.
  
- **Decision Flow**: The logic tree that decides how to respond to user input, including database queries and direct responses.
  
- **Update System Variables**: Updates game state variables based on player actions.
  
- **Manage Context**: Keeps track of the narrative and game state to provide coherent responses.
  
- **Answer User**: The final output message that the LLM generates in response to user input.

---

## Application Engine Demonstration with Quest1
This section provides a step-by-step walkthrough of how the engine handles the first quest, from initial context setting to user interaction and system output.

### Steps
- **Initial Quest Context System Output**: Sets the narrative stage for the quest.
  
- **User Input**: Captures what action the player decides to take.
  
- **LLM Initial Context**: Provides the LLM with all the necessary background information.
  
- **LLM Prompt for User Message Processing**: Detailed logic for how the LLM processes user input to generate appropriate responses.

