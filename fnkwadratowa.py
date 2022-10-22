import math
import matplotlib.pyplot as plt

while(True):
    x=int(input("Podaj wspolczynnik rownania x: "))
    maxX=int(input("Podaj wspolczynnik rownania maxX: "))
    if maxX<x:
        print("konczymy dzialanie funkcji.")
    else:
        deltaX=0.5
        dataX=[]
        dataY=[]

        a=int(input("Podaj wspolczynnik rownania a: "))
        b=int(input("Podaj wspolczynnik rownania b: "))
        c=int(input("Podaj wspolczynnik rownania c: "))

        while x<maxX:
            dataX.append(x)
            y=a*x*x+b*x+c
            dataY.append(y)
            x=x+deltaX

        for i in range(len(dataX)):
            print("x=%2.2f y=%2.2f" % (float(dataX[i]), (float(dataY[i]))))

        plt.figure("wykres fn")
        plt.plot(dataX, dataY)
        plt.grid(True)
        plt.xlim(dataX[0], dataX[-1])
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Wykres fn y=a*x*x+b*x+c")
        plt.savefig("fn.jpg", dpi=72)
        plt.show()

# delta=(b**2)-(4*a*c)

# print("delta to ", delta)

# if delta > 0:
#     x1=-b-math.sqrt(delta)/(2*a)
#     x2=-b+math.sqrt(delta)/(2*a)3

#     print("x1=", x1)
#     print("x2=", x2)

# else:
#     if delta==0:
#         x=-b/(2*a)
#         print("x=",x)
#     else:
#         print("brak miejsc zerowych")
   
  