num_a = 1
num_b = 100
def find_primes(num_a, num_b):
    primes = []
    for num in range(num_a, num_b + 1):
        if num < 2:
            continue
        if num == 2:
            primes.append(num)
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

print(find_primes(num_a, num_b))