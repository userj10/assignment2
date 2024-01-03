vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

sentence = "Hello World"

vowel_count = 0
consonant_count = 0

for n in sentence:
    if n.isalpha():
        if n in vowels:
            vowel_count += 1
        elif n in consonants:
            consonant_count += 1
print(f"Given sentence contains {vowel_count} vowels and {consonant_count} consonants")