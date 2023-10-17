'''
module system
'''

from time import sleep
from modules.controller import produtos, vendedores
import uuid

def header():
    print('=='*20)
    print(f'{"-"*10}{"System 1.0":^20}{"-"*10} ')
    print('=='*20)


def footer():
    print('Encerrando em ', end="")
    for c in range(3,0,-1):
        sleep(1/2)
        print(f"{c}",end=" ")
    print(f'\n{"="*10}{"FIM":.^20}{"="*10}')

def menu():
    opcao = 1
    while opcao != 3:
        print('* Produtos   (1)')
        print('* Vendedores (2)')
        print('* Sair       (3)')
        opcao = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
        while opcao not in [1,2,3]:
            print('Opção invalida! Digite novamente.')
            opcao = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
        if opcao == 1:
            produto_entity = produtos.new_produtos()
            op = 1
            while op != 0:
                print('* Voltar             (0)')
                print('* Cadastrar Produto  (1)')
                print('* Listar Produtos    (2)')
                print('* Buscar Produto     (3)')
                print('* Editar Produto     (4)')
                print('* Remover Produto    (5)')
                op = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
                while op not in [0,1,2,3,4,5]:
                    print('Opção invalida! Digite novamente.')
                    op = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
                if op == 1:
                    id = str(uuid.uuid4())
                    nome = input('Nome: ')
                    preco = float(input('Preço: '))
                    quantidade = int(input('Quantidade: '))
                    descricao = input('Descrição: ')
                    produto_entity.cadastrar(id, nome, preco, quantidade, descricao)
                elif op == 2:
                    dto = produto_entity.listar()
                    print('=='*20)
                    for obj in dto:
                        print('--'*20)
                        for key, value in obj.items():
                            print(f'{key}:{value}')
                    print('=='*20)
                elif op == 3:
                    id = input("id: ")
                    obj = produto_entity.buscar(id)
                    print('=='*20)
                    for key, value in obj.items():
                        print(f'{key}:{value}')
                    print('=='*20)
                elif op == 4:
                    id = input("id: ")
                    nome = input('Nome: ')
                    preco = float(input('Preço: '))
                    quantidade = int(input('Quantidade: '))
                    descricao = input('Descrição: ')
                    produto_entity.editar(id, nome, preco, quantidade, descricao)
                elif op == 5:
                    id = input("id: ")
                    produto_entity.remover(id)

        elif opcao == 2:
             vendedores_entity = vendedores.new_Vendedores()
             op = 1
             while op != 0:
                print('* Voltar              (0)')
                print('* Cadastrar Vendedor  (1)')
                print('* Listar Vendedor     (2)')
                print('* Buscar Vendedor     (3)')
                print('* Editar Vendedor     (4)')
                print('* Remover Vendedor    (5)')
                op = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
                while op not in [0,1,2,3,4,5]:
                    print('Opção invalida! Digite novamente.')
                    op = int(input('Qual opção deseja selecionar? (APENAS NÚMEROS):'))
                if op == 1:
                    id = str(uuid.uuid4())
                    nome = input('Nome: ')
                    data_nascimento = float(input("Data de nascimento: [02012006] sem '/' "))
                    vendedores_entity.cadastrar(id, nome, data_nascimento)
                elif op == 2:
                    dto = vendedores_entity.listar()
                    print('=='*20)
                    for obj in dto:
                        print('--'*20)
                        for key, value in obj.items():
                            print(f'{key}:{value}')
                    print('=='*20)
                elif op == 3:
                    id = input("id: ")
                    obj = vendedores_entity.buscar(id)
                    print('=='*20)
                    for key, value in obj.items():
                        print(f'{key}:{value}')
                    print('=='*20)
                elif op == 4:
                    id = input("id: ")
                    nome = input('Nome: ')
                    data_nascimento = float(input("Data de nascimento: [02012006] sem '/' "))
                    vendedores_entity.editar(id, nome, data_nascimento)
                elif op == 5:
                    id = input("id: ")
                    vendedores_entity.remover(id)
