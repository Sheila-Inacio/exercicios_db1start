def mask_cpf(cpf: str): 
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}' 

def __capitalize_word(word: str): 
    return f'{word[0].upper()}{word[1:]}' 

def capitalize(text: str): 
    words = text.split(' ') 

    result = '' 
    for word in words: 

        result += f'{__capitalize_word(word)} ' 

    return result.rstrip() 