import unittest
from LanguageLearningApp import LanguageLearningApp, UserProfile

class TestLanguageLearningApp(unittest.TestCase):
    def setUp(self):
        self.app = LanguageLearningApp()
        self.app.add_word("apple", "pomme")
        self.app.add_word("banana", "banane")
        self.app.create_user_profile("user1")

    def test_add_word(self):
        self.app.add_word("orange", "orange")
        self.assertTrue("orange" in self.app.vocab)

    def test_remove_word(self):
        self.assertTrue(self.app.remove_word("apple"))
        self.assertFalse("apple" in self.app.vocab)

    def test_select_random_word(self):
        word, translation = self.app.select_random_word()
        self.assertTrue(word in self.app.vocab)
        self.assertTrue(translation in self.app.vocab.values())

    def test_check_translation(self):
        self.app.select_random_word()
        self.app.current_translation = "pomme"
        self.assertTrue(self.app.check_translation("pomme"))
        self.assertFalse(self.app.check_translation("orange"))

    def test_save_and_load_vocab(self):
        filename = "test_vocab.json"
        self.app.save_vocab(filename)
        self.app.load_vocab(filename)
        self.assertEqual(self.app.vocab, {"apple": "pomme", "banana": "banane"})

    def test_start_quiz(self):
        self.app.start_quiz()
        self.assertEqual(self.app.score, 0)
        self.assertEqual(self.app.total_questions, 0)

    def test_create_user_profile(self):
        self.assertTrue(self.app.get_user_profile())
        self.assertEqual(self.app.get_user_profile().username, "user1")

    def test_update_vocab_progress(self):
        self.app.get_user_profile().update_vocab_progress("apple", True)
        self.assertEqual(self.app.get_user_profile().vocab_progress["apple"], [1, 1])

    def test_get_vocab_progress(self):
        self.app.get_user_profile().update_vocab_progress("apple", True)
        self.assertEqual(self.app.get_user_profile().get_vocab_progress("apple"), 100)

    def test_save_and_load_user_profile(self):
        self.app.get_user_profile().update_vocab_progress("apple", True)
        filename = "test_profile.json"
        self.app.save_user_profile(filename)
        self.app.load_user_profile(filename)
        self.assertEqual(self.app.get_user_profile().username, "user1")
        self.assertEqual(self.app.get_user_profile().vocab_progress["apple"], [1, 1])

if __name__ == '__main__':
    unittest.main()
