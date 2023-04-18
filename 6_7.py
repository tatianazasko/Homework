numbers = int(input())

even = 0
odd = 0

while numbers > 0:
    if numbers % 2 == 0:
        if numbers in even:
            print([even])
    else:
        if numbers in odd:
            print([odd])