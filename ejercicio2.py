numero_notas=10
suma=0
i=1
while (i <= numero_notas):
    nota=float(input(f"ingrese la nota numero {i}: "))
    suma=suma+nota
    i+=1
prom = suma / numero_notas
print("el promedio de notas es:", prom)