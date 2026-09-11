def new_line():
    print("\n")

#Getting input form the user
print("Getting input form the user")
new_line()
#code 1
print("Code 1")
name = input("What is your name:")
favorite_colour = input("What is your favorite colour:")
print(name    +   " likes "   +  favorite_colour)

new_line()

#code 2
print("Code 2")
name=input("name:")
age=input("age:")
address=input("address:")
print("My Name is:",name)
print("My age is:",age)
print("My address is:",address)

new_line()

#code 3
print("Code 3")
name=input("name:")
score=int(input("score:"))
department=input("department:")

print("My name is ",name)
print("My score is",score/10,"/10" )
print("My department is",department)
 
new_line()


#Casting
print("Casting")
new_line()

x=str("Archana")
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

new_line()

#Using Arithmetic Operators

print("Using Arithmetic Operators")
new_line()

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=a*b*c
e=a+b+c
f=d/e
print(f)

new_line()


#if else
print("if else")
new_line()
#code 1
print("Code 1") 
meghna=input()
if(meghna=="Died"):
    print("Surya meets Priya")
else:
    print("Surya weds Meghna")


new_line()

#code 2
print("Code 2")
mark=int(input("mark:"))
if(mark>35):
    print("Pass")
else:
    print("Fail")


new_line()

#code 3
print("Code 3")
income=int(input("Income:"))
if(income>7000):
    print("Scholarship is not available")
else:
    print("Scholarship is available")

new_line()

#code 4
print("Code 4")
x=int(input())
if(x%3==0 and x%5==0):
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")

new_line()

#code 5
print("Code 5")
x  =int(input())
if(x%2==0):
  print("Even")
else:
  print("Odd")


new_line()

#code 6
print("Code 6")
score=int(input("Score Percentage:"))
if(score>=70):
      name=input("Enter your name:")
      age=input("Enter your date of brith:")
      location=input("Enter your age:")
      print("You are eligible")
else:
      print("You are not eligible")

new_line()


#code 7
print("Code 7")
salary=int(input("Salary:"))
age=int(input("Age:"))
if(salary>=20000 or age<=25):
   loan=int(input("Loan:"))
   if(loan>50000):
      print("Maximum loan amount is 50000")
   else:
      print("You are eligible for loan")
else:
   print("You are not eligible for loan")


new_line()

#elif consept
print("elif consept")
new_line()
#code 1
print("Code 1")
score=int(input("Score:"))
if(score<35):
    print("Poor Student")
elif(score>35 and score<70):
    print("Average Student")
else:
    print("Good Student")
 

new_line()

#code 2
print("Code 2")
a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
      print(a+b)
elif(operation=="sub"):
      print(a-b)
elif(operation=="mul"):
      print(a*b)
elif(operation=="div"):
      print(a/b)
else:
      print("Invalid operation")
      
    
      
      
new_line()

#for loop

print("For Loop")
new_line()
#code 1
print("Code 1") 
for i in range(6):
    print(i)


new_line()

#code 2
print("Code 2")

for i in range(1,11):
    print(i,"*3=",i*3) 
    
new_line()

#code 3
print("Code 3")
for i in range(1,11,5):
        print(i)


new_line()

#code 4
print("Code 4")
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)


new_line()

#code 5
print("Code 5")
e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)


new_line()


#code 6

print("Code 6")
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)


new_line()

#code 7
print("Code 7")
sum=0
for i in range(1,6):
        sum=sum+i
print(sum)


new_line()

#code 8
print("Code 8")
a=[]
print("Enter 10 numbers:")
for i in range(5):
    num=int(input("Enter num "+str(i+1)))
    a.append(num)
print(a)


#Nested LOOP
print("Nested LOOP")
new_line()

#code 1
print("Code 1")

for i in range(1,8):
    print("\nWeek:", i)
    for j in range(1,3): 
       print("Day:",j)

new_line()
#code 2

print("Code 2")
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(j,end=" ")

new_line()

#code 3

print("Code 3")
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end=" ")

new_line()

#while loop
print("while loop")
new_line()
#code 1
print("Code 1")
i=0
while(i<5):
    print(i)
    i=i+1

#code 2
print("Code 2")
i=10
while(i<=200):
    print(i)
    i=i+10
    
#code 3
print("Code 3")

i=10
while(i>0):
   print(i,end=",")
   i=i-1

new_line()

#code 4
print("Code 4")

i=4
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)


#code 5