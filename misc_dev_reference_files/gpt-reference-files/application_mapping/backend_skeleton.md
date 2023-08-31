# Agartha RPG Back-End Skeleton

## Folder Structure

Agartha/
|-- app/
|   |-- __init__.py
|   |-- routes.py
|   |-- models.py
|   |-- services/
|   |   |-- account_service.py 
|   |   |-- encryption_service.py
|   |   |-- character_management_service.py
|   |   |-- profession_service.py
|   |   |-- weapon_service.py
|   |   |-- stats_service.py
|   |   |-- element_service.py
|   |   |-- avatar_service.py
|   |   |-- chat_service.py
|   |   |-- skill_tree_service.py
|   |   |-- character_detail_service.py
|   |   |-- dice_log_service.py
|   |   |-- ai_chat_service/
|   |       |-- langchain/
|   |           |-- memory_handling/
|   |               |-- buffermemory.py
|   |               |-- bufferwindowmemory.py
|   |               |-- summarymemory.py
|   |               |-- tokenmanagement.py
|   |       |-- prompts/
|   |           |-- character_prompts.py
|   |           |-- chat_ui_prompts.py
|   |           |-- elemental_prompts.py
|   |           |-- elements_desc.txt
|   |           |-- initial_prompt.txt
|   |           |-- profession_prompts.py
|   |-- utilities/
|   |   |-- validations.py
|   |   |-- helpers.py
|   |-- game_data/
|       |-- current_game_state.json
|       |-- game_save.json
|       |-- character_info.json
|       |-- campaign.md
|       |-- lore.md
|       |-- command_output/
|       |-- command_output/
|           |-- ach/
|               |-- current_achievements.json
|               |-- future_achievements.json
|               |-- past_achievements.log
|               |-- sample_achievements.json
|           |-- ali/
|               |-- current_allies.json
|               |-- fixed_allies.json
|               |-- future_allies.json
|               |-- past_allies.log
|           |-- cam/
|               |-- current_events.json
|               |-- fixed_events.json
|               |-- future_events.json
|               |-- past_events.log
|           |-- env/
|               |-- current_environment.json
|               |-- fixed_environment.json
|               |-- future_environments.json
|               |-- past_environments.log
|           |-- itens/
|               |-- current_items.json
|               |-- future_items.json
|               |-- past_items.log
|               |-- sample_items.json
|           |-- lor/
|               |-- current_lore.md
|               |-- fixed_lore.md
|           |-- mag/
|               |-- current_spells.json
|               |-- future_spells.json
|               |-- past_spells.log
|               |-- sample_spells.json
|           |-- music/
|               |-- fixed_music.json
|           |-- opo/
|               |-- current_opponents.json
|               |-- fixed_opponents.json
|               |-- future_opponents.json
|               |-- past_opponents.log
|           |-- puz/
|               |-- current_puzzles.md
|               |-- future_puzzles.md
|               |-- past_puzzles.log
|               |-- sample_puzzles.md
|           |-- sav/
|               |-- current_save.json
|           |-- ski/
|               |-- current_skills.json
|               |-- future_skills.json
|               |-- past_skills.log
|               |-- sample_skills.json
|           |-- tes/
|               |-- current_tests.md
|               |-- future_tests.md
|               |-- past_tests.log
|               |-- sample_tests.md
|           |-- tra/
|               |-- future_trades.json
|               |-- past_trades.log
|               |-- sample_trades.json
|-- database/
|   |-- mysql_config.json
|   |-- qdrant_config.json
|-- static/
|   |-- css/
|   |-- images/
|   |-- js/
|-- templates/
|   |-- index.html
|   |-- login.html
|   |-- create_or_continue.html
|   |-- landing_page.html
|   |-- profession_selection.html
|   |-- weapon_selection.html
|   |-- stats_distribution.html
|   |-- roll_for_elements.html
|   |-- choose_element.html
|   |-- final_description.html
|   |-- chat_ui.html
|-- config.py
|-- app.py
|-- tests/
|-- requirements.txt
|-- README.md
|-- wsgi.py


|   |-- services/
|   |   |-- account_service.py  (Updated)
|   |   |    |-- login_user(username, password): Authenticates the user and initiates a new session.
|   |   |    |-- register_user(user_details): Registers a new user and saves their details to the database.
|   |   |    |-- send_verification_email(email): Sends an email verification link to the user's email.
|   |   |    |-- verify_email(token): Verifies the user's email using a token.
|   |   |    |-- send_password_reset_email(email): Sends a password reset link to the user's email.
|   |   |    |-- reset_password(token, new_password): Resets the user's password using a token.
|   |   |
|   |   |-- encryption_service.py  (New)
|   |   |    |-- encrypt_password_sha(password): Encrypts the password using the SHA algorithm and returns the hashed password.
|   |   |
|   |   |-- character_management_service.py
|   |   |    |-- get_existing_characters(user_id): Fetches existing characters for a user.
|   |   |    |-- create_new_character(character_details): Creates a new character for the user.
|   |   |
|   |   |-- profession_service.py
|   |   |    |-- get_all_professions(): Fetches all available professions.
|   |   |    |-- save_selected_profession(user_id, profession_id): Saves the selected profession for the user.
|   |   |
|   |   |-- weapon_service.py
|   |   |    |-- get_all_weapons(): Fetches all available weapons.
|   |   |    |-- save_selected_weapons(user_id, weapon_ids): Saves the selected weapons for the user.
|   |   |
|   |   |-- stats_service.py
|   |   |    |-- get_initial_or_saved_stats(user_id): Fetches the initial or saved stats for the user.
|   |   |    |-- save_distributed_stats(user_id, stats): Saves the distributed stats for the user.
|   |   |
|   |   |-- element_service.py
|   |   |    |-- roll_for_elements(): Executes a roll to determine available elements.
|   |   |    |-- save_selected_element(user_id, element_id): Saves the selected element for the user.
|   |   |
|   |   |-- avatar_service.py
|   |   |    |-- generate_avatar(user_details): Generates an avatar for the user using DALL-E.
|   |   |    |-- get_avatar(user_id): Fetches the generated avatar for the user.
|   |   |
|   |   |-- chat_service.py
|   |   |    |-- get_initial_message(): Fetches the initial chat message from MASTER-AI.
|   |   |    |-- save_and_fetch_next_message(user_id, user_input): Saves the user's response and fetches the next message from MASTER-AI.
|   |   |
|   |   |-- skill_tree_service.py
|   |   |    |-- get_profession_skill_tree(profession_id): Fetches the skill tree for the selected profession.
|   |   |    |-- get_elemental_skill_tree(element_id): Fetches the skill tree for the selected element.
|   |   |
|   |   |-- character_detail_service.py
|   |   |    |-- get_character_details(user_id): Fetches detailed information about the character, such as inventory and stats.
|   |   |
|   |   |-- dice_log_service.py
|   |   |    |-- log_dice_action(action_details): Logs a dice-related action.
|   |   |    |-- get_dice_log(user_id): Fetches the log of all dice-related actions for the user.



## Services Overview
- **Account Service (`account_service.py`)**:
  - Methods to handle user authentication and registration.
  
- **Character Management Service (`character_management_service.py`)**:
  - Methods to manage existing characters and create new ones.

- **Profession Service (`profession_service.py`)**
  - Methods to fetch all professions and their details.
  - Methods to save the selected profession.

- **Weapon Service (`weapon_service.py`)**
  - Methods to fetch all weapons and their details.
  - Methods to save the selected weapons.

- **Stats Service (`stats_service.py`)**
  - Methods to fetch and save character stats.
  - Methods to validate stat distribution.

- **Element Service (`element_service.py`)**
  - Methods to execute dice rolls for elements.
  - Methods to fetch available elements based on the roll.
  - Methods to save the selected element.

- **Avatar Service (`avatar_service.py`)**
  - Methods to generate and fetch DALL-E avatars.

- **Chat Service (`chat_service.py`)**
  - Methods to manage chat interaction, including fetching initial messages and saving user responses.

- **Skill Tree Service (`skill_tree_service.py`)**
  - Methods to fetch skill trees for both profession and elements.

- **Character Detail Service (`character_detail_service.py`)**
  - Methods to fetch and manage character details like inventory, stats, and more.

- **Dice Log Service (`dice_log_service.py`)**
  - Methods to log and fetch all dice-related actions.
