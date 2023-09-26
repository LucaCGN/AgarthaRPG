# Game Application Documentation with Langchain Integration

## Table of Contents
1. [Application Flow](#application-flow)
2. [Base Chat Logic](#base-chat-logic)
3. [Prompt Chaining Logic](#prompt-chaining-logic)
4. [Resource Modules](#resource-modules)
5. [Infrastructure Modules](#infrastructure-modules)
6. [User Experience](#user-experience)
7. [Engine Summary](#engine-summary)
8. [API Interactions](#api-interactions)
9. [Agent-based Decision Making](#agent-based-decision-making)
10. [Application Engine Demonstration](#application-engine-demonstration)
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
- **API Interactions**: Manages the interaction with external APIs for fetching real-world data or other services.
  - **Langchain Component**: Use Langchain's `API Chain` for this module. **(New)**
  
- **Agent-based Decision Making**: Manages complex decision-making processes in the game.
  - **Langchain Component**: Use Langchain's `Agents` for this module. **(New)**

---

## User Experience
Detailed steps from user login to quest completion, including character creation and elemental affinity determination, are outlined in the original document.

---

## Engine Summary
- **Agent-based Decision Making**: How the agent decides which tool to use based on the context.
  - **Langchain Component**: Use Langchain's `Agents` for this part. **(New)**

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

USER EXPERIENCE:
block0:
1. Log In
block1: 
2. Choose Character Name
3. Choose Character Profession
4. Choose Character Weapons
5. Roll 4d6, droplowets, 6 times for all 6 Value stat
6. Print the user the avaiable values, and ask the player stat by stat which value to assign to it.
7. Give context that player is just made 18 and ask him to describe their character personality and phisical characteristics.
block2.
8. Inniate game with initial prompt of player waking up and giving game context.
9. Set player goals in the scenario, inspect with his 2 bags and 2 weapons
10.Player should interact as he want, minnimally or extensevly with the scenario, until he complete the block objectives 
block3:
11. Once the player leaves the house, we set the two objectives by giving the player context: 1. he needs go to the village but before that 2. he need to perform his daily training routine, which will serve as combat tutorial.
12. The relevant NPCs will be training between the player and the city, that makes the engagement with the tutorial unavoidable
13. Player will be presented to all his weapons actions and will be given the chance to perform to combat actions in the training dummy to get a feel of the system.
block4:
14. Today is the day you, your childhood friend and your mentor are going to the city for both of you to perform the elemental affinity ritual. Being ready to depart in 3 hours is the next objective
15. The player is free to interact however he wants with the village within his 3 hour window, which will give the sense of freedom that is the goal of the game.
16. Once the LLM, which will be keeping track of the passage of time through each iteration with the user, infers that 3 hours have passed, if the player is not on the pier yet, Novak will appear and scold you, if you resist, he will just get furious and bring you by force.
block5:
17. Goal again is time based. Travel is supposed to take 3 hours but will only last 1h, in this 1h, you can interact with the NPCs as to bond with them or to learn more about the world.
18. In the 1 hour limit, a highlevel elemental beast atacks and we get our only cutscene like part of the tutorial, where the mentor NPC propels the ship towards the shore while performing some strange magic on both you and your childhood friend, you crash on the shore and faint.
block6:
19. Player wake up, feels something weird with his body, trys to remember what happened and in this moment:
20. interrupt game flow to run for element affinity
21. craft your initial abilitys based on your character choices and how you desire to use your element
22. "in this moment", the players pc has a mental visualiztion of his element and how he can use it
23. Before he can process it, he looks at the childhood NPC which appears to be experiencing the same thing, and before both of you can say a world, you hear two children scream from what appears to be a small cave entrance 30ft from you both.
24. Your friend speeds towards the cave, and you, still completely confused, follows her inside.
block6:
25. As we change blocks, the objective here switchs to complete the dungeon! The user will be introduce to many mechanics, the dungeon general mechanics, the combat mechanics and the alignment mechanic.
26. The player navigates through the dungeon, one of the paths with a trap and estaer like chamber with a treasure.
27. Be it by staying and prioritizing the treasure or by how the PC saves or not the children, define character alignment
28. Battle and defeat the wolf
29. Depending on the outcome, faint or finish cave exploration before exiting it.