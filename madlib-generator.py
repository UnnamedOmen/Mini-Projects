with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

words = set() # holds unique words found in the story
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1] 
        words.add(word)   # adds found words to the word set()
        start_of_word = -1 # reset for next word search

answers = {}

for word in words:
    answer = input("Enter a " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)