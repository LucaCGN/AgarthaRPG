# Agartha RPG Front-End Architecture

## 1- Index Page

### Components:

1. **Header Text**: "Welcome to Agartha, the next-gen AI-powered chat-based RPG"
2. **Login Button & Form**: Swichts the visible form to the Login Form.
3. **Register Button & Form**: Swichts the visible form to the  Registration Form.
4. **Forgot Password Link**: Navigates to the Password Reset Page.
5. **Register Button**: Submits the registration form.
2. **Login Button**: Submits the login form.

### Behavior:

- Login Fields:  + Forgot Password Link
- Registration Fields: Full Name, Birthday, email, password and confirm password
- Successful login navigates to 'Create New Character or Continue Adventure' screen.
- Forgot Password Link navigates to the Password Reset Page.
- Register button submits the form and triggers an email verification process.
---

*As it clear above, the first page is a dynamic page which can lead to 3 different pages, the email verfication page, the password reset page and the character creation/continue adventure page*

## 2- Email Verification Page

### Components:

2. **Verification Code Field**: To enter the code received via email.
3. **Verify Button**: Submits the verification code.

### Behavior:

- Verify Button validates the code and if correct, navigates to 'Create New Character or Continue Adventure' screen.

---

## 3- Password Reset Page 1

### Components:

1. **Email Field**: To enter the email for password reset.
2. **Send Reset Link Button**: Sends a password reset link to the email.
3. **Back to Login Link**: Navigates back to the Login Page.

### Behavior:

- Send Reset Link Button sends an email with the reset link and navigates to a confirmation screen.
- Back to Login Link navigates back to the Login Page.

---


## 4- Password Reset Page 2 - (confirmation screen)

### Components:

1. **new passordd Field**: To enter the new password.
2. **confirm password field**:  To confirm the new password.
3. **Confirm change**: To confirm the changes

### Behavior:

- Choose new password and confirm it
- Confirm the update of the users pw

---

## Create New Character or Continue Adventure Page

### Components:

1. **Create New Character Button**: Starts new character creation flow.
2. **Continue Adventure Button**: Skips to chat UI for existing characters.

### Behavior:

- 'Create New Character' button navigates to the Creation Page
- 'Continue Adventure' button navigates to the Chat UI page for users with existing characters.

---

## 1- Begin Creation Page

### Components:

1. **Header Text**: "Begin your journey in Agartha"
2. **Action Button**: 'Begin Character Creation'

### Behavior:

- Clicking the action button navigates the user to the Profession Selection Page.

---

## 2- Profession Selection Page

### Components:

1. **Header Text**: "In Agartha, your role and backstory is defined by your profession choice"
2. **Icon Grid**: 25 round selectable icons representing professions.
3. **Description Box**: Blank area for updating profession description.
4. **Next Button**: Button to proceed.

### Behavior:

- Clicking an icon updates the Description Box.
- Clicking the Next Button saves the selection and navigates to Weapons Selection Page.

---

## 3- Weapons Selection Page

### Components:

1. **Header Text**: Explanation of weapons selection.
2. **Icon Grid**: 25 round selectable icons for weapons.
3. **Description Boxes**: Two boxes for weapon descriptions.
4. **Next and Back Buttons**: To navigate between pages.

### Behavior:

- Clicking an icon updates the respective Description Box.
- Both Next and Back Buttons save the current state and navigate accordingly.

---

## 4- Stats Distribution Page

### Components:

1. **Header Text**: Dynamic text based on user choices.
2. **Stats UI**: Interactive UI for stats distribution.
3. **Character Description Input**: Text box with sub-inputs for gender, hair, facial details, body details, and name.
4. **Next and Back Buttons**: To navigate between pages.
5. **Confirmation Button**: Appears after clicking Next, warning the user that they can't go back after this point.

### Behavior:

- Stats UI updates in real-time.
- All inputs are saved upon navigation.

---

## 5- Roll for Elements Page

### Components:

1. **Header Text**: Explanation text.
2. **Roll Button**: Button to roll for elements.
3. **Roll Animation**: An animation to represent the roll.

### Behavior:

- Clicking the Roll Button triggers the animation and determines available elements.

---

## 6- Choose Element Page

### Components:

1. **Header Text**: "Choose your element"
2. **Element Icons**: Selectable icons for elements.
3. **Next Button**: Button to proceed.

### Behavior:

- Clicking an icon selects the element.
- Next Button saves the selection.

---

## 7- Character Avatar & Final Description Page

### Components:

1. **Avatar**: Generated avatar image.
2. **Final Description**: Text based on user choices.
3. **Begin Adventure Button**: To start the game.

### Behavior:

- Clicking "Begin Adventure" navigates to the chat UI and starts the game.

---

## Game UI

### Components:

1. **Left Lateral Menu**: Links to Profession Skill Tree, Elemental Magic Skill Tree, Character Details, World Map.
2. **Chat UI**: Main game interaction.
3. **Right Lateral Menu**: Roll20 style log for dice actions.

### Behavior:

- Left and Right Menus can be collapsed and overlaid on chat in mobile view.
- Additional functionalities, like DALL-E images for impactful moments, can be integrated above the Chat UI.

