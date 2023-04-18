def move(list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            list.append(list.pop(0))
    else:
        for i in range(steps):
            list.insert(0, list.pop())
            return


nums = list(map(int, input().split()))
N = int(input())
print(move(nums, N)) #на выводе проблема ((((

