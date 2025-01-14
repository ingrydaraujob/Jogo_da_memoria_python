import tkinter as tk
from tkinter import messagebox
import random

#configurações do jogo 
num_linha = 4
num_colunas = 4
cartao_size_w = 10
cartao_size_h = 5
cores_cartao = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
cor_fundo = "#343a40"
cor_letra = "#ffffff"
font_style = ("arial",12,"bold")
max_tentativas = 25

#grade aleatória de cores para as cartas os cartoes
def create_card_grid():
    cores = cores_cartao *2
    random.shuffle(cores)
    grid = []

    for i in range (num_linha):
        linha = []
        for i in range(num_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

#lidar com cliques do jogador nos cartões 
def card_clicked(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao["bg"]
    if cor == "black":
        cartao["bg"] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()

#verificar se os dois cartoes revelados sao iguais 
def check_match():
    carta1 , carta2 = cartao_revelado
    if carta1["bg"] == carta2["bg"]:
        carta1.after(1000, carta1.destroy)
        carta2.after(1000, carta2.destroy)
        cartas_correspondentes.extend([carta1, carta2])
        check_win()
    else:
        carta1.after(1000, lambda:carta1.config(bg="black"))
        carta2.after(1000, lambda:carta2.config(bg="black"))
    cartao_revelado.clear()
    update_score()



#verificar se o jogador ganhou 
def check_win():
    if len(cartas_correspondentes) == num_linha * num_colunas:
        messagebox.showinfo("parabens! ", "voce ganhou o jogo!!")
        janela.quit()

#atualizar a potuação e verificar se o jogador perdeu p jogo 
def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text="Tentativas: {}/{} ".format(numero_tentativas, max_tentativas))
    if numero_tentativas >= max_tentativas:
        messagebox.showinfo("fim de jogo", "voce perdeu o jogo")
        janela.quit()


#interface principal
janela = tk.Tk()
janela.title("Jogo da memoria")
janela.configure(bg=cor_fundo)


#grade de cartões
grid = create_card_grid()
cartoes = []
cartao_revelado = []
cartas_correspondentes = []
numero_tentativas = 0


for linha in range (num_linha):
    linha_de_cartoes = []
    for col in range(num_colunas):
        cartao = tk.Button(janela, width=cartao_size_w, height=cartao_size_h, bg="black", relief= tk.RAISED, bd=3, command=lambda r=linha, c=col: card_clicked(r,c))
        cartao.grid(row=linha, column= col, padx= 5 , pady= 5 )
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)





#personalisando botão
button_style = {"activebackground ": "#f8f9fa" , "font":font_style, "fg":cor_letra}
janela.option_add("Button", button_style) 

#numeros de tentativas
label_tentativas = tk.Label(janela, text="Tentativas:{}/{}".format(numero_tentativas, max_tentativas),fg=cor_letra, bg = cor_fundo , font=font_style)
label_tentativas.grid(row=num_linha , column= num_colunas, padx=10 , pady=10 )


janela.mainloop()