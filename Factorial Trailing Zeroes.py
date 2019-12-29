def trailingZeroes(self, n: int) -> int:
    zeroes = 0
    while(n>=5):
       zeroes += int(n/5)
       n=n/5
     return int(zeroes)
