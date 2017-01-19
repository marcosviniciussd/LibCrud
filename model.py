# -*- coding: UTF-8 -*-

'Classe padrão para perfis de usuario'
class perfil(object):
    
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print("NOME: ", self.nome)
        print("TELEFONE: ", self.telefone)
        print("EMPRESA: ", self.empresa)

perfil1 = perfil("Marcos", "99476547", "Caelum")

