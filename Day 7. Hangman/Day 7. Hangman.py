import random
import os
clear = lambda: os.system('cls')
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]
print(logo)
used_letters = []
lives = 6
end_of_game = False
chosen_word = random.choice(word_list)
#print(f'Pssst, the solution is {chosen_word}.')
display = []
for c in range(len(chosen_word)):
    display.append("_")
while not end_of_game:
    guess = input("Guess a letter \n").lower()
    #clear()
    if guess in used_letters:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:

        for position in range(len(chosen_word)):

            if chosen_word[position] == guess:
                display[position] = guess

    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print(f"You lose. The word was {chosen_word}")
    used_letters += guess
    print(f"{' '.join(display)}")
    print(stages[lives])