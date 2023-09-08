while True: 
    try: 
        x = int(input("Digite algo: ")) 
        break 
    except ValueError: 
        print("Valor inválido - Tente novamente") 