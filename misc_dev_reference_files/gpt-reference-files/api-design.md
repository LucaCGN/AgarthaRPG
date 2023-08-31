## Part 1: General API Design and Backend Skeleton

### API Endpoints

1. **Interactible Stats Bar**
    - `GET /api/stats`: Retrieve the initial stats (D&D attributes).
    - `POST /api/stats`: Update the stats based on user input.

2. **Avatar Description User Text Input Box**
    - `GET /api/avatar/description`: Retrieve the initial or saved description.
    - `POST /api/avatar/description`: Update the avatar description.

3. **Character Final Description Text Box**
    - `GET /api/avatar/final-description`: Retrieve the AI-generated final description.

4. **Avatar Image Box**
    - `GET /api/avatar/image`: Retrieve the avatar image (possibly generated with DALL-E API).

5. **Professions Icons Selection Box**
    - `GET /api/professions`: Retrieve available professions.
    - `POST /api/professions`: Update the selected profession.

6. **Fighting Styles Icons Selection Box**
    - `GET /api/fighting-styles`: Retrieve available fighting styles.
    - `POST /api/fighting-styles`: Update the selected fighting style.

7. **Header Space for Quick Text for User Guide**
    - `GET /api/guide-text`: Retrieve quick guide text.

8. **"Roll Dice For Elements" Button**
    - `POST /api/roll-dice`: Perform dice roll for elements.

## Part 2: Mapping the Application Logic

### Data Flow

1. **Interactible Stats Bar**
    - Fetch data from `/api/stats`.
    - Display the stats in the UI.
    - Update the stats based on user interaction.
    - Save the updated stats to `/api/stats`.

2. **Avatar Description User Text Input Box**
    - Fetch initial description from `/api/avatar/description`.
    - Update the description based on user input.
    - Save the updated description to `/api/avatar/description`.

3. **Character Final Description Text Box**
    - Fetch the AI-generated description from `/api/avatar/final-description`.

4. **Avatar Image Box**
    - Fetch the avatar image from `/api/avatar/image`.

5. **Professions Icons Selection Box**
    - Fetch available professions from `/api/professions`.
    - Update the selected profession.
    - Save the selected profession to `/api/professions`.

6. **Fighting Styles Icons Selection Box**
    - Fetch available fighting styles from `/api/fighting-styles`.
    - Update the selected fighting style.
    - Save the selected fighting style to `/api/fighting-styles`.

7. **Header Space for Quick Text for User Guide**
    - Fetch quick guide text from `/api/guide-text`.

8. **"Roll Dice For Elements" Button**
    - User clicks the button to roll dice.
    - Call `/api/roll-dice` to get the result.
