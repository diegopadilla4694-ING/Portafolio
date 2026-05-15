import random 

def lista_project(num_random_1, num_random_2, input_range):

      lista = [random.randint(num_random_1, num_random_2) for _ in range(input_range)]
      print(lista)


      new_lista = [sum(lista), max(lista), min(lista)]
      print(new_lista)


      count = 0
      for num in new_lista:
        count += num
    
      print(count)
    
try:
    
    num_random_1 = int(input("Ingrese un numero entero por favor: "))
    num_random_2 = int(input("Ingrese un numero entero por favor: "))
    input_range = int(input("Ingrese un numero entero por favor: "))

    lista_project(num_random_1, num_random_2, input_range)

except ValueError:
    
    print("ERROR SOLO NUMEROS ENTEROS POR FAVOR")
    



