'''Crear un programa que solicite 4 notas obtenidas de un curso de
programacion y mediante una condicion simple mostar si aprobó o desaprobó
la materia (tener en cuenta que la nota promedio para aprobar en 6)'''
'''''
not1 = float(input("Ingrese su nota 1 -> "))
not2 = float(input("\nIngrese su nota 2 -> "))
not3 = float(input("\nIngrese su nota 3 -> "))
not4 = float(input("\nIngrese su nota 4 -> "))

promedio = (not1 + not2 + not3 + not4) / 4

if promedio >= 6: 
    print(f"Usted aprobó la materia con un promedio de {round (promedio, 3.72)}")
   # print("Usted aprobo la meteria con un promedio de {}".format(promedio))
   # print("Usted aprobo la meteria con un promedio de", )
   
else: 
    print("\nNo aprobo el curso, su promedio de ", round (promedio, 2))
    
print("\nFin del programa")
'''''

fruta = input("Ingrese su fruta -> ").lower()

if fruta == "sandia":
    print("Usted eligio sandia")
