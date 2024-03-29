import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list
allword = load_words()
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    if not word: return 0

    assert type(word) == str,       "type missing"
    assert word.islower(),f'{word} Not lowercase'
    assert len(word) > 0,       "word lenght must not be zero"
    assert type(n) == int,      "n not int"
    assert n >= 0,      "hand lenght must not be zero"
    score = len(word) * sum([SCRABBLE_LETTER_VALUES[letter] for letter in word])
    if len(word) == n:
        score += 50
    assert score >= 0,      "score is negative"
    return score
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    assert type(hand) == dict,      "Error type"
    assert len(hand) > 0,       "Hand must be more than zero"
    assert type(word) == str,       "Error type"
    assert len(word) > 0,       "Word must be more than zero"

    temp_hand = hand.copy()
    for letter in word:
            temp_hand[letter] -= 1
    assert type(temp_hand) == dict,      "Error type"
    return temp_hand
'''
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
letter = "quail"
print(update_hand(hand, letter))
'''
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    assert type(hand) == dict,      "Error type"
    assert len(hand) > 0,       "Hand must be more than zero"
    assert type(word) == str,       "Error type"
    assert len(word) > 0,       "Word must be more than zero"
    assert type(word_list) == list, "Error type"
    
    copy_hand = hand.copy()
    copy_word_list = word_list.copy()
    for letter in word:
        if letter not in hand:
            return False
        elif copy_hand[letter] > 0:
            copy_hand[letter] -= 1
        else:
            return False
        
    if word in copy_word_list:
        return True
    else:
        return False

'''
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
letter = "quail"
word_list = load_words()
print(is_valid_word(letter, hand, word_list))
'''

#
# Problem #4: Playing a hand
#

def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    assert type(hand) == dict,      "Error type"
    assert len(hand) > 0,       "Hand must be more than zero"
    return sum(hand.values())

'''
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
letter = "quail"
print(calculate_hand_len(hand))
'''

def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    # As long as there are still letters left in the hand:
    display_hand(hand)
    score = 0
    while calculate_hand_len(hand) > 0:     
        input_hand = input(f'Enter word, or a "." to indicate that you are finished: ')
        if input_hand == ".":
            print(f'Total scores: {score}')
            break
        elif is_valid_word(input_hand, hand, word_list) == False:
            print(f'{input_hand} Not in word_list')
            print(f'Total scores: {score}')
        else:
            score += get_word_score(input_hand, n)
            print(get_word_score(input_hand, n))
            print(f'Total scores: {score}')   
            hand = update_hand(hand, input_hand)
        display_hand(hand)
    return score
'''
n = 7
hand = deal_hand(n)
word_list = load_words()
play_hand(hand, word_list, n)
'''
#
# Problem #5: Playing a game
#

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand = {}
    last_hand = {}
    while True:
        check = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        assert type(check) == str, "check not a str"
        n = 7
        if check == "n":
            hand = deal_hand(n)
            last_hand = hand
        elif check == "r":
            if not last_hand:
                print("no reply hand from last game")
                continue
            else:
                hand = last_hand
        elif check == "e":
            return False
        play_hand(hand, word_list, n)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
