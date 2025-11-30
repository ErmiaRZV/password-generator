from abc import ABC, abstractclassmethod
import string
import random
import nltk

nltk.download('words')

# Base abstract class for all password generators
class PasswordGenerator(ABC):
    @abstractclassmethod
    def generate_password(self):
        """Generates a password according to the specific generator logic"""
        pass

# Simple numeric PIN generator
class pinGenerator(PasswordGenerator):
    def __init__(self, length: int = 4):
        self.length = length
        self.characters = string.digits

    def generate_password(self):
        """Generate a numeric PIN of given length"""
        return "".join([random.choice(self.characters) for _ in range(self.length)])

# Random password generator with options for digits, symbols, and capitals
class randomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 4, include_digits: bool = False, include_symbols: bool = False, include_capitals: bool = False):
        self.length = length
        self.include_symbols = include_symbols
        self.include_digits = include_digits
        self.include_capitals = include_capitals
        self.character = string.ascii_lowercase
        if self.include_digits:
            self.character += string.digits
        if self.include_capitals:
            self.character += string.ascii_uppercase
        if self.include_symbols:
            self.character += string.punctuation

    def generate_password(self):
        """Generate a random password with selected character options"""
        return "".join([random.choice(self.character) for _ in range(self.length)])

# Memorable password generator using dictionary words
class memorablePasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 4, include_upper: bool = False, separator: str = "-"):
        self.length = length
        self.include_upper = include_upper
        self.character = nltk.corpus.words.words()  # List of English words
        self.separator = separator

    def generate_password(self):
        """Generate a memorable password by joining random words with separator"""
        password = [random.choice(self.character) for _ in range(self.length)]
        if self.include_upper:
            # Randomly capitalize some words
            password = [word.upper() if random.choice([True, False]) else word.lower() for word in password]
        return self.separator.join(password)

# Demo in CLI
def main():
    pin = pinGenerator()
    memorable = memorablePasswordGenerator()
    random_password = randomPasswordGenerator()

    print(f"Your PIN is: {pin.generate_password()}")
    print(f"Your Memorable Password is: {memorable.generate_password()}")
    print(f"Your Random Password is: {random_password.generate_password()}")

if __name__ == '__main__':
    main()
