import sys
import json

if __name__ == '__main__':
    words = open('words.txt', 'r').read()
    words_list = words.split('\n')

    search = sys.argv[1]

    looking = []

    for word in words_list:
        found = True
        lowered_word = word.lower()
        for c in lowered_word:
            if c not in search or lowered_word.count(c) > search.count(c):
                found = False

        if found:
            looking.append(lowered_word)

    sorted = {}
    for word in looking:
        sorted.setdefault(str(len(word)), []).append(word.lower())

    print json.dumps(sorted, indent=4, sort_keys=True)
