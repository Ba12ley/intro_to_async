from typing import List


# Fibonachi
# def fib(n: int) -> List[int]:
#     numbers = []
#     current = 0
#     next = 1
#     while len(numbers) < n:
#         current, next = next, current + next
#         numbers.append(current)
#     return numbers


def fib():
    current = 0
    next = 1
    while True:
        current, next = next, current + next
        yield current

result = fib()

for n in result:
    print(n, end=', ')
    if n > 2000:
        break
print('Finished')
