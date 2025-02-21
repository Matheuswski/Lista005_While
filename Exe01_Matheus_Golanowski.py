#Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
print("Matheus Golanowski")
to = 0
while to <= 50:
    numero = int(input("Digite um número: "))
    to += numero
    if to > 50:
        print("O total é  {}".format(to))
        break