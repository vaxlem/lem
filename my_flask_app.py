# A simple password check
allowed_passwords = {5, 10, 3, 8, 4}  # Allowed passwords

def login():
    try:
        # Get user input
        password = int(input("Enter the password: "))
        
        # Check if the entered password is in the allowed passwords set
        if password in allowed_passwords:
            print("Access granted.")
            # Function to access the Google Drive document (pseudo code)
            access_google_drive_document()
        else:
            print("Access denied. Incorrect password.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def access_google_drive_document():
    # This function represents accessing a Google Drive document
    # Actual implementation would involve integrating Google Drive API
    print("Accessing document from Google Drive...")

# Run the login
login()
