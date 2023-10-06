import math
#ingresar valores (float es para los numeros decimales)
a=float(input("ingresa valor de a: "))
b=float(input("ingresa de b: "))
c=float(input("ingresa de c: "))

#calcular discriminante (d)
d=b**2-4*a*c

#si el determinante es >0 (math.sqrt es la raiz cuadrada)
if d >0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("si el determinante es mayor que 0:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
#si el determinante es igual a 0 solo se obtiene una solucion
elif d ==0:
    x=-b/(2*a)
    print("si el determinante es igual que 0:")
    print(f"x1 = {x}")
#si el determinante es negativo se hace una solucion compleja
#(pr: parte real, pi: parte imaginaria) {complex se usa para representar numeros complejos}
else:
    pr= -b/(2*a)
    pi= math.sqrt(-d)/(2*a)
    s1 = complex(pr, pi)
    s2 = complex(pr, -pi)
    print("si el determinante es negativo:")
    print("x1 =", s1)
    print("x2 =", s2)

#para probar las tres posibilidades:
#>0 = a: 2 b: -5 c: 2
#=0 = a: 1 b: -4 c: 4
#-x = a: 3 b: 2  c: 5