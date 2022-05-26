
def find_anagram(word, anagram):
    word_list = list(word)
    anagram_list = list(anagram)
    if len(word_list)!= len(anagram_list):
        return False
    word = sorted(word)
    anagram = sorted(anagram)
    if word == anagram:
        return True

    else:
       return False

word = "night"
anagram = "thing"
print(find_anagram(word, anagram))

word = "act"
anagram = "ace"
print(find_anagram(word, anagram))

