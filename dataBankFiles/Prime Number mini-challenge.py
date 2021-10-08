def prime(n):
    if n < 0:
        print('Please give a positive integer')
        return
    elif n == 0 or n == 1:
        return False

    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False
