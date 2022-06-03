numero1=int(input("Inserte su primer medida: "))
numero2=int(input("Inserte su segunda medida: "))
numero3=int(input("Inserte su tercera medida (si su figura no requiere esta medida introduzca el numero 1): "))
numero4=int(input("Inserte su cuarta medida (si no requiere esta medida introduzca el numero 1): "))

resultado1=numero1*numero2/numero3*numero4
resultado2=numero1*numero2*numero3*numero4
resultado3=numero1*numero2*numero3/numero4
print("El area de un triangulo con las medidas dadas es de: ", resultado1)
print("El area de un rectangulo con las medidad dadas es de: ", resultado2)
print("El area de un pentagono con las medidas dadas es de: ", resultado3)