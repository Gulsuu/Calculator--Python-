from artcalculator import logo

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2 

#Create a dictionary.
dic={}
dic["+"]=add #call functions
dic["-"]=subtract
dic["*"]=multiply
dic["/"]=divide

def calculator():
  print(logo)
  print("WELCOME TO THE CALCULATOR!")

  num1=float(input("What's the first number:"))
  for key in dic:
      print(key)
      
  shouldcontinue=True
  while shouldcontinue==True:
    symbol=input("Which operation do you want press one above:")
    num2=float(input("What's the next number:"))
    calculationfunc=dic[symbol]
    answer=calculationfunc(num1,num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.").lower()=="y":
      num1=answer
    else:
      shouldcontinue=False
      calculator() #to start a new calculation (recursion)

calculator()
