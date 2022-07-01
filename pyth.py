"""d2={"mayank":"moon", "mutable":"which cana be changed"}
word=input()
print(d2[word])
"""
# s = set()  # set bs unique values hi return krta hai. like isme agr hum do bar 3 daal diye aur print karwaye to bs ek bbar hi 3 dikhayga !----> isliye ye set se alag hai
# l=[1,2,3,4,3,5]
#slist = set(l)
# print(slist)
# s.add(3)
# s.add(5)
# s.add(2)
# s.add(3)
# s.add(4)
# s1=s.union([1,2,3])  # ye maths wala hi union hai.
# print(s)
# print(s1)
# print(s,s1)
# s2=s.intersection({3,5,7,8})
# print(s)
# print(s2)
# print(s,s2)
# print(len(s1))
# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s2))
"""print("age:= ")
age=int(input())
if (age<7 or age >100) :
    print("data not available")
elif age >18 :
    print("you can drive")
elif age == 18 :
    print("we have to think my child")
else :
    print("u can't drive we are extremely sorry")
list2=[2,3,5,6,7]
if 5 in list2:           #"in" ek keyword hai
    print("heyyy")
else:
    print("hehe")    """
#operatr = input("enter opertor u need \n")
#var1= int(input("first number \n"))
#var2= int(input("second number \n"))
#opr= input("type of operator \n")
# if var1==45 and var2==3 and opr =="*":
#    print ( "45 * 3 = 555")
# elif var1== 56 and var2 ==9 and opr =="+":
#    print( " 56 + 9 = 77")
# elif var1==56 and var2==6 and opr =="/":
#    print( "56 / 6 = 4")
# elif opr =="*":
#    print(var1 * var2)
# elif opr =="/":
#    print(var1 / var2)
# elif opr =="+":
#    print(var1 + var2)
# elif opr == "-":
#    print(var1 - var2)
# else :
#    print("kya kr hai bhai tu")
# for loop
#list1 = [["harry", 2], ['mayank',30],["parul",8]]
#dict1 = dict(list1)
# print(dict1)
# for name , objects in dict1.items() :
#    print(name , objects)
#list2 =[int , float, 2 ,45, 67,3, 78 ,'mayank',6]
# for item in list2 :
#    if str(item).isnumeric() and item > 6:
#        print(item)
# ************while loopL***********
#i= 0
# while(True):
#    if i+1<5:
#        i=i+1
#        continue
#    print(i+1 , end=" ")
#    if(i==44):
#        break
#    i=i+1
# while (True):
#    inp = int(input("enter your  number \n"))
#    if inp<100 :
#        print(inp)
#        continue
#    else:
#        break

# while (True):
#    inp = int(input("enter your  number \n"))
#    if inp>100 :
#        print("congrats you have entered a number greater than 100 \n")
#        break
#    else:
#        print("try again! \n")
# ***********Exercise 3-->"guess the number"**************
#user = int(input("enter number whihch u want to guess \n"))
#i = 1
# while i < 10:
#    inp = int(input("enter your guess \n"))
#    if inp > user:
#        print("you have to guess another number but less than your choosen number")
#        print("And now u have only", 9-i, " guess left")
#        i = i+1
#    elif inp < user:
#        print("you have to guess another number but greater than your choosen number")
#        print("And now u have only", 9-i, " guess left")
#        i = i+1
#    else:
#        print("congratulations you have guessed the number")
#        break
# if i <= 9:
#    print("you are winner")
# else:
#    print("your game is over")

#********pre define function******#
# def func2(a, b):
#    """hiiii how are u"""
#    average = (a + b)/2
#
#
#    print(average)
#    return average
#
#
#v = func2(2, 5)
# print(v)
# print(func2.__doc__)

"""try exception handling"""
"""inp= input("enter number 1 \n")
inp1 =input("enter 2nd number \n")
try:
    print("sum of given numbers are", int(inp)+int(inp1))
except Exception as g:
    print(g) """
# print('hehe')
# FILE IO BASICS
"""
"r" - open file for reading - default
"w" - open file fow writing
"x" - creates file if not exists
"a" - Add more contents to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""
# f = open("sample1.txt", "r")   # read mode
# f = open("sample1.txt", "rt")    #read + text mode
# f = open("sample1.txt", "rb")    # read in binary mode
# f= open("sample1.txt","w")      # write mode open hogya ab hum isme jo bhi likhenge wo overwrite kr dega
# f= open("sample1.txt","a")     #append mode me open hua hai to ab jo bhi likhenge wo last me add hite jayga
# f= open("sample1.txt","r+")     # reasd and write mode both
#f.write(" hehe thank you")
# print(f.read())
#f.write(" hey buddyyyy ! light weighttttt")
# b = f.write(" hey buddyyyy ! light weighttttt") #`return krega ki kitne character apan add kiye
# print(b)
#content = f.read()
# print(content)
# for reading line by line
"""for lines in content: #isse character by character  print krega
    print(lines)"""

""" for line in f:    
#iske liye content = f.read( )nhi krte kyoki aaise krne se vo nul ho jata hai 
    print(line,end=" ") """
# print(f.readline()) #iske liye content = f.read( )nhi krte kyoki aaise krne se vo nul ho jata hai
# f.close()

# exercise_4
"""user_in = int(input("enter number of rows \n"))
boolean = int(input("enter 1 or 0 \n"))
m = bool(boolean)
if m ==True :
    for a in range(user_in):
     b=1
     for b in range(a+1):
        print(" * ",end=" ")
     print("\n")    
else:    
    for c in range(user_in):
     for d in range(user_in - c):
        print(" * ", end= " ")
     print("\n")    """

"""f = open("sample1.txt")
print(f.tell())   # ye hume ye batayga ki abhi humara pointer kaunse character me hai
print(f.readline())
#print(f.tell())
f.seek(0)    # seek function pointer ko waps se waha reside kara deta hai jaha hum chahte hau ::- jo bracket me rahega waha
print(f.readline())
f.close()"""
# With block to open python Files
# with open("sample1.txt") as f:   #isse open aur close dono ho jata hai
#     a= f.readline()
#     print(a)
#
#g= open("sample1.txt","r")
# print(g.readline())
# l=10
# def func1(n):
#    global l
#    m=4
#    l=3
#    l=l+4
#    print(l,m)
#    print(n,"  i have printed" , l)
# func1("hello")
# print(l)
# x=89
# def harry():
#     x= 20
#     def rohan():
#         global x
#         x=88
#     print("before calling rohan()", x)
#     rohan()
#     print("after calling rohan()", x)
# harry()
# print(x)
# def factorial(n):
#    fac =1
#    for i in range(n):   # iska mtlb i 0 se n-1 tak jayga
#        fac = fac *(i+1)
#    return fac
#number = int( input("enter your number \n"))
#j= factorial(number)
# print(j)
# uper wala tarita itrative tha naki recursive
""" Recursion"""
# def factorial(n):
#    if n==1 or n==0:
#        return 1
#    else:
#        return n*factorial(n-1)
#
#number = int( input("enter your number \n"))
#j= factorial(number)
# print(j)
# fibonaci series
"""def fibo(n):
    if n==0:    #we are considering first index as 0
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)   

number = int(input("enter nth index whose fibonaci number u want \n "))
print(fibo(number))
"""

########## Lambda function########
# example:-
#minus = lambda x,y : x-y
# print(minus(7,9))
# def a_first(a):
#    return a[0]
#a= [[1,14],[9,6],[8,23]]
#a.sort(key= a_first)
# print(a)

# this can also be done with the use of lambda function

# a = [[1, 14], [9, 6], [8, 23]]
# a.sort(key=lambda b: b[1])
# print(a)

# mport random
#random_number = random.randint(0,   90)
# print(random_number)
#rand = random.random()*100
# print(rand)
#lst=["star plus","humagama","zee tv",1,45]
#choize= random.choice(lst)
# print(choize)
#z= random.getrandbits(10)
# print(z)
# _________exercise 6 :- snake water gun
"""user =0
cpu = 0
print("and here we go !! good luck")
n=1
lst1 =["snake","water","gun"]
while n<=10:
    choize1 = random.choice(lst1)
    print("what you want to chose from snake, water and gun")
    inp = input("snake__water__gun \n")
    
    if choize1 == "snake" and inp =="water":
        print("computer won ")
        cpu=cpu+1
        n=n+1
        
    elif choize1 =="snake" and inp == "gun":
        print("you won")
        user =user +1
        n=n+1
        
    elif choize1 == "water" and inp =="snake":
        print("you won")
        user = user +1
        n=n+1
        
    elif choize1 == "water" and inp =="gun":
        print("computer won ")
        cpu = cpu+1
        n=n+1
        
    elif choize1 == "gun" and inp =="water":
        print("you won")
        user = user +1
        n=n+1
        
    elif choize1 == "gun" and inp =="snake":
        print("computer won ")
        cpu = cpu +1
        n=n+1
        
    else :
        print("drawwww")
        n=n+1
if user>cpu:
   print("your are winner !!!!")
elif user == cpu:
    print("drawww")
else:    
    print("computer is winner")   
     """"""import platform
import math
import time
##########___fstring____#########
me = "mayank"
#aa = "chemical branch and %s"%me
#print(aa)
#****************
#a1 = 3
#a = "this %s %s"%(me,a1)
#print(a)
#****************
#a1 =3
#a="this is {} {}"
#b= a.format(me,a1) #agr hum uper brackets me 1 aur 0 daal se ie {1}{0} to me ki value {0}me jayga .
#print(b)
#****************
a1=3
a= f"this is {me} {a1} {math.sqrt(25)}"  #this is f string ie: fast string and most readable form
print(a)
"""
# _____*ARGs and *kwargs_____
"""kisi bhi huamre banaye hue function me parameters /arguments fixed hote the aur future aspect me vo helpful nhi hita kyoki hume new entities add krne hote hai thatswhy we use args and kwargs
isme normal phir *args phir *kwargs hog hamesha aur ye as a touple hi pass hota hai """
# def funct1_name(animal, *args,**kwargs):
#    print(normal)
#    for items in args:
#     print(items)
#    print("\n now lets see some heroes \n")
#    for key,value in kwargs.items():
#     print(key," is a ",value)
# normal =  "hey there! normal here"
# har=["mayank","parul","himanshu","mrinal"]
# kw ={"mayank":"monitor","parul":"dancer","himanshu":"player","mrinal":"teacher"}
# funct1_name(normal,*har,**kw)
# ______Time Modulation_____
#import time
# k=0
#normal1 = time.time()
# while k<45:
#    print("hey mayank")
#    #time.sleep(2)
#    k+=1
#print("time taken: ", time.time()- normal1," seconds")
#normal2 = time.time()
# for i in range(45):
#    #time.sleep(2)
#    print("hey mayank")
#print("time take: " ,time.time()-normal2, " seconds")
#localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
# ______enumerate function


# li=["Bhindi","gobhi","aloo","chips"]
# for index , items in enumerate(li):    #enumerate function use krne se hume uski value aur index ka value pata chal jata hai jo 0 se initialize hota hai.
# if index%2 is 0:
#   print(items)
#import sklearn as sk
# print(sk.__version__)
#import sys
# print(sys.path)
#import abcd
# print(abcd.b)
#print(abcd.pstr(" hehehehe"))
# print(abcd.add(6,7))
# lis = ["mayank","parul","mrinal","himanshu","sam"]
# a = " and ".join(lis)
# print(a, "other avengers")
# _____________Map_________________
# num = ["3","34","64"]
# # for i in range(len(num)):
# #     num[i]=int(num[i])    .... ye thoda hectic hai
# #.... so ab hum Map ki help lenge aur ye humeshsa ek object return krta hai aur max case me list ke  sath use hota hai ! isme hum sabse pehel vo function likhenge jisse sare element pe run krna hain aur phir vo list jisko change krna hai. Hum yaha lembda function use kr skte hai
# # num2 = list(map(int,num))
# num2= list (map(lambda x : int(x), num ))
# num2[2]=num2[2]+2
# print(num2[2])
# lst = [2,3,4,5,6,7,8]
# lst2 = list(map(lambda x : x*x, lst))
# print(lst2)
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for i in range(5):  #aisa krne se vo apne aap 0,1,2,3,4 le elaga
#            val=list(map(lambda x:x(i),func))
#            print(val)
# ___________filter function_________
# filter function is to give put put as per condition given as a list isme pehel function likhte hai phir itteratir
# lis1 =[1,2,3,4,5,65,7,8,9,0,9,866,44,32]
# def is_greater_5(num):
# return num>5
# gr_than_5 =  list(filter(is_greater_5,lis1))
# print(gr_than_5)
# ____________ Reduce Function________
# ye functools ka part hota hai to waha se import karwate hai
# list1 = [1,2,3,4]  # hume iska sum chahiyue
# # num = 0
# # for item in list1:
#     # num= num+item
# # print(num)   ye thoda ajeeb sa hogya kyoki python me hum isse ek function me ek line me kr skte hai
# from functools import reduce
# num = reduce(lambda x,z:x+z,list1)  #pehle ke do number ko add krega phir jo result ayga usko tesre se add krega
# print(num)
# ______eaxmple of returning function through function
# def mayankret(func1):
# if func1 == 0:
# return print
# elif func1==1:
# return int
# funct1 = 0
# print(mayankret(funct1))
# def exec(func):
#     func("heyyyy")
# exec(print)
# def dec1(func1):
# def nowexec():
# print("Executing Now")
# func1()
# print("Executed")
# return nowexec
# @dec1      #yehi hai decorator ka symbol aur is @dec1 ka same matlan hai jo "mayank_here=dec1(mayank_here)" ka hai
# def  mayank_here():
# print("mayank iss awesomee")
# mayank_here()
# mayank_here=dec1(mayank_here)
# mayank_here()
"""________________________________________________________"""
# class student:
# pass
#
#
# harry = student()
# larry = student()
#
# harry.name = "harry"
# harry.std = 12
#
# harry.section = 1
# print(harry.std)
"""class me agr koi varible hai with some values to hum us class se derived sare object se us variable ko call kr skte hai par CHANGE nhi kr skte hai..change sirf tabhi hoga jab hum us variable ko classs ke naam ke sath call kre"""
# class students :
#    def __init__(self,aname, asalary, arole):  #here it is constructor
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#    def printdetail(self):
#        return f"The name is {self.name} . Salary is {self.salary}. His/Her role is {self.role}"
#
#
#    pass
#harry = students("Mayank",1200000,"manager")
# print(harry.printdetail())
# print(harry.__dict__)
# larry = students()
"""________________________________________________________________________________"""


# class Employee:
#    no_of_leaves = 8
#
#    def __init__(self, aname, asalary, arole):  # here it is constructor
#    self.name = aname
#    self.salary = asalary
#    self.role = arole
#
#    def printdetail(self):
#    return f"The name is {self.name} . Salary is {self.salary}. His/Her role is {self.role}"
#
#    @classmethod
#    def change_no_leaves(cls, newleaves):
#    cls.no_of_leaves = newleaves
#
#    @classmethod
#    def from_str(cls, string):
# """params = string.split("-")
#    print(params)
#    return cls(param[0], param[1], param[2]) """
# return cls(*string.split("-"))
#
#    @staticmethod
#    def printgood(string):
# print("This is good "+string)
# return " "
#
#
# harry = Employee("Harry", 1200000, "Manager")
# rohan = Employee("Rohan", 3400000, "Executor")
# rohan.change_no_leaves(34)
#from unicodedata import name
#
#from sklearn.linear_model import GammaRegressor
#
#
# print(rohan.printdetail())
# print(rohan.no_of_leaves)
# print(Employee.no_of_leaves)
# print(harry.no_of_leaves)
# karan = Employee.from_str("Karan-234565-Student")
# print(karan.printdetail())
# karan.printgood("Karan")
# Encapsulation - implementation ke detail ko hide kr dena
# class programmer(Employee):
# def __init__(self, aname, asalary, arole,alanguage):
#    self.name = aname
#    self.salary = asalary
#    self.role = arole
#    self.language = alanguage
# def printProg(self):
# return f"The name is {self.name} . Salary is {self.salary}. His/Her role is {self.role}. Language is {self.language}"
# print f"the programmer is {self.name}. The salary is {self.salary}.
#
# harry = Employee("Harry", 1200000, "Manager")
# rohan = Employee("Rohan", 3400000, "Executor")
# rahul = programmer("Rahul",22222222,"producer",["python","c++"])
# print(rahul.printProg())
# _______________Multiple Inheritance____________________
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):  # here it is constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"The name is {self.name} . Salary is {self.salary}. His/Her role is {self.role}"

    @classmethod
    def change_no_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        """params = string.split("-")
           print(params)
           return cls(param[0], param[1], param[2]) """
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good "+string)
        return " "


class player:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetail(self):
         return f"The name is {self.name} . Game is {self.game}."

class CoolProgrammer(player, Employee):
    pass
harry = Employee("Harry", 1200000, "Manager")
rohan = Employee("Rohan", 3400000, "Executor")
karan = CoolProgrammer("Karan","footBall")
print(karan.printdetail())