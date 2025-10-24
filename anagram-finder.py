import nltk
from nltk.corpus import words
from nltk.data import find
from itertools import permutations

def word_init():
    try:
        find('corpora/words.zip')
    except LookupError:
        try:
            find('corpora/words')
        except LookupError:
            nltk.download('words', quiet=True)


word_init()
ENGLISH_WORDS = set(w.lower() for w in words.words())


class Cryptic:
    """
    Find anagram words/phrases from a bag of letters split by group sizes
    """
    

    def __init__(self, input_letters, num_words):
        self.input_letters = input_letters
        self.num_words = list(num_words)
        self.english_words = ENGLISH_WORDS

        if sum(self.num_words) != len(self.input_letters):
            raise ValueError("Sum of num_words must equal the number of input letters.")     
    
    
    def is_word(self, word):
        """
        Validate a single word against the dictionary.
        """
        return word.isalpha() and word.lower() in self.english_words    
    
    def split_by_sizes(self, s):
        """
        Split a string s into chunks according to self.num_words.
        """
        parts = []
        i = 0
        for size in self.num_words:
            parts.append(s[i:i + size])
            i += size
        return parts


    def anagram_finder(self):
        """
        Return a list of possible words/phrases.
        For one chunk, returns ['WORD']; for multiple chunks, returns ['AAA BBB', ect].
        """
        results = []
        all_perms = permutations(self.input_letters, len(self.input_letters))

        if len(self.num_words) == 1:
            for combo in all_perms:
                s = ''.join(combo)
                if self.is_word(s):
                    results.append(s)
            return results

        for combo in all_perms:
            s = ''.join(combo)
            parts = self.split_by_sizes(s)

            if all(self.is_word(p) for p in parts):
                results.append(' '.join(parts))

        return results


def main():
    input_letters = 'needth'
    num_words = [3, 3]
    cryptic = Cryptic(input_letters, num_words)
    possible_words = cryptic.anagram_finder()

    if len(possible_words) > 0:
        print("POSSIBLE WORDS:")
        for w in possible_words:
            print(w)
    else:
        print("NO POSSIBLE WORDS FOUND")


if __name__ == "__main__":
    main()