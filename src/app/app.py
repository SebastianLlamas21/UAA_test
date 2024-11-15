from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        if (a == 0 or b == 0):
            return 0
        else:
            return a / b
            
            

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False.
        """
        for numero in lista:
            if numero > 1:
                for i in range(2, numero):
                    if (numero % i) == 0:
                        break
                else:
                    return True
        return False
        
            
        

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        if(inicio != fin):
            cantidad_pares = 0
            for numero in range(inicio, fin + 1):
                if(numero % 2 == 0):
                    cantidad_pares += 1
            return cantidad_pares
        else:
            return 0
        

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        maximo = None
        for numero in lista:
            if numero % multiplo == 0:
                if maximo is None or numero > maximo:
                    maximo = numero
        return maximo

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        palabra = palabra.replace(" ", "").lower()
        return palabra == palabra[::-1]

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(numero):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        if(numero > 0):
            suma = 0
            for n in range (1, numero):
                if(n%2 != 0):
                    suma += n
            return suma     
        else:
            return 0  
                       

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        conjunto = set(lista)
        return len(lista) == len(conjunto)

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        factorial = 1
        for n in range(1, numero+1):
           factorial *= n
         
        return factorial   


    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        cadena = cadena.upper()
        cant_vocales = 0
        for letra in cadena:
            if(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
                cant_vocales +=1
        return cant_vocales    

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        if len(lista) < 2:
            return None
    
        unicos = set(lista)
        
        if len(unicos) < 2:
            return None
        
        ordenados = sorted(unicos, reverse=True)
        return ordenados[1]
        

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        if n <= 0:
            return []
    
        fibonacci = [0, 1]
        
        for i in range(2, n):
            siguiente = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(siguiente)
        
        return fibonacci[:n]
