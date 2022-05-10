#4. Realizar las cuatro operaciones básicas 
# (Suma, Resta, Multiplicación, División)

Op = input("Ingrese operación: ")

try:
    if('+' in Op):
        # corta la operacion por el signo (4+5 en ['4', '5'])
        Op = Op.split('+')
        # float porque los elementos en 
        print(f"El resultado es {float(Op[0]) + float(Op[1])}")

    elif('-' in Op):
        Op = Op.split('-')
        print(f"El resultado es {float(Op[0]) - float(Op[1])}")

    elif('*' in Op):
        Op = Op.split('*')
        print(f"El resultado es {float(Op[0]) * float(Op[1])}")

    elif('/' in Op):
        Op = Op.split('/')
        print(f"El resultado es {float(Op[0]) / float(Op[1])}")
        
except ValueError:
    print("Por favor, escriba un valor numérico válido")

except ZeroDivisionError:
            print("Error, división entre 0")