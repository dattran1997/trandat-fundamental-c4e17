letter_counts = {}
word = input("enter a word: ")

for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts)
letterItems = list(letter_counts.items())
print(letterItems)
letterItems.sort()
for index in letterItems:
    print(*index,sep ="  ")
