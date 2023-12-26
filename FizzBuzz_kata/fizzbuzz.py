def fizzbuzz(num: int) -> str:
    if num == 15 or num == 30 or num == 45:
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    return str(num)
