funcionario = []
n_funcionario = 1
import json
import os

def clear_os():
    os.system('cls')

def menu() :
    option = int(input('''
[1] - Cadastrar Funcionário
[2] - Consultar Funcionário
[3] - Editar Funcionário
[4] - Sair do programa
'''))
    clear_os()
    return option

def cadastra_funcionario() :
    funcionario_nome = input('Digite o nome do funcionario: ')
    funcionario_cep = input('Digite o cep do funcionario: ')
    funcionario_telefone = input('Digite o telefone do funcionario: ')

    Funcionarios_dados = {"funcionario_nome": funcionario_nome, "funcionario_cep":funcionario_cep, "funcionario_telefone":funcionario_telefone}
    file = open("Funcionarios.json", "r", encoding='utf-8')

    data = file.read()
    data = json.loads(data)
    data.append(Funcionarios_dados)

    file = open("Funcionarios.json", "w+", encoding='utf-8')
    data = json.dumps(data)
    file.write(data)
    file.close()
    
    print(data)
    print('Funcionario adicionado')

    clear_os()

def mostrar_funcionario() :
    file = open("Funcionarios.json", "r", encoding='utf-8')
    data = file.read()
    funcionarios = json.loads(data)
    for funcionario in funcionarios:
      print(f'''
      Nome: {funcionario['funcionario_nome']}
      Cep: {funcionario['funcionario_cep']}
      Telefone: {funcionario['funcionario_telefone']}''')

    
def programa() :

    while True:
        option = menu()

        if option == 1 :
            cadastra_funcionario()
        if option == 2 :
            mostrar_funcionario()
        if option == 4 :
          break

programa()