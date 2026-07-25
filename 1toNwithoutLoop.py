class solution:
    def printTillN(self, n):
            #code here 
            if n == 0:
                return
            self.printTillN(n-1)
            print(n, end=" ")


c1 = solution()
c1.printTillN(333)