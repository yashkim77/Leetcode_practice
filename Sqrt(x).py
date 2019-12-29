def mySqrt(self, x):
        if x == x*x:
            return x
        left = 1
        right = x
        while left < right:
            mid = (left + right)//2
            if x >= mid*mid:
                left = mid + 1
            else:
                right = mid
        return left-1
