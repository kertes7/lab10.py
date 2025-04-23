#task 1

def factorial_recursive(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Число повинно бути цілим і невід'ємним")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


#task 2

def fibonacci_recursive(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Число повинно бути цілим і невід'ємним")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


#task 3

def sum_list_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

#task 4

def is_palindrome_recursive(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])
