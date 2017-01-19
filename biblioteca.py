# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print("[ CADASTRANDO NOMES ]")
    print("Digite o nome: ")
    nome = input()
    nomes.append(nome)

def listar(nomes):
    print("[ LISTANDO NOMES ]")
    for nome in nomes:
        print(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
         print()
         print("*********************************************************")
         print("1 - CADASTRAR")
         print("2 - VISUALIZAR")
         print("0 - SAIR")
         print("*********************************************************")
         print()

         escolha = input()

         if(escolha == '1'):
             cadastrar(nomes)

         if(escolha == '2'):
            listar(nomes)

menu()
             

    