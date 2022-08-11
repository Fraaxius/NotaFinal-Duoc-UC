status1 = "REPROBADO"
status2 = "APROBADO"

print ("Hola! Bienvenid@ a la calculadora de notas de DuocUC\n")
notapre=float(input("Ingrese su nota de presentación: \n"))
notaexam=float(input("Ingrese su nota de examen: \n"))

print ("\nBasado en los actuales porcentajes de notas (ya sea 60% de presentación y 40% de examen...)")
notafinal1 = notapre * 0.6
notafinal2 = notaexam * 0.4
notafinal = notafinal1 + notafinal2

if notafinal < 3.95:
    print (f"Tu nota es", round(notafinal), f"tu situación es {status1}\n")

elif notafinal >= 4.0:
    print (f"Tu nota es {notafinal}, tu situación es {status2}\n")

print ("Gracias por usar el programa <3\n")

print ('''
Hecho por Francisco Sánchez M.
Estudiante de Informática Biomédica en Duoc UC.
''')
