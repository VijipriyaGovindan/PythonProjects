import math
class generators():
    def getsqrRoot(self,myNumber):
        for i in range(2,myNumber):
            yield round(math.sqrt(i),2)

    def getFibnoGen(self,myNumber):
        a , b =0,1
    
        for i in range(myNumber):
            yield a
            a,b = b, a+b
def main():
    mygenClass = generators()
    print(f" The square roots are {list(mygenClass.getsqrRoot(15))} ")
    print(f" The fib series are {list(mygenClass.getFibnoGen(15))} ")

if __name__ == "__main__":
    main()



        