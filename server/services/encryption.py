from cryptography.fernet import Fernet

# NOTE:
# This key is hardcoded for development and testing purposes only.
# In production or any environment where sensitive data is handled,
# this key should be stored securely using environment variables
# or a secrets manager. For example:
#   - Use python-dotenv to load from a `.env` file (keep it out of version control)
#   - Use Docker secrets or an external vault (e.g., AWS Secrets Manager)
#
# We're keeping it inline temporarily to simplify testing directly
# from the GitHub repo without requiring extra setup steps.
FERNET_KEY = Fernet.generate_key()
cipher = Fernet(FERNET_KEY)

def encrypt_data(data: bytes) -> bytes:
    return cipher.encrypt(data)

def decrypt_data(encrypted: bytes) -> bytes:
    return cipher.decrypt(encrypted)
