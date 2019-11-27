#problem 1b
#consider large n
import math

function_classes = ["O(n^2)","O(n)","O((logn)^2)","O(2^(2*n))","O(n^(1/2))","O(4^n)","O(2^n)","O(nloglogn)"]

testn = [5,10,20,500,1000,10000]

#   O(n^2)
def f1 (n):
    return n*n
    
#   O(n)
def f2 (n):
    return n

#   O((logn)^2)
def f3 (n):
    return math.log(n,2)**2

#   O(2^(2*n))
def f4 (n):
    return 2**(2*n)
    
#   O(n^(1/2))
def f5 (n):
    return n**(.5)

#   O(4^n)
def f6(n):
    return 4**n

#   O(O(2^n))
def f7(n):
    return 2**n

#   O(nloglogn)
def f8(n):
    return math.log(math.log(n,2),2)

# get runtimes

def getorder (n):
    complexity = []
    complexity.append( f1(n))
    complexity.append(f2(n))
    complexity.append(f3(n))
    complexity.append(f4(n))
    complexity.append(f5(n))
    complexity.append(f6(n))
    complexity.append(f7(n))
    complexity.append(f8(n))
    return complexity

for j in testn:
    print("N="+str(j))
    for i in range (len(function_classes)):
        complexity = getorder(j)
        print(function_classes[i]+ ":  " + str(complexity[i]))


    
    

        