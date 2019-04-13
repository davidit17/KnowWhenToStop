import random


def random_gen(low, high):
    while True:
        yield random.randrange(low, high)


def printlist(lst):
    for num in lst:
        print (num)


n = 4
gen = random_gen(1, 10*n)
end = 1
lst = []
act = 0
strtMsg = "\npress 1 to get new number or 0 to choose the current number "


for i in range(1, n+1):
    number = next(gen)
    lst.append(number)
    if end:
        printlist(lst)
        print("\nYour number is ", lst[i-1])
        act = (int(input(strtMsg)))
        if act:
            continue
        if act == 0:
            choise = number
            end = 0

if end:
    choise = number


print("\nAll Numbers : \n")
printlist(lst)
print("\nyour number : ", choise)
print("max number : ", max(lst))
