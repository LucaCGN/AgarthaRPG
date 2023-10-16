import warnings

# Suppress Firestore UserWarning
warnings.filterwarnings("ignore", category=UserWarning)

def login_user(db, email, password, ui):
    # Validate inputs
    if not email or not password:
        ui.display_message("Email and password cannot be empty.")
        return None
    
    try:
        # Query Firestore to find a user document that matches the entered email
        users_ref = db.collection('user')
        query_ref = users_ref.where('email', '==', email)
        
        users = query_ref.stream()
        
        user_found = False
        for user in users:
            user_data = user.to_dict()
            if user_data.get('password') == password:
                user_found = True
                ui.display_message(f"Logged in as {user.id}")
                return user.id  # Save this user ID for future use in the application
        
        if not user_found:
            ui.display_message("Debug: No users found.")
        
        ui.display_message("Invalid email or password.")
        return None
    except Exception as e:
        ui.display_message(f"An error occurred: {e}")
        return None
