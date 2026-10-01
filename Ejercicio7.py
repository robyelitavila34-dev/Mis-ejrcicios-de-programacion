#Ejercicio 7 : Calcular IVA 

#cREANDO VARIABLES

precio_base = int(input("Precio del producto : \n"))

#caLculando IVA
IVA = precio_base * 0.19

#Precio + iva 
precio_final = precio_base + IVA

print(f"El precio final del producto con el IVA es {precio_final}")
