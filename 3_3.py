name = str(input('Введите ваше имя:'))
age = int(input('Введите ваш возраст:'))
city = str(input( 'Введите ваш город:'))
print(f"Здравствуйте, {name} (возраст:{age}, город:{city})")
print("Здравствуйте, {} (возраст:{}, город:{})".format(name, age, city))
print("Здравствуйте, {name} (возраст:{age}, город:{city})".format(name=name, age=age, city=city))

#я старалась избегать слова лет/год в возрасте т.к. не зналю как это записать в код
