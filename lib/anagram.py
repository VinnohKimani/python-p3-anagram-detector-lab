# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_original = sorted(self.word)
        result = []

        for word in word_list:
            if word.lower() == self.word:
                continue #skip a word if the word is already in the list
            if sorted(word.lower()) == sorted_original:
                result.append(word)
        return result
