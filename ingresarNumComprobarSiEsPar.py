num = None; #Declaro variable y le asigno None còmo valor.
num = input("Ingrese un número por favor: ")#Ahora pido al usuario que ingrese el dato requerido y lo guardo en num
if  str. isdigit(num) == True: #Voy a evaluar si el dato ingresado es un entero mediante el mètodo de Python màs eficiente ya que es el que menos tiempo tarda en ejecutarse. Si es un entero ingresamos al condicional.Puede ocurrìr que el usuarui NO ingrese un entero sino otra cosa.
    print("Gracias por ingresar un nùmero entero...")# Mostramos en pantalla confirmando al usuario que ingresò un entero.       
    pasoEntero = int(num)#convertimos el tipo de dato string a cadena y lo guardamos en la variable "pasoEntero", ya estamos en capacidad de manipular el dato de tipo entero.
    if pasoEntero % 2 == 0:#Evaluamos si el nùmero ingresado es par, para eso comprobamos si el resto de su divisiòn por 2 es igual a cero
        print(f"El {pasoEntero} es par.")#Si lo es, entonces sabemos que es par
    elif pasoEntero % 2 != 0:#Si su resto es diferente de 0 sabemos que es impar
        print(f"El {pasoEntero} es impar.")# Mostramos en pantalla dicho resultado y terminamos el programa.
elif "." in num:#Mediante el punto podemos comprobar si el dato ingresado es un flotante.
    print("Usted ha insertado un valor con decimal, no es válido, será convertido a entero.") # Aclaramos que ingresò un flotante y que serà necesario eliminar su parte decimal.   
    convierto = float(num)  #Con la funciòn nativa de Python "float()" convertimos un dato a tipo flotante, por default lo que viene de un input en Python es como cadena, esa conversiòn la guardo en otra variable.
    print("Ahora el tipo de dato cadena pasò a ser: " ,type(convierto))#Informamos que ya cambio su tipo de dato.
    convierto = int(convierto)#Nuevamente de tipo flotante lo convierto pero esta vez a entero, ya siendo entero podrà ser evaluado, es una conversiòn escalonada, aunque este proceso se puede acortar y no tiene porquè ser de este modo.
    print("Ahora pasò a ser del tipo: ",type(convierto))#Informamos de la conversiòn o paso a entero.
    print(f"Genial, hemos eliminado su parte decimal y ya es entero el {convierto}, vamos a comprobar ahora si es par o impar...")#Muestro en pantalla que las conversiones finalizaron con èxito.
    num = convierto #Una vez finalizada la operaciòn de conversiòn, cambio de variable el resultado de la operaciòn.Es no es obligatorio pero me puede permitir entender el còdigo màs fàcil si le damos nombres directos a cada variable o constante sobre su contenido.
    if num % 2 == 0:#Al ya estar en tipo entero el dato ingresado, se puede meter en un condicional y evaluarlo.
        print(f"El {num} es par.")#Muestro resultado
    elif num % 2 != 0:#
        print(f"El {num} es impar.")##Muestro resultado
    else:#
        print("error!!!")#    #Muestro resultado
elif num == "":#con las comillas vacìas se puede evaluar si el usuario dejò el campo sin ingresar nada.
    print("Error!, usted no puede dejar el campo en blanco, si o si debe ingresar un número entero.") #   Muestro en pantalla el error y termina el programa ahì.
elif num == "q" and "w" and "e" and "r" and "t" and "y" and "u" and "i" and "o" and "p" and "a" and "s" and "d" and "f" and "g" and "h" and "j" and "k" and "l" and "ñ" and "z" and "x" and "c" and "v" and "b" and "n" and "m" and "Q" and "W" and "E" and "R" and "T" and "Y" and "U" and "I" and "O" and "P" and "A" and "S" and "D" and "F" and "G" and "H" and "J" and "K" and "L" and "Ñ" and "Z" and "X" and "C" and "V" and "B" and "N" and "M"  or "q" + "w" + "e" + "r" + "t" + "y" + "u" + "i" + "o" + "p" + "a" + "s" + "d" + "f" + "g" + "h" + "j" + "k" + "l" + "ñ" + "z" + "x" + "c" + "v" + "b" + "n" + "m" + "Q" + "W" + "E" + "R" + "T" + "Y" + "U" + "I" + "O" + "P" + "A" + "S" + "D" + "F" + "G" + "H" + "J" + "K" + "L" + "Ñ" + "Z" + "X" + "C" + "V" + "B" + "N" + "M":#Caracteres comparados con un resultado negativo. Podemos comparar en un condicional los datos que consideramos una condiciòn.
            print(f"Error, usted ingresó: {num} y sólo debe ingresar números enteros en este programa, las cadenas de texto no son válidas y los caracteres tampoco.")# Muestro error y aclaro detalles.
else:
    print("Error, intente nuevamente.")
#num = input("Ingrese un nùmero: ")
#try:
  #  int(num)
 #   it_is = "Es correcto el ", num, "es entero."
#except ValueError:
 #   it_is = False

#print(it_is)
                   