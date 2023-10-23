# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:37:07 2023

@author: mathi
"""

#lesson 2

R=0.08206
n=0.5
T=298.15
V=2.5
P=n*R*T/V
#print("At temperautre {} K the pressure is {} atm.".format(T,P))
print("At temperautre {} K the pressure is {} atm and the volume is {} L.".format(T,P,V))

a=5
b=complex(a)
print(b)

x=3
y=float(x)
print("The variable is {}".format(y))

z=7//10
Z=7%10
print(z,Z)


my_name=input("Enter your name")

print(my_name)



R=0.08206
n =input("Enter the number of moles:")
n= float (n)
T =input("Enter the temperature in K:")
T = float (T)
V=input("Enter the volume in L:")
V= float (V)
p = n*R*T/V
print("Gas pressure is {} atm".format(p))

n =float(input("Enter the number of moles:"))#autre de manière de le déclarer en float

r=10
h=3
V=(1/3)*3.14*(r**2)*h
print(V)



import math as m
#import sys
#import random
#import matplotlib
#import cclib

#dir (m)

ang = float(input("Enter a numerical variable:"))
ang_rad=ang*m.pi/180
si=m.sin(ang_rad)
print("The sine of {} is {}".format(ang,si))

#ex1
num1 =float(input("Enter a numerci value:"))
num2 =float(input("Enter another numerci value:"))
sum=num1+num2
product=num1*num2
print("The sum of {} and {} is {}".format(num1, num2, sum))
print("The product of {} and {} is {}".format(num1, num2, product))

#ex2
numA = float(input("Enter a temperature in Celsius:"))
conv=numA +273
print(conv)

#ex3
edge = float(input("Enter the length of the edge:"))
vol = edge**3
area = 6*(edge**2)
print("The volume of the cube is {} cm^3 and the area is {} cm^2".format(vol,area))

#ex4
money1 = float(input("How many banknotes of 10 do you have ?"))
money2 = float(input("How many banknotes of 20 do you have ?"))
money3 = float(input("How many banknotes of 50 do you have ?"))
sum=money1*10 +money2*20+money3*50
print("The total of money on your bank account is {} €".format(sum))

#ex5
radius = float(input("What is the radius of the circle ?"))
circumference = 2*3.14*radius
area = 3.14*(radius**2)
print("For a radius of {} cm the circumference is {} cm and the area is {} cm2.".format(radius,circumference,area))

#ex6
import math
angle = input("Give an angle :")
l1 = float(input("Give me the length of the first side:"))
l2 = float(input("Give me the length of the second angle:"))
c=((l1**2+l2**2)-(2*l1*l2*math.cos(math.radians(angle))))**(1/2)
print(c)

#lesson 3
message =("Good Morning")
print(len(message))

print(message[8])


print(message[8:]) #last character blank for includ it

print(message[-1])
print(message[:-1])
print(message.lower())
print(message.upper())

print(message.find('o'))
new_message = message.replace('Morning', 'Afternoon')
print(new_message)

print(dir[str])

num = input("Enter an integer:")
num = int (num)
if num<5:
    print("blablabla")
else:
    print("nvm")

num = int(input("Enter the number: "))
if num%2==0:
    print("The number {} is an even number".format(num))
else:
    print(f"The number {num} is an odd number") #f instead of putting format at the end of the quote*



#example number 667
marks = float(input("Enter ur marks: "))
if marks<40:
    print("Apagnan")
elif marks>=40 and marks <=50:
    print("il a les cramptés")
elif marks>=50 and marks <=75:
    print("Quoi ?")
elif marks>=75 and marks<=90:
    print("coubeh")
else:
    print("error")

#ex
weight = float(input("Rentre ton poids petit gros:"))
height = float(input("Enter your height in meters:"))
BMI = weight/height
if BMI<18.5:
    print("underweight")
elif BMI>=18.5 and BMI<25:
    print("normal weight")
elif BMI>=25 and BMI<30:
    print("overweight")
elif BMI>=30:
    print("obesity")
else:
    print("error")
    
#write a python program to convert temperatures
temp = input("Iput the temp you like to convert ? (e.g., 45F, 16°)")
degree = int(temp[:- 1])
i_convention = temp[- 1]

if i_convention.upper() == "C":
    result = int(round((9 *  degree)/ 5+32))
    o_covention =  "Fahrenheit"
elif i_convention.upper() == "F":
    result = int (round((degree - 32)*5/9))
    o_convention = "Celsius"
else :
    print("Input propper convention.")
    quit()
print("The temp in", o_convention, "is", result, "degrees.")

#divisible natural numbers

num1 =  int(input("Enter a natural number:"))
num2 =  int(input("Enter an other natural number:"))
q = num1%num2
if q == 0 :
    print("It is divisible")
    print(num1//num2)
else :
    print("It's not divisible")
    print("The result is",num1//num2,"and the rest" ,q)

#program to find a minimum of two  numbers

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a other number:"))
if num1 > num2 :
    print("The minimum is ", num2,".")
elif num1==num2 :
    print("Both numbers are equals.")
else :
    print("The minimum is ", num1,".")

#ex

units = int(input("Enter the numbers of units:"))
if units<=100 :
    print("No charge")
elif units >100 and units <200:
    print("The bill is Rs", 5*units-500)
elif units>=200 :
    print("The bill is Rs", 10*units-1500)


#Course on While

num = int (input("Enter an integervalue:"))

while num >0:
    res = num // 3
    print("the interger division of {} by 3 gives: {}".format(num, res))
    num = int(input("Enter an integer value"))

print("We're done")

#initialize a counter

num = int(input("Enter an integer value:"))
ndiv = 0
while ndiv<num:
    res = num // ndiv
    print("The integer division of {} by {} gives: {}".format(num, ndiv, res))
    ndiv = ndiv +1

print("We're done")
print("Total number of divisions : {}".format(ndiv))

#

num = int(input("Enter an integer value:"))
ndiv = 0
while num>0:
    res = num // 3
    print("The integer division of {} by 3 {} gives: {}".format(num, res))
    ndiv = ndiv +1
    print(("Number of divisions so far: {}".format(ndiv)))
    num = int(input("Enter an integer value:"))

print("We're done")
print("Total number of iterations : {}".format(ndiv))

#cours6: Les lists complex

a=[1,2,"5","Name"] #comment écrire une list

a.append("Margot") or a.add("Margot") #rajouter un élément dans la liste
a.remove("Name") #retire un élémengt de la liste
a[1]="ce que l'on veut changer" #permet de changer qqchose dans la liste 

print(a[1])#affiche un seul element de la liste

#les tuples sont immutable
#a_tuple=("joe","margot",2021-01") #on ne peut pas ajouter , changer ou retirer


#les sets
a_set={"Margot","joe","arthur"}

int=[1,2,3,4]
print(int)
smooth=[3.14,7,-2+3j,'water',False,[1,2]]
long_smooth=len(smooth)
print(long_smooth)
print(smooth)
smooth[3][4]#donne dans le mot "water" la 5e lettre (4e index)
print (smooth[5][1])#va dans la 2e list a l'interieur et prend le 2e element
smooth[2:5]#ca ecrit du 2e element au 4e element sans prendre en compte le 5e
smooth[:4]#ca écrit tout jusqu'au 3e element 
smooth[1:]#ca écrit tt la liste except le 1er element

bg=[3.14,7,-2+3j,'water',False,[1,2],5,"Hello","Hi","1","e"]
bg[::2]#ca fait un pas de 2 en 2 , on ^rend que les éléments 1 sur 2
print(bg[-1])
print(bg[-2])
bg.pop(2)#retire l'élément à l'index 2
print(bg)


#exo1: faire la somme d'une série en utilisant une liste
n= int(input("Enter a value:"))
the_list=[]
for i in range (1,n+1):
    the_list.append(1/i)
    print(the_list)
Sn=sum(the_list)
print(f"The sum is {Sn}")

#ex
nat7= list(range(7))
print(nat7)
print(type(nat7))

#ex écrire un elist fin cree une list
print("This programm will createa list from real numeric data ")
nval=int(input("Enter nb of values:"))
llnum=[]
for i in range (nval):
    value=float(input("Enter a numeric value:"))
    llnum.append(value)
print(llnum)

#ex sépare la phras la ou ya un a 
line="Temperature is 298.15 K before combustion"
words=line.split('a')
print(words)

#ex sur mettre une temp dans une liste en sépare
ligne=input("Enter, in a single line and SEPARATED BY SPACES, the desired temp")
smooth_text=ligne.split()
print("List is now {}".format(smooth_text))
temp=[]
for element in smooth_text:
    value=float(element)
    temp.append(value)
    
print("The final list is {}".format(temp))

#ex
a=[1,3,5,7,11]
b=[13,17]
c=a+b
print ("First instruction print: {}".format (c))
b[0] = -1
d = []
for e in a:
  d.append (e+1)
print ("Second instruction print: {}". format (d))
d.append(b[0] + 1)
d.append(b[-1] + 1)
print ("Third instruction print: {}". format (d))
print ("Fourth instruction print: {}".format (d[-2:])) 
print ("Fifth instruction print: {}".format(d[:-1])) 
print ("Sixth instruction print: {}".format(d[1:4]))

#ex sur list des carrées des nb naturels
n=int(input("enter a value :"))
list_margot=[]
for i in range (1,n+1):
    list_margot.append(i**2)
print(list_margot)


#ex sur la liste des notes d'un exam
liste_name=[]
list_grade=[]
mean=0
number_of_student=int(input("Enter a number of student:"))
for i in range (1,number_of_student+1):
    name=input("Enter a name:")
    liste_name.append(name)
    grade=int(input("Enter the grade:"))
    list_grade.append(grade)
    mean=mean+grade
    print(name)
    print(grade)

print(liste_name)
print(list_grade)
average=mean/number_of_student
print("The average of the grade is {}".format(average))

num = int(input("Enter an integer value:"))
ndiv = 1
while ndiv<num:
    res = num // ndiv
    print("The integer division of {} by {} gives: {}".format(num, ndiv, res))
    ndiv = ndiv +1

print("We're done")
print("Total number of divisions : {}".format(ndiv))

#
nume = 1
ndive = 0

while nume>0 and nume<211:
    if nume%3==0:
        print(f"The number is {nume}")
        ndive = ndive + 1
    nume+=1

print("The number of iterations is : {}".format(ndive))

#
nat=0
sum=0
while nat<=10:
    sum=sum+nat
    nat=nat+1

print("The sum of the 10 first natural numbers is {}".format(sum))

#
i=0
sum =0
while i<10:
    yep = int(input("Enter a value:"))
    sum = sum +yep
    i=i+1
averg = sum//10
print("The average of the 10 numbers is : {}".format(averg))

#
i=0
a="*"
while i<=10:
    print(a)
    a=a+"*"
    i=i+1
print(a)

#marche pas
i=1
num = int(input("Enter a number"))
while i<=num:
    b=i+1
    fact=b*i
print(fact)

#factoriel

n = int(input("Enter the number:"))
f =n
r=1

while f!=0:
    r*=f
    f=-1
print("Factorial of:",n,"is",r)

#Break Statement

name='APagnan22n'
size = len(name)
i = 0
#iterate loop till the last character
while i < size:
    #break loop is current character is number
    if name[i].isdecimal():
        break;
    #print current character
    print(name[i], end=' ')
    i = i + 1
print("\nThe execution has stopped")

#example(skip the numbers)
name='Jessa29Roy'

size = len(name)
i=-1
while i< size-1:
    i=i+1
    if not name[i].isalpha():
        continue
    print(name[i], end =' ')

#repetitive structure

for i in range(3): #3 integers (0, 1, 2)
    print("Value of i: {}".format(i))

#example for
n = int(input("Enter the value of n :"))
for i in range(n):
    q_i =  i**2 #calculate square of i
    print(q_i) # write the value

#week 3
#i in range(n)  0 ...... n-1
#range(2,6)    2 3 4 5
#range(ni, nf, step)    ex :  range(2, 8, 2)   2 4 6 (with a step of 2)

n = int(input("Enter the value of n:"))
for i in range (1, n+1):
    q_i = i**2
    print(q_i)

#
n = int(input("Enter the value of n:"))
for i in range (1, n+1, 2):
    q_i = i**2
    print(q_i)

#Accumulator becarful start with 1 != 0

sum = 0
for i in range (6):
    sum = sum + 1
    print(f"The value of sum is in each iteration : {sum}")
print("The sum is valid {}".format(sum))

#fact
prod = 1
for i in range (1,6):
    prod = prod*i
    print(f"The partial sum is {prod}")

#loop in loop
for i in range (4):
    for j in range (3):
        print("i = {}, j = {}".format(i,j))

#ex1
sum = 0
val = int(input("Enter a value:"))
for i in range(val+1):
    sum = sum + i
print(f"The sum is {sum}")

#ex2
sum = 0
val = int(input("Enter a value:"))
for i in range(1, val+1):
    sum = sum + (i+1)/i**2
print(f"The sum is {sum}")

#ex3
sum = 1
val = int(input("Enter a value:"))
for i in range(1, val+1):
    sum = sum*i
print(f"The factorial is {sum}")

#ex4
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}{j}")

#ex5
for i in range(1,10):
    for j in range(1,10):
        if i!=j:
            print(f"{i}{j}")

#ex6 (triangular exercise)
a = int(input("Enter the number of triangular numbers you want:"))
for i in range(0, a+1):
    t=i*(i+1)/2
    print(t)

#ex7
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            print(f"{i}{j}{k}")

#ex8
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if(i+j+k==22):
                print(f"{i}{j}{k}")

#ex9
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if(i**3+j**3+k**3==(i*100+j*10+k)):
                print(f"{i}{j}{k}")

#ex10
n = int(input("Enter a value:"))
for i in range(1, n+1):
    if n%i==0:
        print(f"{i} is a divisor of {n}")

#ex11 (nombres impairs)
num = int(input("Enter a positive number"))
sum = 0
for i in range(0, num+1):
    odd_num = 2*i +1
    print(f"The odd number is {odd_num}")
    sum = sum + odd_num
print(f"The sum of the first {num} odd numbers is {sum}")

#week 4

#mon ex marche pas
i = 0
sum = 0
listab=[]
val = int(input("Enter a value:"))
while val !="":
    listab.append(val)
    for i in range(val+1):
        sum=sum+i
        print(f"La somme des valeurs est : {sum}")
    mean=sum//len(listab)
    print(f"La moyenne est : {mean}")

#la correction en photo
value=input("En")

#ex2 marche toujours pas
n = input("Enter a name:")
listn = []
while n !=' ':
    listn.append(n)
    n = str(n)
    n = input("Enter a name")
    print(f" Hi \n{n}")
    print(f"Hi {listn}")


#ex3 correction photo
el = ['H', 'C', 'N', 'O', 'S']
masses = [1, 12, 14, 16, 32]  
mass = 0

for i in range(len(el)):
    Natoms = int(input("Nombre d'atomes de l'élément " + el[i] + ": "))
    mass += Natoms * masses[i]

print("La masse totale est :", mass)


#ex4
result = 0
listY=[]
n = int(input("Enter the maximum degree of the polynomial:"))
for i in range(0,n+1):
    coef = input("Enter the coefficient of the polynomial:")
    listY.append(coef)
    print(listY)
x = input("Enter the value of x:")
for i in range(0, n+1):
    result = result + coef[i]*(x**i)

#ex4 correction photo

#Def course
#exemple 1
def hf():
    print('hello world')
hf()

#exemple 2
def add(x,y):
    c=x+y
    print(c)
add(5,4)

#exemple 3
def func(a=11, b=2, c=10):
    print(f'a is{a} and b is {b} and c is {c}')
func(6,7)


#week4
#fucntion dictionnary

#{key : value
# }

#example1 on dictionnary

country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Rome",
    "England" : "London"
}
print(country_capitals)

#dictionnary is an immutable objects we can't change it values once declared
#key are immutable

my_dict = {1:"Hello", (1,2):"Hello Hi", 3:[1,2,3]}
print(my_dict)

#key can't be a list

country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Rome",
    "England" : "London"
}
print(len(country_capitals))

#creating a dictionnary
Dict = {}
print("Empty dictionary:")
print(Dict)

#dict() method
Dict = dict({1:'Geeks',2:'For',3:'Geeks'})
print("\nDictionary with the use of dict():")
print(Dict)

#Nested Dictionary (list in a list)
Dict = {1:'Geeks', 2:'For',
    3: {'A': 'Welcome', 'B':'To', 'C':'Geeks'}}
print(Dict)

#to access a value in the dictionary
country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Rome",
    "England" : "London"
}
print(country_capitals["United States"])

#same but with a nested
Dict = {1:'Geeks', 2:'For',
    3: {'A': 'Welcome', 'B':'To', 'C':'Geeks'}}
print(Dict[3]['A'])

#
Dict = {'Dict1': {1:'Geeks'}, 'Dict2':{'Name': 'For'}}

print(Dict['Dict1'])

#change a element in a dictionary
#key cannot be changed but values can

country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Naples",
    "England" : "London"
}

print(country_capitals)
country_capitals["Italy"] = "Rome"
print(country_capitals)

##Change a value in a list with using the position
#list = [0,5,2,1,3]
#list[3]=8

#add an item
country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Rome",
    "England" : "London"
}
print(country_capitals)
country_capitals["Germany"] = "Berlin"
print(country_capitals)

#Adding a dict in a nested dict
Dict[5] = {'Nested':{'1':'Life', '2':'Geeks'}}
print("\nAdding a nested key")
print(Dict)

#Delete item with del
del country_capitals["United States"]

#clear function
#country_capitals.clear()
##photo of != functions

#print key one by one
country_capitals = {
    "United States": "Whashington D.C",
    "Italy" : "Rome",
    "England" : "London"
}

for country in country_capitals:
    print(country)

#an other way
for country in country_capitals:
    capital = country_capitals(country)
    print(capital)

#
for keys, values in country_capitals.items():
    print(country_capitals.key())
    print(country_capitals.values())

#demo for all dictionary methods
dict1 = {1:"Python", 2:"Java", 3: "Ruby", 4: "Scala"}

#
dict2 = dict1.copy()
print(dict2)

dict1.clear()
print(dict1)

print(dict2.get(1))

#all cities in europe
cities = ('Paris','Athens','Madrid')

continent = 'Europe'

my_dict= dict.fromkeys(cities, continent)

print(my_dict)

#None
cities = ('Paris','Athens','Madrid')
my_dict= dict.fromkeys(cities)
print(my_dict)

#convert two list into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict =dict(zip(keys, values))
print(res_dict)

#merge two dictionaries into one

dict1 = {'Ten': 10, 'Twenty':20, 'Thirty':30}
dict2 = {'Thirty':30, 'Fourty':40,'Fifty':50}

dict1.update(dict2)
dict3 = {**dict1, **dict2}
print(dict3)

#exercise
employees = ['Kelly', 'Emma']
defaults = {"designation":'Developer',"salary":8000}

n_dict = dict.fromkeys(employees, defaults)

print(n_dict)

#Dictionary problem

Element = {'Hydrogen': 'H' , 'Helium': 'He', 'Lithium': 'Li', 'Beryllium': 'Be', 'Boron': 'B', 'Carbon': 'C', 'Nitrogen': 'N', 'Oxygen':'O', 'Fluorine': 'F', 'Neon': 'Ne'}
MeltingPoint = {14, 1, 453, 1560, 2349, 3915, 63, 54, 53, 25}
BoilingPoint = {20, 4, 1603, 2742, 4200, 3915, 77, 90, 85, 27}

dictF= dict.fromkeys(Element, MeltingPoint, BoilingPoint)

Sym = str(input("Enter a specific element via its symbol:"))
Temp = int(input("Enter a temperature (in Kelvin):"))

if Temp >=  BoilingPoint:
    print("The element is a gas.")
elif Temp< BoilingPoint and Temp> MeltingPoint:
    print("The element is a solid.")
elif Temp<=MeltingPoint:
    print("The element is a liquid.")
else:
    print("error")

#Dictionary problem without error

Element = {
    'H': ('Hydrogen', 14, 20),
    'He': ('Helium', 1, 4),
    'Li': ('Lithium', 453, 1603),
    'Be': ('Beryllium', 1560, 2742),
    'B': ('Boron', 2349, 4200),
    'C': ('Carbon', 3915, 3915),
    'N': ('Nitrogen', 63, 77),
    'O': ('Oxygen', 54, 90),
    'F': ('Fluorine', 53, 85),
    'Ne': ('Neon', 25, 27)
}

Sym = input("Enter a specific element via its symbol: ").strip()
Temp = int(input("Enter a temperature (in Kelvin): "))

if Sym in Element:
    element_info = Element[Sym]
    name, melting_point, boiling_point = element_info

    if Temp >= boiling_point:
        print(f"{name} is a gas at {Temp} K.")
    elif Temp < boiling_point and Temp > melting_point:
        print(f"{name} is a solid at {Temp} K.")
    elif Temp <= melting_point:
        print(f"{name} is a liquid at {Temp} K.")
else:
    print("Element not found in the dictionary.")


#ex2

Bank = {
    'ANZ' : (2.3, 4.1),
    'Bank of Australia' : (0.1, 5),
    'Commonwealth Bank' : (3.5, 3.8),
    'Westpac' : (3.7, 3.7)
}

B = input("Enter your bank's name:").strip()
Y = int(input("Enter the price of your mortgage:"))
Z = int(input("Enter the numbers of years you will own this mortgage:"))

if B in Bank:
    bank_info = Bank[B]
    Rate12, Rate3 = bank_info

    mg_calcul = 2*Y*(Rate12/100) + Z*Y*(Rate3/100)

print(mg_calcul)


#Week5 : def function

def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



#example
def f(*kids):
  print("The youngest child is " + kids[2])

f("Emil", "Tobias", "Linus")


#Keyword Arguments (Dictionary)

def my_function(child3, child2, child1):
    print("The youngest child is" + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #3 dictionarys

#** is for 2 arguments

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Resfnes")

#* the input can be a tuple, list, number but not a dictionary|| ** input can be dicitionary

def my(fname = "luis", lname ="xyz"):
  print(fname +" "+lname)

my("Emil") #"luis" will be not considerate like delete by the input but if I return my() without an input it will write "luis"

#pass Statement is for no error

#Return the max

a=int(input("Enter a value:"))
b=int(input("Enter another value:"))

def max(a, b):
  if a>b:
    print(f"The biggest number is {a}.")
  elif a==b:
    print(f"Numbers are equals.")
  else:
    print(f"The biggest number is {b}")
    
max(a, b)


#try/except
#This block will test the expected error to occur


#ex
try:
    pass
except Exception:
    pass
    
try:
    num = int(input("Enter a number :"))
    if (num%2)==0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))
except ValueError as e:
    print("Try a proper number.")
except Exception:
    print("Error")

#ex

try: 
    num = int(input("Enter a number:"))
except ValueError as e:
    print(e)
else:
    if(num%2)==0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))

#ex

while True:
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("{0} is Even".format(num))
        else:
            print("{0} is Odd".format(num))
        break  # Sortir de la boucle si l'entrée est valide
    except ValueError as error:
        print(error)
        print("Try a proper number.")

#week 5
import numpy as np
np.max()
np.min()

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0, 8.0,7.0],[6.0,5.0,4.0]])
print(b)

#get dimension

a.ndim

#get shape

b.shape

#get type

a.dtype

#get size

a.itemsize

#get bytes

a.nbytes

a.size

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get a specific element [r, c]
a[1, 5]

#get a specific row
a[0,:]

#get a specific column
a[:,2]

#startindex:endindex:stepsize
a[0, 1: -1:2] #0 première ligne

#
a[1, 5] = 20

a[:,2] =  [1,2]
print(a)

#All às matrix
np.zeros((2,3))

#All 1s matrix

np.ones((4,2,2), )

#Week 6

import matplotlib.pyplot as plt
import numpy as np
#%matplolib inline



x=np.linspace(-2,2,101)
y=x**2
print(x)

plt.plot(x,y)
plt.show()


x = np.linspace(0,3*np.pi,500)

plt.plot(x, np.sin(x**2)) 
plt.title('A simple chirp')



x=np.linspace(-2,2,101)
y=x**2

plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 2.5)
plt.title("Chart Title")
plt.plot(x, y)
plt.show()


x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y)
y2 = x**4
plt.plot(x, y2)
plt.show()


x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x, y, label = "x^2")
y2 = x**4
plt.plot(x, y2, label = "x^4")
plt.legend()
plt.show()


x=np.linspace(-2,2,11)
plt.xlabel("x")
plt.ylabel("f(x)")
y2=x**2
plt.plot(x, y2, 'g',label = "x**2")
y3 = x**3
plt.plot(x, y3, 'ro', label = "x**3")
y4=x**4
plt.plot(x, y4, 'b.', label='x**4')
plt.legend()
plt.show()



x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x, y, 'g',label = "x**2")
y2 = x**4
plt.plot(x, y2, 'b.', label='x**4')
#plt.savefig("fig1.png")
plt.legend()
#plt.savefig("fig2.png")
plt.show()
plt.savefig("fig3.png")

#Ex1

Num = int(input("How many number os points to draw ? : "))
x = np.linspace(-1, 1, Num)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x, y, label ="cos(2*pi*x)")
plt.title("2pix")
plt.legend()
plt.savefig("cos2pix.png")
plt.show()



#Ex2

Num = int(input("How many number os points to draw ? : "))
x = np.linspace(-1, 1, Num)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x, y, label ="cos(2πx)")
plt.title("2πx")
y2=np.sin(2*np.pi*x)
plt.plot(x, y2, label ="sin(2πx)")
plt.title("sin2(2πx)")
plt.legend()
plt.savefig("trigonometric.png")
plt.show()



#Ex3

a = True
while a:
    
    try:

        Num = int(input("How many number os points to draw ? : "))
        
    except ValueError as error:
        
        print(error)
        print("Try a proper number.")  
        
    else:
        
        x = np.linspace(0, 4, Num)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
        plt.plot(x, y, label ="sin(πx)sin(20πx)e^(-x)")
        plt.title("sin(πx)sin(20πx)e^(-x)")
        plt.legend()
        plt.savefig("sin(πx)sin(20πx)e^(-x).png")
        plt.show()
        a=False
        


#Ex4


R = 0.08206
Iso = int(input("How many isothermes : "))
Num = int(input("How many number of points  : "))

for i in range(0, Iso):
      
    Temp= int(input("Enter Temperatures : "))
    Vm= np.linspace(2,10,Num)
    plt.xlabel("Molar volume")
    plt.ylabel("Pressure atm")
    p=(R*Temp)/Vm
    plt.plot(Vm, p)
    plt.title("Isotherm")
    plt.legend()
    plt.savefig("isotherm.png")
    plt.show()
    

#Ex111
'''
x1 = int(input("Enter x value : "))
x0 = int(input("Enter x0 value : "))
Num = int(input("How many number of points  : "))

x=np.linspace(-2,2,Num)
plt.xlabel("x")
plt.ylabel("f(x)")
y=(np.exp(-((x1-x0)**2)/(2*(s**2))/(np.sqrt(2*np.pi)))
plt.plot(x,y)
plt.legend()
plt.show()
'''
#exo1

n=int(input("Enter the number of point for the function: "))

x=np.linspace(0,3,n)

plt.xlabel("x")
plt.ylabel("f(x)")
y=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y,label='sin(3pix)e^(-x)')
y2=np.exp(-x)
plt.plot(x,y2,label='e^-x')
plt.title("sin(3pix)e-x and e-x")
plt.legend()
plt.show()

#exo2

xo=int(input("Enter xo: "))
s=float(input("Enter s: "))
d=int(input("Enter the number of point for the function: "))
f=int(input("Enter the number of point for the function: "))
n=int(input("Enter the number of point for the function: "))
x=np.linspace(d,f,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=(1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - xo) / s)**2)
plt.plot(x,y)
plt.title("Fonctioin de gauss")
plt.legend()
plt.show()

#exo3

n = int(input("How many?"))
for i in range (0,n):
    x = np.linspace(-1,1,100)
    s = float(input("s"))
    x0 = float(input("x0"))
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*((x-x0)**2)/(s**2))
    a = input("line : ")
    nom = input("name ? ")
    plt.plot(x,y,a,label = nom)

plt.title("Gaus")
plt.legend()
plt.show()

#Week 7 or 8 ?

name = "names"

f_name = open("names.txt")
for name in f_name:
    name = name.strip() # No space between the != output of files
    print(f"Hello {name}")
 
#Loop to return name wanted (specific character)

f_name = open("names.txt")
for name in f_name:
    if "a" in name: #If there is an a the name will be printed
        name = name.strip() 
        print(f"Hello {name}")
     
#Opening a file

f = open("oklm.txt", "r")#reading
f = open("oklm.txt", "w")#writing
f = open("oklm.txt", "a")#appending
f = open("oklm.txt", "r+")#reading + writing
    
print(f.name)
print(f.mode)
f.close()


#Writing

fnames = open("names.txt")
for name in fnames:
    print(name)

fnames=open("names.txtn", "w")
for name in fnames: 
    print(name)


#Reading Files (context Manager)
with open("oklm.txt", "r") as f:
    pass


with open("oklm.txt", "r") as f:
    #Small Files:
    f_contents = f.read()#read the file line per line
    print(f_contents)

    
with open("oklm.txt", "r") as f:
    #With the extra lines
    f_contents = f.readline()#one line at the time (here line 1)
    print(f_contents)
    f_contents = f.readline()#one line at the time (here line 2)
    print(f_contents)    

with open("oklm.txt", "r") as f:
    #With the extra lines
    f_contents = f.readline()
    print(f_contents, end = '')#print a blank line after this one
   

#Writing Files
##The error:

with open("oklm.txt", "w") as f:   
    f.write("Oklm")
 
   
#
with open("oklm.txt", "w") as f:   
    f.write("hello world")
    f.seek(5)
    f.write("--") 

   
#
with open("oklm.txt", "w") as f:
    val ='names'
    val1 = 10
    val2 = 'niamh'
    f.write(val+ ' '+val1+val2)
    f.seek(0)
    f.write("Oklm")
    f.seek(6)
    f.write('z')



