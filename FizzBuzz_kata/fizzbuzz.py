def fizzbuzz(num: int) -> str:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    return str(num)


print(*[fizzbuzz(i) for i in range(1, 101)], sep='\n')
