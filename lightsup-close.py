w ,b, vars = "\033[7m", "\033[100m" , "\033[0m"
from os import system
q = input("1: Lights Up\n2: Lights Close\n: ")
if q == '1':
    system('cls')
    for i in range(1700):
        print(w + "_",end="")
    print("Light's Up",end=""+ vars)
    for i in range(1700):
        print(w + "_",end="")
elif q == '2':
    system('cls')
    for i in range(1700):
        print(b + "_",end="")
    print("Light's Close",end=""+ vars)
    for i in range(1700):
        print(b + "_",end="")