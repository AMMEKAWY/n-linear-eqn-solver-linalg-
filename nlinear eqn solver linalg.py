import numpy as np
from numpy import linalg


print("the number of equations MUST be equal to the number of variables")

n=int(input("the number of equations="))

print("eqns MUST be on matrix form AX=Y")

a=np.zeros((n,n))
b=np.zeros((n,1))
c=np.zeros((n,1))
i=0
j=0
while i != n:
    j=0
    while j!= n:
        a[i,j]=float(input(print("a", i+1,j+1, "=")))
        j+=1
    i+=1

print(a)
i=0

while i != n:
    b[i,0]= float(input(print("y", i+1,1, "=")))
    i+=1

delta=round(linalg.det(a),4)

if delta==0:
    print("there is infinite number of solutions")

elif delta !=0:
    c=np.dot(linalg.inv(a),b)
    print(c)
    
    









