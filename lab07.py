def find_vogal(encrypted_message):
    '''Função que busca uma vogal. Por meio de um loop, ela verifica
    se o caractere é um dígito. Em caso positivo, ela verifica se é
    uma vogal. Em caso positivo novamente, ela retorna o índice do
    caractere na string e sai da função na primeira ocorrência.'''
    vogals = "aeiouAEIOU"
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            if encrypted_message[i] in vogals:
                vogal_value = encrypted_message.find(encrypted_message[i])
                return vogal_value
                break


def find_number(encrypted_message):
    '''Função que busca por um número. Por meio de um loop, ela verifica
    se o caractere é númerico. Em caso positivo, ela retorna o índice
    dele na string e sai da função na primeira ocorrência.'''
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isnumeric():
            number_value = encrypted_message.find(encrypted_message[i])
            return number_value
            break


def find_consonant(encrypted_message):
    '''Função que busca uma consoante. Por meio de um loop, ela verifica
    se o caractere é um dígito. Em caso positivo, ela verifica se é
    uma vogal. Em caso negativo, ela retorna o índice do caractere na
    string e sai da função na primeira ocorrência.'''
    vogals = "aeiouAEIOU"
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            if not encrypted_message[i] in vogals:
                consonant_value = encrypted_message.find(encrypted_message[i])
                return consonant_value
                break


def index(encrypted_message, first_character, second_character):
    '''Função que organiza as chamadas de caractere. Para cada cenário,
    ela chama a função ou artíficio necessário para encontrar o índice
    da primeira ocorrência do caractere inserido. No caso do segundo
    caractere, ela verifica os índices posteriores ao do primeiro.'''
    if first_character == "vogal":
        if second_character == "numero":
            first_value = find_vogal(encrypted_message)
            second_value = find_number(encrypted_message[first_value:]) + first_value
        elif second_character == "vogal":
            first_value = find_vogal(encrypted_message)
            second_value = find_vogal(encrypted_message[first_value:]) + first_value
        elif second_character == "consoante":
            first_value = find_vogal(encrypted_message)
            second_value = find_consonant(encrypted_message[first_value:]) + first_value
        else:
            first_value = find_vogal(encrypted_message)
            second_value = encrypted_message[first_value:].find(second_character) + first_value
    elif first_character == "numero":
        if second_character == "numero":
            first_value = find_number(encrypted_message)
            second_value = find_number(encrypted_message[first_value:]) + first_value
        elif second_character == "vogal":
            first_value = find_number(encrypted_message)
            second_value = find_vogal(encrypted_message[first_value:]) + first_value
        elif second_character == "consoante":
            first_value = find_number(encrypted_message)
            second_value = find_consonant(encrypted_message[first_value:]) + first_value
        else:
            first_value = find_number(encrypted_message)
            second_value = encrypted_message[first_value:].find(second_character) + first_value
    elif first_character == "consoante":
        if second_character == "numero":
            first_value = find_consonant(encrypted_message)
            second_value = find_number(encrypted_message[first_value:]) + first_value
        elif second_character == "vogal":
            first_value = find_consonant(encrypted_message)
            second_value = find_vogal(encrypted_message[first_value:]) + first_value
        elif second_character == "consoante":
            first_value = find_consonant(encrypted_message)
            second_value = find_consonant(encrypted_message[first_value:]) + first_value
        else:
            first_value = find_consonant(encrypted_message)
            second_value = encrypted_message[first_value:].find(second_character) + first_value
    else:
        if second_character == "numero":
            first_value = encrypted_message.find(first_character)
            second_value = find_number(encrypted_message[first_value:]) + first_value
        elif second_character == "vogal":
            first_value = encrypted_message.find(first_character)
            second_value = find_vogal(encrypted_message[first_value:]) + first_value
        elif second_character == "consoante":
            first_value = encrypted_message.find(first_character)
            second_value = find_consonant(encrypted_message[first_value:]) + first_value
        else:
            first_value = encrypted_message.find(first_character)
            second_value = encrypted_message[first_value:].find(second_character) + first_value
    return first_value, second_value


def find_key(operator, encrypted_message, first_character, second_character):
    '''Função que retorna a chave para decriptografia. Ela pega os dois
    valores do índice de cada caractere inserido e, mediante o operador
    posto, a função realiza o procedimento para o encontro da chave.
    A função retorna a chave no final.'''
    first_value, second_value = index(encrypted_message, first_character, second_character)
    if first_value >= 0 and second_value >= 0 and operator == "+":
        key = first_value + second_value
    elif first_value >= 0 and second_value >= 0 and operator == "-":
        key = first_value - second_value
    elif first_value >= 0 and second_value >= 0 and operator == "*":
        key = first_value * second_value
    return key


def decrypt(encrypted_message, key):
    '''Função que decriptografa o código. Com o valor da chave,
    por meio de um loop, ela encontra o valor do caractere codificado
    inserido e faz o procedimento matemático a fim de descobrir o
    valor do caractere decodificado para chamá-lo. Ela, entao, cria
    uma nova string com a mensagem decodificada e a retorna.'''
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        value = ((ord(encrypted_message[i]) - 32 + key) % 95) + 32
        new_letter = chr(value)
        decrypted_message += new_letter
    return decrypted_message


def main():
    operator = input()
    first_character = input()
    second_character = input()
    line_numb = int(input())
    encrypted_message_ = [input() for _ in range(line_numb)]
    encrypted_message = ""
    for i in range(len(encrypted_message_)):
        encrypted_message += encrypted_message_[i]
    key = find_key(operator, encrypted_message, first_character, second_character)
    print(key)
    for i in range(len(encrypted_message_)):
        decrypted_message = decrypt(encrypted_message_[i], key)
        print(decrypted_message)


if __name__ == "__main__":
    main()
