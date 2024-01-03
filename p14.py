def pig_latin_word(sentence):
    new_sentence = sentence.split(" ")
    pig_latin_words = []
    for word in new_sentence:
        if word.isalpha():
            pig_latin_word = word[1:] + word[0].lower() + 'ay'
            pig_latin_words.append(pig_latin_word)
        else:
            pig_latin_words.append(word)
    pig_latin_sentence = ' '.join(pig_latin_words)
    return pig_latin_sentence

sentence = "Hello world"
print(pig_latin_word(sentence))
