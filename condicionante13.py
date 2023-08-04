data = input(" Digite uma data: ")
dia = int(data[0 : 2])
mes = int(data[3 : 5])
ano = int(data[6 : 9])

if len(data) == 10 and data[2] == "/" and data[5] == "/" and dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0:
    print("Data válida ")    
else: 
    print("Data inválida ")    
