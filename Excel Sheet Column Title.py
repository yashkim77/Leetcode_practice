 def convertToTitle(self, n: int) -> str:
        string = ""
        while n>0:
            rem = n % 26
            if rem == 0:
                string = chr(90) + string
                n= n//26 -1
            else:
                string = chr((rem - 1) + ord('A')) +string
                n= n//26
        return string
