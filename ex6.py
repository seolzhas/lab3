def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

user_input = input("Enter a sentence: ")

reversed_sentence = reverse_sentence(user_input)

print("Reversed sentence:", reversed_sentence)
