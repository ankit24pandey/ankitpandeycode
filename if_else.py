"""
var1=89
var2=int(input())
if var2>var1:
    print(var2," is greater")
elif var1==var2:
    print("equal")
else:
    print(var1, " is greater")

l=[3,6,87]
print(34in l)
if 34 in l:
    print("yes its in l")

print("enter age")
age=int(input())
if age>18:
    print("you are allowed to drive")
elif age==18:
    print("we cant decide")
else:
    print("you are not allowed")
"""
#to find bonus of employee:-----------------------------------------------------------------------
"""
print("enter years of work")
a=int(input())
print("enter salary")
b=int(input())
if a>5:
    c=b+(5*b)/100
    print("your salary is " ,c)
else:
    print(b)
   """
#to find it is square or not---------------------------------------------------------------
"""
print("enter length")
a=int(input())
print("enter breadth")
b=int(input())
if a==b:
    print("it is square")
else:
    print("no its not square")
   """
#to findout which num is greater-----------------------------------------------------
"""
print("enter n1")
n1=int(input())
print("enter n2")
n2=int(input())
if n1>n2:
    print(n1, " is greater")
elif n1==n2:
    print("equal")
else:
    print(n2, "is greater")
    """
#to find price----------------------------------------------------------
"""
print("enter number of quantity")
n=int(input())
print("total price")
p=n*100
print(p)
if p>=1000:
    cost=p-(p*10)/100
    print(cost)
else:
    print("cost is ",p)
"""
#TO FIND GRADE---------------------
"""
print("enter marks of student")
n=int(input())
if n<33:
    print("f")
elif n>=33 and n<=50:
    print("d")
elif n>50 and n<=60:
    print("c")
elif n>60 and n<=80:
    print("b")
else:
    print("A")
"""
#to find student is allowed or not to sit in class----------------
"""
print("enter num of class held")
h=int(input())
print("enter num of class attend by student")
s=int(input())
print("enter medical cause")
m=input()
p=(s/float(h))*100
print(p)
if p>=75:
    print("allowed")
else:
    if m=='y':
        print("you are allowed because of medical cause")
    else:
        print("not allowed ")
"""
#to check leap year or not---------------------
"""
print("enter year")
y=int(input())
if y%4==0 and y%400==0:
    print("leap year")
else:
    print("not a leap year")
"""
#to find work-------------------
"""
print("enter your age")
a=int(input())
print("enter your gender")
g=input()
if g=='f':
    print("work in URBAN AREAS")
else:
    if g=='m' and a>=20 and a<=40:
        print("work anywhere")
    elif a>=40 and a<=60:
        print("work in URBAN AREAS")
    else:
        print("erroor")
"""
# to find electricity bill-----------------------
# 1.if unit is less than 100 no charge--
# 2.if unit is grater than 100 and less 200 then first 100U is free and next 100U is calculate by 5rs--
# 3. after 200U rs 10-----------------------
"""
print("enter unit")
u=int(input())
amt=0
if u>100 and u<=200:
        amt=(u-100)*5
        print("yout amt is ", amt)
elif u>200:
    amt=500+(u-200)*10
    print("your amt is ",amt)
else:
        print("no charge")
"""
# to pay tax on vehicles-----------
"""
print("enter price of bike")
price=int(input())
if price>100000:
    tax=(15/100)*price
    print("road tax is ",tax)
    ta=price+tax
    print("now cost of your bike after road tax is ",ta)
elif price>=50000 and price<=100000:
    tax=(10/100)*price
    print("road tax is ",tax)
    ta=price+tax
    print("now your bike cost is ",ta)
else:
    tax=(5/100)*price
    print("road tax is ",tax)
    ta=price+tax
    print("your bike price is ",ta)
"""
# to display a day-------------------
"""
print("enter num")
num=int(input())
if num==1:
    print("monday")
elif num==2:
    print("tuesday")
elif num==3:
    print("wednesday")
elif num==4:
    print("thursday")
elif num==5:
    print("friday")
elif num==6:
    print("saturday")
elif num==7:
    print("sunday")
else:
    print("not a day")
"""
# to monument of city-----------------------------------------------------------
"""
print("enter city")
city=input()
if city=='delhi':
    print("red fort")
elif city=='uttarpardesh':
    print("ram mandir")
elif city=='mumbai':
    print("taj hotel")
else:
    print("everything")
"""
# check whether a num is divisible by 2 and 3 both=============
"""
print("enter any number")
n=int(input())
if n%2==0 and n%3==0:
    print("yes it is divisible by 2 and 3")
else:
    print("not")
"""
# To print maximum number among 3========================
"""
print("enter number")
a=int(input())
b=int(input())
c=int(input())
print(max(a,b,c))
"""
# to find youngest age--------------------
"""
print("enter age")
a=int(input())
b=int(input())
c=int(input())
print("youngest age is ",min(a,b,c))
"""
# to check element present in code or not------------------------
"""
print("enter character")
character=input()
vow='a','e','i','o','u'
if character in vow:
    print("yes")
else:
    print("no")
"""
# to check which triangle it is------------------
"""
print("enter sides")
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print("it is euqilateral ")
elif a==b  or a==c or b==c:
    print("isoceles")
else:
    print("scalane")
"""
# to check that triangle is possible or not--------------------------------
"""
print("enter side")
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("yes triangle is possible")
else:
    print("not possible")
"""
# to calculate the bill----------------------
"""
print("enter number of days")
days=int(input())
if days<=5:
    cost=2*days
    print(cost)
elif days>5 and days<=10:
    cost=3*days
    print(cost)
elif days>11 and days<=15:
    cost=4*days
    print(cost)
else:
    cost=5*days
    print(cost)
"""
# to calculate bill per kilometre--------------------
"""
print("enter kilometre")
k=int(input())
if k<=10:
    cost=11*k
    print("amount is ", cost)
elif k>10 and k<=100:
    cost=110+(k-10)*10
    print("amount is ",cost)
else:
    cost=1010+(k-90)*9
    print("your amount is ",cost)
"""
# to give stream---------------------------
"""
print("enter marks")
me=int(input())
ms=int(input())
mss=int(input())
if me>80 and ms>80 and mss>80:
    print("science stream")
elif me>80 and ms>50 and mss>50:
    print("commerece stream")
else :
    print("humanities")
"""