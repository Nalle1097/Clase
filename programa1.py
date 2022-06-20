n = True #VARIABLE EN VERDADERO
while n: #Ciclo
    print("Escoge una opcion")
    print("opcion A . Pares")
    print("opcion B . Impares")
    print("opcion C . Suma a 100")
    print("opcion D . Salir")
    op = input() #Variable por teclado
    if op == "A" or op =="a":
        print("La cantidad de numeros a sumar")
        m = int(input()) #parametro necesario
        p = 1
        suma=0
        while p <=m:
            print("Dame el numero",p)
            num = int(input()) #pido el numero al usuario...
            if num % 2 == 0: #variable de numero pares
                suma = suma + num #Sumar los numeros 
                p = p + 1
                print("La suma de los numeros es",suma)

                
    if op == "B" or op =="b":
        print("La cantidad de numeros a sumar")
        m = int(input()) #parametro necesario
        p = 1
        suma=0
        while p <=m:
            print("Dame el numero",p)
            num = int(input()) #pido el numero al usuario...
            if num % 2 == 1: #variable de numero pares
                suma = suma + num #Sumar los numeros 
                p = p + 1
                print("La suma de los numeros es",suma)

                
    if op == "C" or op == "c":
        w =True
        suma= 0
        while w:
            print("Dame un numero")
            num = int(input())
            suma = suma + num
            print("La suma es",suma)
            if suma >=100:
                w = False
            print("Se detuvo el programa")