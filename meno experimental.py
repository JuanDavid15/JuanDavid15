print("Algoritmo experimental de menu, intento #1
while x = False
    print("")



    match opcion:
    case 1:
        
    case 2:
        print("Algoritmo experimental, tiende al error")
	print(" ")
	for Int in range(5):
	    x1=False
	    St=0;
	    print (f"Hola emplead@ {Int}")
	    print("Hombre (M) y Mujer (F)")
	    G=input("digite su genero: ")
	    N=input("Digite su primer nombre: ")
            N1=input("Digite su segundo nombre: ")
            Ap=input("Digite su primer apellido: ")
            Ap1=input("Digite su segundo apellido: ")
	    if G="M" or G="m":
		print("Hola Señor",N,"",Ap)
	    else:
		print("Hola Señora",N,"",Ap)
                Ced=input("Por favor ingresa tu cedula: ")
	    if (Ced<10000000 or Ced>9999999999):
		St+=1;
		print("Cedula no valida")
	    else:
		if (Ced>=10000000 or Ced<=9999999999) and ST=0:
		    x1=True;
		if x1=True:
			for Int in range(3)
			    if G="M" o G="m" Entonces
                                print(f"Empleado {N}, digite la fecha de nacimiento en formato de DD/MM/AAAA");
			    else
				print(f"Empleada {N}, digite la fecha de nacimiento en formato de DD/MM/AAAA";
			    D=input("Digite el dia (DD): ")
			    M=input("Digite el mes (MM): ")
			    A=input("Digite el año (AA): ")
			    Va="Verdadero";
			    if A<1900 or A>2100:
				Va="Falso"
			    if M<1 or M>12:
				Va="Falso"
			    if Va="Verdadero" Entonces
				    Si M=1 O M=3 O M=5 O M=7 O M=8 O M=10 O M=12 Entonces
						MaxD<-31;
					FinSi
					Si M=4 O M=6 O M=9 O M=11 Entonces
						MaxD<-30;
					FinSi
					Si M=2 Entonces
						Si (A MOD 4=0 Y A MOD 100<>0) O (A MOD 400=0) Entonces
							MaxD<-29;
						Sino
							MaxD<-28;
						FinSi
					FinSi
					Si D<1 O D>MaxD Entonces
						Va<-"Falso";
					FinSi
				FinSi
				Si Va="Verdadero" Entonces
					Escribir "La fecha ",D,"/",M,"/",A," es válida.";
					Int<-3;  
				Sino
					Si Int<3 Entonces
						Escribir "Fecha inválida, intente de nuevo.";
					Sino
						Escribir "Ha superado el límite de intentos.";
					FinSi
				FinSi
				Para Int <- 1 Hasta 3 Hacer
					Escribir "Intento ",Int,": Ingrese un correo electrónico:";
					Leer correo;
					Va<-"Falso";
					Para i <- 1 Hasta Longitud(correo) Hacer
						Si Subcadena(correo, i, i) = "@" Entonces
							Va<-"Verdadero";
						FinSi
					FinPara
					Si Va="Verdadero" Entonces
						Escribir "Correo válido: ", correo;
						Int<-3;  
					Sino
						Si Int<3 Entonces
							Escribir "Correo inválido, intente de nuevo.";
						Sino
							Escribir "Ha superado el límite de intentos.";
						FinSi
					FinSi
				FinPara
			FinPara
		FinSi
	FinPara
FinProceso
    case 3:
        
    case 4:
        
    case 5:
        
    case _:
