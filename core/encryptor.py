# core/encryptor.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class DataEncryptor:
    """
    AES-based symmetric encryption for local data privacy before proof generation.
    """

    def __init__(self, key: bytes | None = None):
        self.key = key or get_random_bytes(32)

    def encrypt(self, plaintext: str) -> str:
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, ciphertext_b64: str) -> str:
        data = base64.b64decode(ciphertext_b64)
        nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
