#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um segundo numero: "))
soma = numero1 + numero2
print("A soma dos numero é de: ",soma)
resposta = input("Voce deseja adicionar mais algum numero (s/n)")
while resposta == "s":
    numero = float(input("Digite outro numero: "))
    soma += numero
    resposta = input("Voce deseja adicionar mais algum numero (s/n)")
print("A soma dos numero é de: ",soma)