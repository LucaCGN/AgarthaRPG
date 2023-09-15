RPG_Game_Database
│
├── user (Collection)
│   ├── user1 (Document)
│   │   ├── user_account_data (Fields)
│   │   │   ├── email
│   │   │   ├── password
│   │   │   ├── premium_status
│   │   │   ├── payment_option
│   │   │   ├── google_auth_enabled
│   │   │   └── character_id (Array of references to character_details)
│   │   │
│   │   └── game_data (Sub-Collection)
│   │       ├── character1 (Document)
│   │       │   ├── character_details (Fields)
│   │       │   │   ├── UserID
│   │       │   │   ├── Name
│   │       │   │   ├── Description
│   │       │   │   ├── Titles (Array)
│   │       │   │   ├── Level
│   │       │   │   ├── Stats (Map)
│   │       │   │   ├── Profession
│   │       │   │   ├── Weapon1
│   │       │   │   ├── Weapon2
│   │       │   │   ├── Element1
│   │       │   │   ├── Element2
│   │       │   │   ├── Element3
│   │       │   │   ├── LifeLevel_Current
│   │       │   │   ├── LifeLevel_Max
│   │       │   │   ├── ManaLevel_Current
│   │       │   │   └── ManaLevel_Max
│   │       │   │
│   │       │   ├── inventory (Sub-Collection)
│   │       │   │   └── item1 (Document)
│   │       │   │       └── item_details (Fields)
│   │       │   ├── skills (Sub-Collection)
│   │       │   │   └── skill1 (Document)
│   │       │   │       └── skill_details (Fields)
│   │       │   ├── actions (Sub-Collection)
│   │       │   │   └── action1 (Document)
│   │       │   │       └── action_details (Fields)
│   │       │   ├── allys (Sub-Collection)
│   │       │   │   └── ally1 (Document)
│   │       │   │       └── ally_details (Fields)
│   │       │   ├── enemys (Sub-Collection)
│   │       │   │   └── enemy1 (Document)
│   │       │   │       └── enemy_details (Fields)
│   │       │   ├── achievements (Sub-Collection)
│   │       │   │   └── achievement1 (Document)
│   │       │   │       └── achievement_details (Fields)
│   │       │   ├── quests (Sub-Collection)
│   │       │   │   └── quest1 (Document)
│   │       │   │       └── quest_details (Fields)
│   │       │   ├── setting (Sub-Collection)
│   │       │   │   └── setting1 (Document)
│   │       │   │       └── setting_details (Fields)
│   │       │   ├── factions (Sub-Collection)
│   │       │   │   └── faction1 (Document)
│   │       │   │       └── faction_details (Fields)
│   │       │   ├── worldviews-changing-events (Sub-Collection)
│   │       │   │   └── event1 (Document)
│   │       │   │       └── event_details (Fields)
│   │       │   ├── trades (Sub-Collection)
│   │       │   │   └── trade1 (Document)
│   │       │   │       └── trade_details (Fields)
│   │       │   └── chat_log (Sub-Collection)
│   │       │       └── chat_session1 (Document)
│   │       │           └── chat_session_details (Fields)
│   │       │               ├── sender
│   │       │               ├── message
│   │       │               └── timestamp
│   │       │
│   │       └── ... (Other characters)
│   │
│   └── user2 (Document)
│       └── ...
│
├── fixed_game_data (Collection)
│   ├── initial_game_state (Document)
│   │   └── initial_state_details (Fields)
│   │
│   ├── professions_system (Sub-Collection)
│   │   ├── Miner (Document)
│   │   │   └── profession_details (Fields)
│   │   ├── Taylor (Document)
│   │   │   └── profession_details (Fields)
│   │   └── ... (Other professions)
│   │
│   ├── elements_system (Sub-Collection)
│   │   ├── Ice (Document)
│   │   │   └── element_details (Fields)
│   │   ├── Electricity (Document)
│   │   │   └── element_details (Fields)
│   │   └── ... (Other elements)
│   │
│   ├── weapons_system (Sub-Collection)
│   │   ├── Axe (Document)
│   │   │   └── weapon_details (Fields)
│   │   ├── Bone_Spear (Document)
│   │   │   └── weapon_details (Fields)
│   │   └── ... (Other weapons)
│   │
│   ├── setting (Sub-Collection)
│   │   ├── Forest (Document)
│   │   │   └── setting_details (Fields)
│   │   ├── Desert (Document)
│   │   │   └── setting_details (Fields)
│   │   └── ... (Other settings)
│   │
│   ├── campaign (Sub-Collection)
│   │   ├── Campaign1 (Document)
│   │   │   └── campaign_details (Fields)
│   │   ├── Campaign2 (Document)
│   │   │   └── campaign_details (Fields)
│   │   └── ... (Other campaigns)
│   │
│   ├── items (Sub-Collection)
│   │   ├── Item1 (Document)
│   │   │   └── item_details (Fields)
│   │   ├── Item2 (Document)
│   │   │   └── item_details (Fields)
│   │   └── ... (Other items)
│   │
│   ├── factions (Sub-Collection)
│   │   ├── Faction1 (Document)
│   │   │   └── faction_details (Fields)
│   │   ├── Faction2 (Document)
│   │   │   └── faction_details (Fields)
│   │   └── ... (Other factions)
│   │
│   ├── worldviews-changing-events (Sub-Collection)
│   │   ├── Event1 (Document)
│   │   │   └── event_details (Fields)
│   │   ├── Event2 (Document)
│   │   │   └── event_details (Fields)
│   │   └── ... (Other events)
│   │
│   ├── quests (Sub-Collection)
│   │   ├── Quest1 (Document)
│   │   │   └── quest_details (Fields)
│   │   ├── Quest2 (Document)
│   │   │   └── quest_details (Fields)
│   │   └── ... (Other quests)
│   │
│
└── llm_backend (Collection)
    └── prompts (Sub-Collection)