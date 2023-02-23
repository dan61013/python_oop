# 簡化方法
# 整理出可獨立維護的單元function
# main只做簡易的操作

def checkPositiveInteger(num):
    if (not isinstance(num, int)) or (num <= 0):
        raise ValueError(f"Invalid positive integer: {str(num)}")

def primeFactorize(num):
    
    checkPositiveInteger(num)
    
    prime_factorize = dict()
    i = 2
    while (num > 1):
        if num % i == 0:
            prime_factorize[i] = prime_factorize.get(i, 0) + 1
            num /= i
        else:
            i += 1
    return prime_factorize

def findGCF(nums):
    prime_factorize = [primeFactorize(num) for num in nums]
    
    common_prime = set(prime_factorize[0].keys())
    for pf in prime_factorize[1:]:
        common_prime  &= set(pf.keys())
    
    gcf = 1
    for prime in common_prime:
        m = min([pf[prime] for pf in prime_factorize])
        gcf = gcf * (prime ** m)

    return gcf

def findLCM(nums):
    gcf = findGCF(nums)
    lcm = gcf
    for num in nums:
        lcm *= int(num / gcf)
    return lcm

def main():
    str_numA = input("Positive Integer A: ")
    str_numB = input("Positive Integer B: ")

    numA = int(str_numA)
    numB = int(str_numB)

    nums = [numA,numB]    
    gcf = findGCF(nums)
    lcm = findLCM(nums)

    print("Greatest Common Factor: " + str(gcf))
    print("Lowest Common Multiple: " + str(lcm))

if __name__ == "__main__":
    main()