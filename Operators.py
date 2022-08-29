# a,b=[float(x) for x in input().split()]
# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a)
# print(b//a)

""" Arithmetic Operators """
# a=float(input("Enter the Value Of a:"))
# b=float(input("Enter the value of b:"))
# a,b=[int(x) for x in input("Enter The Value Of a and b:").split()]
# print(f"The Value of {a} + {b} is {a+b}")
# print(f"The Value of {a} - {b} is {a-b}")
# print(f"The value of {a} * {b} is {a*b}")     #  here before the string we wrote "f" is called as "fast string"
# print(f"The value of {a} / {b} is {a/b}")
# print(f"The value of {a} // {b} is {a//b}")
# print(f"The value of {a} % {b} is {a%b}")
# print(f"The value of {a} ** {b} is {a**b}")

"""Floor Division"""
# c=6//3
# print(c)   #2
# d=6.0//3
# print(d)  #2.0
# e=6//3.0
# print(e)   #2.0
# f=7.0//3
# print(f)   #2
# g=7.0/3
# print(g)   #2.3333333333333335

""" Assignment Operators"""
# a=5;b=6
# a=a+b
# print(a)  #a=11
# a=a+a
# print(a)  # a=22

# a=5
# a+=3
# print(a)  # a=a+3 a=5+3 a=8
# a-=4
# print(a)   # a=a-4 a=8-4 a=4
# a*=2
# print(a)  # a=a*2 a=4*2 a=8
# a/=2
# print(a)  # a=a/2 a=8/2 a=4.0
# a**=2
# print(a)  # a=a**2 a=4.0**2 a=16.0

# k=int(input("Enter the Value of k:"))
# print(f"The value of k is {k}")
# k+=2
# print("The Value of k After k+=2 is {}".format(k))
# k-=6
# print("The value of k after k-=6 is {}".format(k))
# k*=2
# print("The Value of k After k*=2 is {}".format(k))
# k/=2
# print("The value of k after k/=2 is {}".format(k))
# k**=2
# print("The value of k after k**2 is {}".format(k))

"""Relational/Comparision Operators"""
# a=int(input("Enter the Value of a:"))
# b=int(input("Enter the VAlue of b:"))
# print(f"The Value of {a} < {b} is {a<b}")
# print(f"The value of {a} > {b} is {a>b}")
# print(f"The value of {a} <= {b} is {a<=b}")
# print(f"The value of {a} >= {b} is {a>=b}")
# print(f"The value of {a} == {b} is {a==b}")
# print(f"The Value of {a} != {b} is {a!=b}")

# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# print("The value of %d<%d=%d"%(a,b,a<b))  # here '0' means "False"
# print("The value of a=%d , b=%d and a<b=%d"%(a,b,a<b))  # here '1' means "True"
# print("The value of a=%d , b=%d and a>b=%d"%(a,b,a>b))  # here '0' means "True"
# print("The value of a=%d ,b=%d and a<=b=%d"%(a,b,a<=b))  # here '1' means "True"
# print("The Value of a=%d , b=%d and a>=b=%d"%(a,b,a>=b))  # here '0' means "False"
# print("The value of a=%d , b=%d and a==b=%d"%(a,b,a==b))
# print("The value of a=%d , b=%d and a!=b=%d"%(a,b,a!=b))

"""Logical Operator"""
# a=int(input("Enter The value of a:"))
# b=int(input("Enter The Value of b:"))
# print("The value of a<b and b>a is {}".format(a<b and b>a))
# print("The value of a>b and a<b is {}".format(a>b and a<b))
# print("The value of a==b and a!=b is {}".format(a==b and a!=b))
# print("The value of a==b or a<b is {}".format(a==b or a<b))
# print("The value of a!=b or a>b is {}".format(a!=b or a>b))
# print("The opposite of {}=={} is {}".format(a,b,not a==b))
# print("The opposite of {}!={} is {}".format(a,b,not a!=b))

"""BitWise Operators"""
# print(5&9)
# print(5|9)
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# c=int(input("Enter the value of c:"))
# print("The Value of {} & {} is {}".format(a,b,a&b))
# print("The value pf {} | {} is {}".format(a,b,a|b))

"""Note: The Formula for Negation (~) is -(value+1) """
# print("The value of ~{} is {}".format(a,~a))
# print("The value of ~{} is {}".format(c,~c))

""" Identity Operator"""
# a=20
# b=20
# if(a is b):
#     print("a and b have same identity")
# else:
#     print("a and b not have same identity")

# if(id(a) == id(b)):
#     print("a and b is have same identity")
# else:
#     print("a and b is not have same identity")

# g=5
# print(type(g) is int)
# print(type(g) is not float)
# print(type(g) is float)
# h=5.23
# print(type(h) is int)
# print(type(h) is float)
# print(type(h) is not float)

"""Membership Operator"""
# family=['Lokesh','rama','Tirupathi','parvathi','Simhachalam','Sai','sandhya','Bhargav',
#         'bindhu','Charan','Arun','Prasanth','Hari','Welcome']
# print('Lokesh' in family)
# print('sandhya' in family)
# print('madhavi' in family)
# print('madhavi' not in family)
# print('gauthami' not in family)
# print('ramya' not in family)
# print('rama' not in family)
# family.sort()
# print(family)
# name=['p','L','m','S']
# name.sort()
# print(*name)
# name.sort(reverse=True)
# print(name)
# for l in name:
#     print(l)

"""Shift Operator (>>Right /2 and << Left *2)"""
# a=20
# print(a>>1)
# print(a>>2)
# print(a>>3)
# print(a>>4)
# print(a>>5)
# print(a>>6)
# b=8
# print(b<<1)
# print(b<<2)
# print(b<<3)
# print(b<<4)
# print(b<<5)