 def isHappy(self, n: int) -> bool:
        memory=set()
        if n == 1:
            return True
        if n == 0:
            return False
        while n!=1:
            if n in memory:
                return False
            memory.add(n)
            n = sum(int(i)**2 for i in str(n))
            print(n)
        return True
