# 封裝 Encapsulation

"""
還記得「低耦合，高內聚」的原則嗎？為了符合這原則，每個物件都要盡可能的去包含需要用到的屬性和方法，
並且使得外部不能以不合理的方法去影響物件，這就稱之為「封裝」
"""

class Calculation:
    def __init__(self, nums):
        self._nums = nums  # {1}
        for num in self._nums:
            self._checkPositiveInteger(num)

    def _checkPositiveInteger(self, num):  # {2}
        if (not isinstance(num, int)) or (num <= 0):
            raise ValueError("invalid positive integer: " + str(num))

    def _primeFactorize(self, num):  # {3}
        prime_factorize = dict()
        i = 2
        while(num > 1):
            if num % i == 0:
                prime_factorize[i] = prime_factorize.get(i, 0) + 1
                num /= i
            else:
                i += 1
        return prime_factorize

    def findGCF(self):
        prime_factorize = [self._primeFactorize(num) for num in self.nums]

        common_prime = set(prime_factorize[0].keys())
        for pf in prime_factorize[1:]:
            common_prime &= set(pf.keys())

        gcf = 1
        for prime in common_prime:
            m = min([pf[prime] for pf in prime_factorize])
            gcf = gcf * (prime ** m)

        return gcf

    def findLCM(self):
        gcf = self.findGCF()
        lcm = gcf
        for num in self._nums:
            lcm *= int(num / gcf)
        return lcm

def main():
    pass

if __name__ == "__main__":
    main()