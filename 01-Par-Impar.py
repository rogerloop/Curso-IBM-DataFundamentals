# Python App para comprobar si par o impar
# Al dividir por 2, con la función módulo , si resto es 0, par, si no, impar
# Autor : Roger Defez
# Fecha : 2022025-03-28

def par_impar(num):
    """
    Función que determina si un número es par o impar.
    :param num: Número a evaluar.
    :return: True si es par, False si es impar.
    """
    if num % 2 == 0:
        return True
    else:
        return False
    
# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Enter a number: "))
    if par_impar(numero):
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")        

