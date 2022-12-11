import os
import math

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = math.floor(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True

def find_p(primes:list, powers:list):
    p = 1
    for idx in range(len(primes)):
        p *= math.pow(primes[idx], powers[idx])
    return int(p+1)
  
def is_power(a, max):
    for i in range(2, math.floor(math.sqrt(max))+1):
        if math.log(a, i).is_integer() and not is_prime(a):
            if math.log(a, i) != 1:
                return True
    return False

def pow_mod(B, E, M):
    if E == 0:
        return 1
    elif E == 1:
        return B % M
    else:
        root = pow_mod(B, E // 2, M)
        if E % 2 == 0:
            return (root * root) % M
        else:
            return (root * root * B) % M

def find_prime_root(powers, p):
    for i in range(2, 10):
        if not is_power(i, p):
            for t_pow in powers:
                # print("Checking {} to the {}, (mod {})".format(i, t_pow, p))
                res = int(pow_mod(i, t_pow, p))
                # print("Result is: {}".format(res))
                if res == 1:
                    break
                elif t_pow == powers[-1]:
                    return i

if __name__ == "__main__":

    input_data = []
    with open(os.getcwd() + "\\ieeja.txt") as input:
        for line in input.readlines():
            input_data.append(int(line))

    k = input_data[0]
    p_values = input_data[1:k+1]
    e_values = input_data[k+1:]

    p = find_p(p_values, e_values)

    test_powers = []
    for p_val in p_values:
        test_powers.append(int((p-1)/p_val))

    if is_prime(p):
        print(find_prime_root(test_powers, p))
    else:
        print("P: {} is not prime".format(p))       
