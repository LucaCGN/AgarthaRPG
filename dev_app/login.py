import warnings

# Suppress Firestore UserWarning
warnings.filterwarnings("ignore", category=UserWarning)

def login_user(db):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Query Firestore to find a user document that matches the entered email
    users_ref = db.collection('user')
    query_ref = users_ref.where('email', '==', email)
    
    users = query_ref.stream()
    
    user_found = False
    for user in users:
        user_data = user.to_dict()
        if user_data.get('password') == password:
            user_found = True
            print(f"Logged in as {user.id}")
            return user.id  # Save this user ID for future use in the application
    
    if not user_found:
        print("Debug: No users found.")
    
    print("Invalid email or password.")
    return None
