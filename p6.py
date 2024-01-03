sentence = "mgo"

sentence = sentence.lower()
letter_counts = {}
for char in sentence:
    if char.isalpha():
        letter_counts[char] = sentence.count(char)

max_count = max(letter_counts, key=letter_counts.get)
print(max_count)