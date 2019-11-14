a=int(input("Enter length of first side"))
b=int(input("Enter length of second side"))
c=int(input("Enter length of third side"))
d=int(input("Enter length of forth side"))
if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
    print("It is a polygon")
elif a==c and b==d and a!=b and c!=d:
    print("It is a rectangle")
elif a==b==c==d:
    print("It is a square")
