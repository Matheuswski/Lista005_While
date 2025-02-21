#Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.
print("Matheus Golanowski")
cont = 0
while cont < 5:
    numero = int(input("Digite um número: "))
    cont += 1
    ulti_num = numero
print("O ultimo numero que vc digitou foi {}".format(ulti_num))
    

