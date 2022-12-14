from nltk.corpus import words

# List of English Words
englWords = words.words()

# Variables
haveLetters = False
haveMustUse = False
letters = []
listOWords = []
dictOWords = {}

# Collect letters from user, make sure letters are valid.
while not haveLetters:
    letters = input("Available letters: ").lower()
    if not letters.isalpha():
        print(f"Please only use letters, {letters} is not a valid set of letters.")
    else:
        haveLetters = True

# Collect must use letter from user, make sure letter is in provided letters
while not haveMustUse:
    mustUse = input("Letter that must be used in each word: ").lower()
    if len(mustUse) == 1:
        if mustUse in letters:
            haveMustUse = True
        else:
            print(f"Must be one of these letters: {letters}")
    else:
        print("Can only have 1 must use letter.")

# Run through each word in englWords, if word is too short or it does not contain must use letter, skip it
# Check if word only contains the letters available
for word in englWords:
    if len(word) < 4 or mustUse not in word:
        continue
    elif set(letters).issuperset(word):
        listOWords.append(word)

# Alphabetize and check if any words contain all provided letters
listOWords.sort()
for word in listOWords:
    containsAllLetters = True
    for letter in letters:
        if letter in word:
            continue
        else:
            containsAllLetters = False
    if containsAllLetters:
        listOWords.remove(word)
        listOWords.insert(0, f"*{word}*")

# Separate words into a dictionary by length
for word in listOWords:
    lengthOWord = len(word)
    if "*" in word:
        lengthOWord -= 2
    if lengthOWord in dictOWords:
        dictOWords[lengthOWord].append(word)
    else:
        dictOWords[lengthOWord] = [word]


# Output words to a text file
with open("Text File of Words.txt", "w") as output:
    output.write(f"Available letters : {letters}\n")
    output.write(f"Must use letter : {mustUse}\n")
    output.write("*Words that use all of the letters*\n")
    for key in sorted(dictOWords):
        output.write(str(f"All possible {key} letter words:\n"))
        output.write(str(dictOWords[key]))
        output.write(str("\n"))
output.close()