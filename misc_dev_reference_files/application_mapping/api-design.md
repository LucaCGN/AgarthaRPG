# Agartha RPG API Design

## Email Verification and Password Reset

- `POST` /api/email-verification: Send a verification email to the user after registration.
- `POST` /api/verify-email: Verify the user's email using the token sent via email.
- `POST` /api/request-password-reset: Issue a password reset email to the user.
- `POST` /api/reset-password: Reset the user's password using the token sent via email.

## Login and Registration Page

- `POST` /api/login: Authenticate the user and start a new session.
- `POST` /api/register: Register a new user and save their initial details.

## Character Management Page

- `GET` /api/character-management: Fetch existing characters (if any).
- `POST` /api/create-new-character: Start a new character creation process.
- `POST` /api/continue-adventure: Continue with an existing character.

## Landing Page

- `GET` /api/landing-page: Fetch the welcome message for the landing page.

## Profession Selection Page

- `GET` /api/professions: Fetch all professions, their corresponding icons, and status attributes.
- `POST` /api/professions/select: Save the selected profession for the user.
- `GET` /api/professions/description: Fetch the description of the selected profession.

## Weapons Selection Page

- `GET` /api/weapons: Fetch all available weapons, their corresponding icons, and status attributes.
- `POST` /api/weapons/select: Save the selected weapons for the user.
- `GET` /api/weapons/description: Fetch the description of the selected weapons.

## Stats Distribution Page

- `GET` /api/stats: Fetch initial or saved stats for the user along with available points.
- `POST` /api/stats: Save the distributed points across various stats.
- `POST` /api/character-description: Save the user's description of the character, which includes gender, hair, facial details, body details, and character name.

## Roll for Elements Page

- `POST` /api/roll-for-elements: Execute a roll to determine which elements are available for selection.

## Choose Element Page

- `GET` /api/available-elements: Fetch elements that are available based on the roll.
- `POST` /api/choose-element: Save the chosen element for the user.

## Avatar & Final Description Page

- `GET` /api/avatar-image: Fetch the DALL-E generated avatar image for the character.
- `GET` /api/final-description: Fetch the final description generated for the character based on previous selections.

## Game Interaction API Endpoints

### Chat UI

- `GET` /api/chat/initial-message: Fetch the initial game message from MASTER-AI.
- `POST` /api/chat/user-response: Save the user's chat response and fetch the next message from MASTER-AI.

### Left Lateral Menu

- `GET` /api/skill-tree/profession: Fetch the skill tree for the chosen profession.
- `GET` /api/skill-tree/elemental: Fetch the skill tree for the chosen elemental magic.
- `GET` /api/character-details: Fetch details like inventory, stats, and more about the character.
- `GET` /api/world-map: Fetch the current world map and user location.

### Right Lateral Menu (Dice Log)

- `GET` /api/dice-log: Fetch a log of all dice-related actions that happened in the game.
