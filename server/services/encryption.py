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
#FERNET_KEY = Fernet.generate_key()
FERNET_KEY = b"o1AeL2cLS2n8eVYxVZxOMXsVPpKUAYCZit7f8vMEgUs="  # <-- Must be static
cipher = Fernet(FERNET_KEY)
def encrypt_data(data: bytes) -> bytes:
    """
    Encrypts raw data using the global cipher instance.

    This function takes a plaintext byte sequence and applies the configured
    cipher’s encryption method, returning the resulting ciphertext.

    Parameters
    ----------
    data : bytes
        The plaintext data to be encrypted.

    Returns
    -------
    bytes
        The encrypted ciphertext.
    """
    return cipher.encrypt(data)


def decrypt_data(encrypted: bytes) -> bytes:
    """
    Decrypts ciphertext back into its original byte form using the global cipher.

    This function takes an encrypted byte sequence produced by the cipher and
    applies the decryption method to recover the original plaintext.

    Parameters
    ----------
    encrypted : bytes
        The ciphertext data to be decrypted.

    Returns
    -------
    bytes
        The decrypted plaintext bytes.
    """
    return cipher.decrypt(encrypted)

