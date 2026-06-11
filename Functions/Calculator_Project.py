def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2



operations_calculator = {
  "+" : add,
  "-" : subtract,
  "*" : multiply, 
  "/" : divide
}

def calculator():
    Booleano = True
    n1 = float(input("What is the first number?: "))


    while Booleano:

        for symbol in operations_calculator:
            print(symbol)

        operation_symbol = input("Pick an operation ")
        n2 = float(input("What is the second number?: "))
        total = operations_calculator[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {total}")

        button = input(f"Type 'yes' to continue calculating with {total}, or type 'no' to start a new calculo").lower()

        if button == "yes":
            n1 = button
        else:
            Booleano = False
            print("\n" * 20)

calculator()
