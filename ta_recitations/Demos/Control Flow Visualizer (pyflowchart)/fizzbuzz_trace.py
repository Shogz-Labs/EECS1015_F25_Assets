from typing import List

def fizzBuzz(n: int) -> List[str]:
    assert isinstance(n, int), 'n must be an integer'
    assert 1 <= n <= 10 ** 4, 'n is out of bounds'
    sol = []
    for i in range(1, n + 1):
        divThree = i % 3 == 0
        divFive = i % 5 == 0
        s = ("Fizz" * (divThree) + "Buzz" * (divFive)) or str(i)
        sol.append(s)
    return sol