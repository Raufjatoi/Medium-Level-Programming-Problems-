# 6. Simple Text Analyzer:
#  Write a program that reads a string from the user and analyzes it.
#  Calculate and display the number of characters, words, and sentences in the string.
sentence = input('Enter sentence : ')
print(f'characters = {len(sentence)}')
print(f'characters without space = {len(sentence.replace(' ',''))}')
print(f'words = {len(sentence.split(' '))}')
print(f'sentence = {len(sentence.split(",","."))}')
      