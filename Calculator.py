#Simple calculator 
 
def Add(a,b):
  return(a+b)

def Sub(a,b):
  return(a-b)
  
def Mul(a,b):
  return(a*b)
  
def Div(a,b):
  return(a/b)

print("Enter operation\n 1.Addition\n 2.Substraction\n 3.Mulltiplication\n 4.Division\n")

choice=int(input("please enter your choice 1,2,3,4:"))

if choice!=1 and choice!=2 and choice!=3 and choice!=4:
  print("Enter valid choice!")

else:

  num_1=float(input("Enter first number"))
  num_2=float(input("Enter second number"))
  
  if choice==1:
    print(num_1,"+",num_2,"=",Add(num_1,num_2))
  
  elif choice==2:
    print(num_1,"-",num_2,"=",Sub(num_1,num_2))
  
  elif choice==3:
    print(num_1,"*",num_2,"=",Mul(num_1,num_2))
  
  elif choice==4:
    print(num_1,"/",num_2,"=",Div(num_1,num_2))
  
  else:
    print("Invalid Operation")
  
