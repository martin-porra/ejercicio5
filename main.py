import csv
from clase import  estudiante
import os

def menu():
 os.system('cls')
 print ("Selecciona una opción")
 print ("\t1 - Ingresar un año y división, y liste nombre y porcentaje de inasistencias")
 print ("\t2 - Modificar la cantidad máxima de inasistencias permitidas")

if __name__ == '__main__':
 lista = []
 archivo = open('estudiantes.txt')
 reader = csv.reader(archivo, delimiter=(','))
 for fila in reader:
  objeto = estudiante(fila[0], fila[1], fila[2], fila[3])
  lista.append(objeto)
 archivo.close()
 print('lista cargada')
 a = True
 while a == True:
   menu()
   opcion = input()
   if opcion == '1':
    print('ingrese año y division a buscar ejemplo "6to" "A" ')
    r = input()
    b = input()
    print('Alumno            Porcentaje ')
    for x in range(0, len(lista)):
     if lista[x].año() == r and lista[x].division() == b:
         if int(lista[x].inas()) > int(estudiante.max()):
           print(str(lista[x].nombre()) + '       ' + str(lista[x].porcentaje()))
   elif opcion == '2':
      print('ingrese numero de inasistencia a modificar')
      m = input()
      estudiante.modi(m)
      print('el numero maximo de inasistencias ahora es ' + str(estudiante.max()))
   else:
    a = False
    print('opcion incorrecta')
 print('programa terminado')