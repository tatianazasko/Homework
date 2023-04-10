words = input('Введите фразу: ')
change = words.split()
text1 = '-'.join(change)
for element in set(text1):
    print("{} - {}".format(element, text1.count(element)))
