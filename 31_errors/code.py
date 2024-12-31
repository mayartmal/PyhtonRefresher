def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0")
    return dividend / divisor



divide(10, 1)

grades = [10, 11, 56, 11]
grades = []
print("it is average program")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("Empty grades list")
except ValueError:
    print("value error")
else:
    print(average)
finally:
    print("Thank you")