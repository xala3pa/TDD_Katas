def fizzbuzz(num: int) -> str:
    if num % 3 == 0:
        return "fizz"
    if num == 5:
        return "buzz"
    return str(num)
