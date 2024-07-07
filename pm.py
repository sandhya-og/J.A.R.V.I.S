import json
import os
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, filename='passwords.json', key_file='key.key'):
        self.filename = filename
        self.key_file = key_file

        # Generate or load encryption key
        if not os.path.exists(self.key_file):
            self.key = Fernet.generate_key()
            with open(self.key_file, 'wb') as kf:
                kf.write(self.key)
        else:
            with open(self.key_file, 'rb') as kf:
                self.key = kf.read()

        self.cipher = Fernet(self.key)

        # Load or create the password file
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}
            self.save_data()

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_password(self, platform, username, password):
        encrypted_password = self.cipher.encrypt(password.encode()).decode()
        self.data[platform] = {'username': username, 'password': encrypted_password}
        self.save_data()

    def get_password(self, platform):
        if platform in self.data:
            encrypted_password = self.data[platform]['password']
            password = self.cipher.decrypt(encrypted_password.encode()).decode()
            return self.data[platform]['username'], password
        else:
            print(f"No credentials found for {platform}")
            return None, None
