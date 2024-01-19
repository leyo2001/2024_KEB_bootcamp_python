import random

# numbers = list()
# for i in range(10):
#     numbers.append(random.randint(1,100))

numbers = [random.randint(1,100) for i in range(10)]

print(numbers)
try:
    pick = int(input(f"Input index(0 ~ {len(numbers)-1}): "))
    print(numbers[pick])
    print(5/0)
except IndexError as err:
    print(f"Out of range : Wrong index number\n {err}")
except ValueError as err:
    print(f"Input Only Number\n {err}")
except ZeroDivisionError as err:
    print(f"denominator can\'t 0\n {err}")
except Exception:
    print("Error occurs")

