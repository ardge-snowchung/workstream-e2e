def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz string for n.

    - multiples of 3 and 5 -> "FizzBuzz"
    - multiples of 3       -> "Fizz"
    - multiples of 5       -> "Buzz"
    - otherwise            -> str(n)
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
