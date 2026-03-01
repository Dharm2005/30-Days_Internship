# Task 5: Word Frequency Counter

sentence = "data science is fun and data science is powerful"

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(word, ":", count)
