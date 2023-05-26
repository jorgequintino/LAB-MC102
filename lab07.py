def find_vogal(encrypted_message: str):
    vogals = "aeiouAEIOU"
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            if encrypted_message[i] in vogals:
                f = encrypted_message.find(encrypted_message[i])
                return f
                break


def find_number(encrypted_message: str):
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isnumeric():
            e = encrypted_message.find(encrypted_message[i])
            return e
            break


def find_consonant(encrypted_message: str):
    vogals = "aeiouAEIOU"
    for i in range(len(encrypted_message)):
        if encrypted_message[i].isalpha():
            if not encrypted_message[i] in vogals:
                g = encrypted_message.find(encrypted_message[i])
                return g
                break


def index(encrypted_message, x, y):
    if x == "vogal":
        if y == "numero":
            c = find_vogal(encrypted_message)
            b = find_number(encrypted_message)
        elif y == "vogal":
            c = b = 0
        elif y == "consoante":
            c = find_vogal(encrypted_message)
            b = find_consonant(encrypted_message)
        else:
            c = find_vogal(encrypted_message)
            b = encrypted_message.find(y)
    elif x == "numero":
        if y == "numero":
            c = b = 0
        elif y == "vogal":
            c = find_number(encrypted_message)
            b = find_vogal(encrypted_message)
        elif y == "consoante":
            c = find_number(encrypted_message)
            b = find_consonant(encrypted_message)
        else:
            c = find_number(encrypted_message)
            b = encrypted_message.find(y)
    elif x == "consoante":
        if y == "numero":
            c = find_consonant(encrypted_message)
            b = find_number(encrypted_message)
        elif y == "vogal":
            c = find_consonant(encrypted_message)
            b = find_vogal(encrypted_message)
        elif y == "consoante":
            c = find_consonant(encrypted_message)
            b = find_consonant(encrypted_message)
        else:
            c = find_consonant(encrypted_message)
            b = encrypted_message.find(y)
    else:
        if y == "numero":
            c = encrypted_message.find(x)
            b = find_number(encrypted_message)
        elif y == "vogal":
            c = encrypted_message.find(x)
            b = find_vogal(encrypted_message)
        elif y == "consoante":
            c = encrypted_message.find(x)
            b = find_consonant(encrypted_message)
        else:
            c = encrypted_message.find(x)
            b = encrypted_message.find(y)
    return c, b


def key(operator, encrypted_message, x, y):
    c, b = index(encrypted_message, x, y)
    if c >= 0 and b >= 0 and operator == "+":
        key = c + b
    elif c >= 0 and b >= 0 and operator == "-":
        key = c - b
    elif c >= 0 and b >= 0 and operator == "*":
        key = c * b
    return key


def descriptografar(encrypted_message, k):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        value = ord(encrypted_message[i]) + k
        if value > 126:
            value = value - 126 + 31
        new_letter = chr(value)
        decrypted_message += new_letter
    return decrypted_message


def main():
    operator = input()
    x = input()
    y = input()
    line_numb = int(input())
    encrypted_message_ = [input() for _ in range(line_numb)]
    encrypted_message = ""
    for i in range(len(encrypted_message_)):
        encrypted_message += encrypted_message_[i]
    k = key(operator, encrypted_message, x, y)
    print(k)
    for i in range(len(encrypted_message_)):
        decrypted_message = descriptografar(encrypted_message_[i], k)
        print(decrypted_message)


if __name__ == "__main__":
    main()
