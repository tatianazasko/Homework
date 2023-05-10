import csv
with open('users.csv', 'w', newline='') as file:
    fieldnames = ['first_name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Nastya', 'age': 31})
    writer.writerow({'first_name': 'Nastya', 'age': 31})
    writer.writerow({'first_name': 'Petya', 'age': 32})