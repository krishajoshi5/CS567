import random
import json
import os

class LanguageLearningApp:
    def __init__(self):
        self.vocab = {}
        self.score = 0
        self.total_questions = 0
        self.current_word = None
        self.current_translation = None
        self.user_profile = None

    def add_word(self, word, translation):
        self.vocab[word] = translation

    def remove_word(self, word):
        if word in self.vocab:
            del self.vocab[word]
            return True
        else:
            return False

    def select_random_word(self):
        if self.vocab:
            word, translation = random.choice(list(self.vocab.items()))
            self.current_word = word
            self.current_translation = translation
            return word, translation
        else:
            return None, None

    def check_translation(self, translation):
        self.total_questions += 1
        if translation == self.current_translation:
            self.score += 1
            return True
        else:
            return False

    def save_vocab(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.vocab, f)

    def load_vocab(self, filename):
        with open(filename, 'r') as f:
            self.vocab = json.load(f)

    def get_score(self):
        return self.score

    def get_progress(self):
        if self.total_questions == 0:
            return 0
        else:
            return (self.score / self.total_questions) * 100

    def start_quiz(self):
        self.score = 0
        self.total_questions = 0

    def create_user_profile(self, username):
        self.user_profile = UserProfile(username)

    def save_user_profile(self, filename):
        if self.user_profile:
            self.user_profile.save(filename)

    def load_user_profile(self, filename):
        self.user_profile = UserProfile.load(filename)

    def get_user_profile(self):
        return self.user_profile


class UserProfile:
    def __init__(self, username):
        self.username = username
        self.vocab_progress = {}

    def update_vocab_progress(self, word, correct):
        if word in self.vocab_progress:
            self.vocab_progress[word][0] += 1
            if correct:
                self.vocab_progress[word][1] += 1
        else:
            self.vocab_progress[word] = [1, int(correct)]

    def get_vocab_progress(self, word):
        if word in self.vocab_progress:
            return self.vocab_progress[word][1] / self.vocab_progress[word][0] * 100
        else:
            return 0

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump({"username": self.username, "vocab_progress": self.vocab_progress}, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            user_profile = cls(data["username"])
            user_profile.vocab_progress = data["vocab_progress"]
            return user_profile


if __name__ == "__main__":
    app = LanguageLearningApp()
    app.add_word("apple", "pomme")
    app.add_word("banana", "banane")
    app.create_user_profile("user1")
    app.get_user_profile().update_vocab_progress("apple", True)
    app.save_user_profile("user1_profile.json")
