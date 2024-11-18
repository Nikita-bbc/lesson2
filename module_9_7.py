def is_prime(func):
    def wrapper(*args):
        mod_fun = func(*args)
        if mod_fun <= 1:
            print('Составное')
            return mod_fun
        if mod_fun <= 3:
            print('Простое')
            return mod_fun
        if mod_fun % 2 == 0:
            print('Составное')
            return mod_fun
        i = 5
        while i * i <= mod_fun:
            if mod_fun % i == 0 or mod_fun % (i + 2) == 0:
                print('Составное')
                return mod_fun
            i += 6

        print('Простое')
        return mod_fun

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


res = sum_three(10, 1, 0)
print(res)
