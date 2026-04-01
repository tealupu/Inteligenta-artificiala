def suma(x):
    return sum(x)


print(suma([5, 10, 3]))


def my_fun(arg1, *argv):
    print("First Argument: ", arg1)
    for arg in argv:
        print("Next Argument through *argv :", arg)


my_fun('Hello', 'Welcome', 'to', 'python')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" % (key, value))


my_func(first='B', mid='to', last='C')

#Fibonacci

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
result = fib(10)
print(result)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
