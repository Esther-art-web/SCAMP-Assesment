def fib(num):
    if num >= 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            add = (fib(num - 2) + fib(num - 1))
            return add
    else:
        return None


num = int(input("Enter a number: "))
print("The fibonacci sequence of", num, ":")
for i in range(num + 1):
    seq = []
    seq.append(fib(i))
    for a in seq:
        print(a, end=",")
