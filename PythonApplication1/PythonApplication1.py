for i in range(1,101):
    if not i % 3 and not i % 5:
        print(i, "FizzBuzz")
    elif not i % 5:
        print(i, "Buzz")
    elif not i % 3:
        print(i, "Fizz")
    else:
        print(i)
