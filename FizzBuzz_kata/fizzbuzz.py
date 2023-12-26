def fizzbuzz(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    result = ""
    if num % 3 == 0:
        result += "fizz"
    if num % 5 == 0:
        result += "buzz"
    return result or str(num)


print(*[fizzbuzz(i) for i in range(1, 101)], sep='\n')
