# Scrabble challenge
#
# A script that takes a Scrabble rack as a command-line argument and prints all
# valid Scrabble words that can be constructed from that rack, along with their
# Scrabble scores, sorted by score.  Rack letters are checked against SOWPODS
# word list in 'sowpods.txt' file.

import sys

# Dictionary containing all letters and their Scrabble values
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

# Function to see if word can be buit from letters in rack
def InRack( word, rack ):
    wordlist = list(word)
    wordComp = list(word)
    racklist = list(rack)
    score = 0

    # Go through all the letters in the word
    for letter in wordlist:
        # Compare each letter with the one in the rack
        for tile in racklist:
            if letter == tile:
                racklist.remove(tile)
                wordComp.remove(letter)
                score = score + scores[letter.lower()]
                # print "Letter found:", letter, wordComp, racklist, score
                break
        else:
            continue

    if len(wordComp) == 0:
        return score
    else:
        return 0

# Check commandline for the correct arguments
if (len(sys.argv) == 2):
    rack = str(sys.argv[1])
    print 'Letters to be played:', rack.lower()

    sowpods = open('sowpods.txt', 'r')

    for word in sowpods:
        word = word.rstrip('\n\r') 
        wordScore = InRack(word, rack)
        if wordScore > 0:
            print wordScore, word 
            #scoreDict[wordScore] = word
        
else:
    print 'scrabble.py letters'
