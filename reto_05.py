"""
Usaremos este script para enseñar Python a principiantes.
El script es un ejemplo de lectura de números de un archivo en Python.

El problema es:
Para todos los enteros entre 1 y 99 (incluidos ambos):
# Leer la entrada 3, 5 y 99 del archivo de entrada
# Imprimir fizz para múltiplos de 3
# Imprimir buzz para múltiplos de 5
# Imprimir fizzbuzz para múltiplos de 3 y 5
"""

def fizzbuzz(max_num):
    
    three_mul = 'fizz'
    five_mul = 'buzz'
    with open('myfile.txt','r') as fi:
        print('i have created')
        num1 = int(fi.readline())   
        num2= int(fi.readline())        
        max_num = int(fi.readline())
         
    for i in range(1,max_num):
        if i%num1==0 and i%num2==0:
            print(i,three_mul+five_mul)
        elif i%num1==0:
            print(i,three_mul)
        elif i%num2==0:
            print(i,five_mul)
        else:
            print("x")

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)