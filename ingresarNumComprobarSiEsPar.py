num = input("Ingrese un número por favor: ")
if "." in num:
    print("Usted ha insertado un valor con decimal, no es válido, será convertido a entero.")    
    convierto = float(num)  
    print(type(convierto))
    convierto = int(convierto)
    print(type(convierto))
    print(f"Genial, hemos eliminado su parte decimal y ya es entero el {convierto}, vamos a comprobar ahora si es par o impar...")
    num = convierto 
    if num % 2 == 0:
        print(f"El {num} es par.")
    elif num % 2 != 0:
        print(f"El {num} es impar.")
    else:
        print("error!!!")    
elif num == "":
    print("Error!, usted no puede dejar el campo en blanco, si o si debe ingresar un número entero.")    
elif num == "q" and "w" and "e" and "r" and "t" and "y" and "u" and "i" and "o" and "p" and "a" and "s" and "d" and "f" and "g" and "h" and "j" and "k" and "l" and "ñ" and "z" and "x" and "c" and "v" and "b" and "n" and "m" and "Q" and "W" and "E" and "R" and "T" and "Y" and "U" and "I" and "O" and "P" and "A" and "S" and "D" and "F" and "G" and "H" and "J" and "K" and "L" and "Ñ" and "Z" and "X" and "C" and "V" and "B" and "N" and "M"  or "q" + "w" + "e" + "r" + "t" + "y" + "u" + "i" + "o" + "p" + "a" + "s" + "d" + "f" + "g" + "h" + "j" + "k" + "l" + "ñ" + "z" + "x" + "c" + "v" + "b" + "n" + "m" + "Q" + "W" + "E" + "R" + "T" + "Y" + "U" + "I" + "O" + "P" + "A" + "S" + "D" + "F" + "G" + "H" + "J" + "K" + "L" + "Ñ" + "Z" + "X" + "C" + "V" + "B" + "N" + "M":
            print(f"Error, usted ingresó: {num} y sólo debe ingresar números enteros en este programa, las cadenas de texto no son válidas y los caracteres tampoco.")
if "1" and "2" and "3" in num:
    print("Es un numero entero")        
    pasoEntero = int(num)
    if pasoEntero % 2 == 0:
        print(f"El {pasoEntero} es par.")
    elif pasoEntero % 2 != 0:
        print(f"El {pasoEntero} es impar.")    
                   