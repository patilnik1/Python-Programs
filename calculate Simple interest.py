#program to calculate Simple interest

p = float(input("Enter Value of p:"))
r = float(input("Enter Value of rate:"))
n = int(input("Enter number of year:"))

si = p*r*n/100
print("Simple interest= ", si)