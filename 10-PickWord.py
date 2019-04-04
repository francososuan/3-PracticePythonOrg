import random

words = []

with open("sowpods.txt","r") as f:
    line = f.readline()
    words.append(line)

    while line:
        line = f.readline().strip("\n")
        words.append(line)

random_index = random.randint(0, len(words)-1)

print("Random word: ", words[random_index])