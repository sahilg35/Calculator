def add (n1,n2):
  return n1+n2

def subtract (n1,n2):
  return n1-n2

def multiply (n1,n2):
  return n1*n2

def divide (n1,n2):
  if n2 == 0:
    return "Invalid input"
  else:
    return n1/n2

operations = {
  "+": add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

from art import logo

def calculation():
  print(logo)
  is_continue = False
  n1 = float(input("What is your first number? "))
  
  for symbols in operations:
    print(symbols)
  
  
  while not is_continue:
    ops = input("Pick an opeation?: ")
    n2 = float(input("What is your next number? "))
    symbol = operations[ops]
    answer = symbol(n1,n2)
    print(f"{n1} {ops} {n2}= {answer}")
    
    cont = input(f"Type 'y' to continue calculating with {answer},or type 'n' to start a new calculation: ").lower()
    if cont == "y":
      n1 = answer
    else:
      is_continue = False
      calculation()


calculation()
    