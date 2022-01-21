# Assignment3
#BANOTH LIKITHA ASSIGNMENT 3

#function 1

def datatypes(string,bool,list,int,float,set,tuple):
   return f"The required string  is {string}\nThe required bool is {bool}\nThe required list is {list}\nThe required int is {int}\nThe required float is {float}\nThe required set is {set}\nThe required tuple is {tuple}\n"

print(datatypes('data',bool(5),list(range(5,10)),int(45.8),float('33'),set(range(200,1000,100)),tuple(2*[5,10,15,20]))) 

#function 2

def func2(x):
    return f"{x}\n{(list(x.keys()))}\n{list((x.values()))}"

fruits={'colour':'fruit','red':'apple , watermelon','yellow':'banana , mango ','green':'grapes',}

animals={'colour':'animal','red':'ant','yellow':'lion','green':'grasshoper','orange':'tiger','black':'pig','white':'cow'}

print(func2(fruits))
print(func2(animals))

#function 3


def listf(t):
   return f"{list(t)}"

a=int(input('Enter first int number:'))
b=int(input('Enter second int number:'))
t=(a,b)
print(listf(t))

x=float(input('Enter first float number:'))
y=float(input('Enter second float number:'))
f=(x,y)
print(listf(f))

p=(100,300)
print('Required list of two numbers is',listf(p))

n1=50
n2=80
q=(n1,n2)
print('Required list of two numbers is',listf(q))
