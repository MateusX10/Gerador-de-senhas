import random
import string



def password_generator(len_pass=8):
    password_user = ""

    ascii_opitions = string.ascii_letters
    number_opitions = string.digits
    punt_opitions = string.punctuation
    opitions = ascii_opitions + number_opitions + punt_opitions
    
    for digit in range(0, len_pass):
        digit = random.choice(opitions)
        password_user += digit
    return password_user


while True:
    try:
        QuantidadeDeCaracteresNaSenha = int(input("Quantos dígitos terá a senha? "))    
    except (NameError, ValueError):
        print("\033[1;31mOpção inválida.Tente novamente.\033[m")

    except (KeyboardInterrupt):
        print("\n\033[1;31mEntrada de dados encerrada pelo usuário...\033[m")
        quit()
    else:
        if QuantidadeDeCaracteresNaSenha < 8:
            print("\033[1;33mOps!Parece que sua senha tem menos de 8 dígitos.\nPor favor, reconsidere uma senha com 8 dígitos ou superior!\033[m")
            continue
        break

password = password_generator(QuantidadeDeCaracteresNaSenha)

print(f'\033[1mSenha gerada: \033[1;32m{password}\033[m')