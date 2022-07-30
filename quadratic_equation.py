a = float(input("enter a :"))
b = float(input("enter b :"))
c = float(input("enter c :"))

positive = (-b + (b**2 - (4*a*c))**0.5)/2*a
negative = (-b - (b**2 - (4*a*c))**0.5)/2*a
print("Roots of Quadratic Equation  are : "+ str(positive) +"," +str(negative))