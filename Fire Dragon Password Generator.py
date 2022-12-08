from string import ascii_letters, digits, punctuation
from random import choice
from tkinter import *


def password_generator():
    from random import randint
    #define o tamanho da senha (entre 8 a 30 dígitos)
    UserChoicePasswordLength = randint(8, 30) 





    password_user = ""
    #Retorna para a variável "letters" todas as letras do alfabeto, incluindo letras maiúsculas
    letters = ascii_letters
    #Retorna números de 0 a 9 para a variável "numbers"
    numbers = digits
    #Retorna todos os sinais de pontuação possíveis para a variável "pontuation"
    pontuation = punctuation
    #Variável "all_digits" está rebendo todos os dígitos possíveis de uma senha
    all_digits = letters + numbers + pontuation

    #define os dígitos da senha
    for digit in range(0, UserChoicePasswordLength):
        password_user += choice(all_digits)


    result = f'Generated password: {password_user}'

    #"text" da variável "generated_password" está recebendo a senha gerada
    generated_password["text"] = result

#cria a interface pro código
janela = Tk()

#Adiciona um título para a janela
janela.title("Fire Dragon Password Generator")
#Define o tamanho da janeja
janela.geometry("390x180")

#Adiciona uma mensagem na janela 
screen_text = Label(janela, text="Welcome to the Fire Dragon Password Generator!")

#define a posição da mensagem
screen_text.grid(column=0, row=1, pady=3)

#Também adiciona uma mensagem na janela
screen_text2 = Label(janela, text="Get start by clicking the button below to generate your password:")

#Define a posição da mensagem
screen_text2.grid(column=0, row=2, pady=4)

#Cria um botão para gerar a senha
button = Button(janela, text="Generate password", command=password_generator)

#Define a posição do botão
button.grid(column=0, row=3, pady=10)

#Senha gerada
generated_password = Label(janela, text="")

#Posição da senha gerada
generated_password.grid(column=0, row=4, pady=30)

#Permite que a janela fique aberta até o usuário fechá-la
janela.mainloop()

