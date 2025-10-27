class Prime:
    def __init__(self, *args):
        self.numbers = list(args)

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return False

        return True

    def get_prime_numbers(self):
        ans = []
        for num in self.numbers:
            if self.isPrime(num):
                ans.append(num)

        return ans




nums = Prime(1, 2, 5, 6, 8, 9, 2, 5, 11, 15)

print(nums.get_prime_numbers())