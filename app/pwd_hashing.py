import bcrypt

# Password to hash
password = "pwd1234#9876"

# Generate salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

# Convert hashed password to a string for SQL insertion
hashed_password_str = hashed_password.decode()

print(hashed_password_str)
