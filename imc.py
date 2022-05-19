
peso = float(input("Ingrese el peso correspondiente [kg]: "))
estatura= float(input("Ingrese la altura correspondiente [m] :"))

#Calcular el IMC 

IMC = round(peso/(estatura**2),2)


#Resultado
print ("El índice de masa corporal es:"+ str(IMC))
 