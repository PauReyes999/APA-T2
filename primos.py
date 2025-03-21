"""
Pau Reyes Boix
>>> esPrimo(5)
True
"""

from collections import Counter 
def esPrimo(num):
    """"
    Devuelve true si el numero es primo, False si no lo es."
    
    Pruebas unitarias:
    >>> for numero in range (2, 10);"
    ...     print (esPrimo(numero))
    True"
    "True"
    "False"
    "True"
    "False"
    "True"
    "False
    """
    if num < 2:
        return False
    for i in range (2,num-1):
        if num % i == 0:
            return False
    return True

def primos(numero):
    """"
    Genera una tupla con los números primos menores que el número dado"
    
    >>>  primos(100)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 87)

    """
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """
    Descompon un número en sus factores primos
    >>> print(descompon(120))
    (2, 2, 2, 3, 5)

    >>> print(descompon(315))
    (3, 3, 5, 7)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //=divisor
        divisor += 1
    return tuple(factores)

def mcd(numero1, numero2):
   """
   Calcula el MCD de dos numeros

   >>>  mcd(10,15)
   5
   """

   factores1 = Counter(descompon(numero1))
   factores2 = Counter(descompon(numero2))
   factores_comunes = factores1 & factores2  # Intersección de factores primos con menor exponente
   mcd_valor = 1
   for factor, exponente in factores_comunes.items():
        mcd_valor *= factor ** exponente
   return mcd_valor


def mcm(numero1, numero2):
    """
    Calcula el mínimo común múltiplo (MCM) de dos números a partir de su descomposición en factores primos.

   >>> mcm(3,4)
   12
    """
    # Descomponer ambos números en factores primos
    factores1 = Counter(descompon(numero2))
    factores2 = Counter(descompon(numero2))

    # Calcular la unión de los factores con el mayor exponente
    factores_unidos = factores1.copy()

    # Para cada factor en el segundo número
    for factor, exponente in factores2.items():
        if factor in factores_unidos:
            # Tomamos el mayor exponente entre los dos números
            factores_unidos[factor] = max(factores_unidos[factor], exponente)
        else:
            # Si el factor no está en el primero, lo agregamos con su exponente
            factores_unidos[factor] = exponente

    # Calcular el MCM
    mcm_valor = 1
    for factor, exponente in factores_unidos.items():
        mcm_valor *= factor ** exponente  # Multiplicamos cada factor elevado a su exponente

    return mcm_valor

def mcmN(*numeros):
    """
    Calcula el mínimo común múltiplo (MCM) de un número arbitrario de argumentos.
 
   >>> mcmN(42,60, 70, 63)
   1260

    """
    # Comenzamos con el primer número
    mcm_resultado = numeros[0]

    # Iteramos sobre el resto de los números
    for numero in numeros[1:]:
        mcm_resultado = mcm(mcm_resultado, numero)  # Calculamos el MCM entre el resultado actual y el siguiente número

    return mcm_resultado

def mcdN(*numeros):
    """
    Calcula el máximo común divisor (MCD) de un número arbitrario de argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    # Comenzamos con el primer número
    mcd_resultado = numeros[0]

    # Iteramos sobre el resto de los números
    for numero in numeros[1:]:
        mcd_resultado = mcd(mcd_resultado, numero)  # Calculamos el MCD entre el resultado actual y el siguiente número

    return mcd_resultado