print('Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его
# с аналогом на своём языке.
#
# Программа получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# 
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

text = input('Введите текст: ')
text_length = len(text)

counter_1 = 0
counter_2 = 0

for i in range(text_length):
  if text[i] != ' ':
    counter_1 += 1
    if i != text_length:
      counter_2 = counter_1
  elif (counter_2 == 0) or (counter_2 < counter_1):
    counter_2 = counter_1
    counter_1 = 0
  else:
    counter_1 = 0

print('Длина самого длинного слова:', counter_2)
