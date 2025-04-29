class Solution(object):
    def search(numerobuscado,nums):
        
        list = nums
        numerobuscado = int(numerobuscado)
        posicion = -1
        for i in range(len(list)):
            if list[i] == numerobuscado:
                posicion = i
                print (f"El numero {numerobuscado} esta en la posicion: ", i)
                break
            elif list[i] != numerobuscado and i == len(list)-1:
                print (f"Resultados: {posicion}")
                break

        return list            
    
    numeroBuscado = input("ingrese el numero objetivo:")
    nums = [1, 2, 3, 4, 5, 0, 7, 8, 9, 10]
    search (numeroBuscado,nums)
        