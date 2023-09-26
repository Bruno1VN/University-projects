import os.path as path
import datetime

class piloto:  
    registro_do_piloto = ""
    nome = ""
    dia = ''
    mes = ''
    ano = ""
    sexo = ""
    curso_de_especializacao = ""
    email = ""
    telefone = ""

class voo:
    voo_numero = ""
    origem = ''
    destino = ""
    distancia = ""
    tempo_medio = ""
    aeronave = ""
    escala = ""

class viagem:
    voo_numero = ""
    nome = ""
    registro = ''
    saida = ""
    hora_saida = ""
    chegada = ""
    hora_chegada = ""
    ocorrencia = ""

def menu():
    #Função que apresenta o menu principal e retorna um valor escolhido pelo usuario 
    print("**********************")
    print("Submenu de Pilotos.....1")
    print("Submenu de Voos........2")
    print("Submenu de Viagens.....3")
    print("Submenu de Relatórios..4")
    print("Salvar arquivos........5")
    print("Sair...................6")
    opcao = input("---> ")
    return opcao

def menu_pilotos():
    #Função que apresenta o menu de pilotos e retorna um valor escolhido pelo usuario
    print("********PILOTOS***********")
    print("Listar cadastros.1")
    print("Listar nomes.....2")
    print("Incluir .........3")
    print("Alterar .........4")
    print("Excluir .........5")
    print("Sair.............6")
    opcao = input("---> ")
    return opcao

def menu_voos():
    #Função que apresenta o menu voos e retorna um valor escolhido pelo usuario
    print("***********VOOS***********")
    print("Listar cadastros.1")
    print("Listar voos......2")
    print("Incluir .........3")
    print("Alterar .........4")
    print("Excluir .........5")
    print("Sair.............6")
    opcao = input("---> ")
    return opcao

def menu_viagens():
    #Função que apresenta o menu viagens e retorna um valor escolhido pelo usuario
    print("***********VIAGENS***********")
    print("Listar cadastros.............1")
    print("Listar numero das viagens....2")
    print("Incluir .....................3")
    print("Alterar .....................4")
    print("Excluir .....................5")
    print("Sair.........................6")
    opcao = input("---> ")
    return opcao

def menu_relatorios():
    #Função que apresenta o menu relatorios e retorna um valor escolhido pelo usuario
    print("***********RELATÓRIOS***********")
    print("Pilotos acima de X anos.............1")
    print("Escalas em X cidades................2")
    print("Viagems entre os dias X e Y.........3")
    print("Sair................................4")
    opcao = input("---> ")
    return opcao
  
def existe_arquivo(endereco):
  if path.exists(endereco):
    return True
  else:
    return False

def verifica_piloto(registro, lista_pilotos):
    verificador = False
    i = 0
    while i < len(lista_pilotos): # Verifica se o valor informado já consta em outro cadastro
          if registro == lista_pilotos[i].registro_do_piloto:
              verificador = True
          i += 1
    return verificador

def cadastro_piloto(lista_pilotos):
    #Função de cadastro das informaçoes do piloto
    p = piloto() 
    p.registro_do_piloto = input("informe o registro do piloto: ")
    if verifica_piloto(p.registro_do_piloto, lista_pilotos) == False:    # prossegue com o cadastro caso o registro seja valido
        p.nome = input("Informe o nome do piloto: ")
        p.dia = str(input("Informe o dia de nascimento: "))
        p.mes = str(input("Informe o mes de nascimento: "))
        p.ano = str(input("Informe o ano de nascimento: "))
        p.sexo = str(input("Informe o sexo do piloto: "))
        p.curso_de_especializacao = str(input("informe o curso de especialização: "))
        p.email = []
        p.email.append(input("informe o e-mail(s): "))
        mail = True
        while mail == True: # verifica se o usuario deseja inserir mais de um email
            pgt = (input("Deseja adicionar um novo email (S/N): "))
            if  pgt == "S" or pgt == "s":
                p.email.append(input("Digite mais um e-mail: "))
            else:
                mail = False

        p.telefone = []
        p.telefone.append(input("informe o telefone(s): "))
        tel = True
        while tel == True: # verifica se o usuario deseja inserir mais de um telefone
            pgt = (input("Deseja adicionar um novo telefone (S/N): "))
            if  pgt == "S" or pgt == "s":
                p.telefone.append(input("Digite mais um telefone: "))
            else:
                tel = False
        lista_pilotos.append(p)
        print("Fim das informações do piloto. \n")
    else:
        print('Já existe um piloto com esse registro cadastrado. \n')

def cria_arquivo_piloto(lista_pilotos, lista_dados_pilotos):
    if existe_arquivo("arquivo_piloto.txt"):
        arq = open("arquivo_piloto.txt", "a")
    else:
        arq = open('arquivo_piloto.txt', 'w')
    i = 0
    verificador_dados_piloto(lista_dados_pilotos)
    while i < len(lista_pilotos):
            p = lista_pilotos[i]
            verificador = False
            j = 0
            while j < len(lista_dados_pilotos): # Verifica se o valor informado já consta em outro cadastro no arquivo
                if p.registro_do_piloto == lista_dados_pilotos[j][0]:
                    verificador = True
                j += 1
            if verificador == False:
                arq.write(p.registro_do_piloto)
                arq.write(';')
                arq.write(p.nome)
                arq.write(';')
                arq.write(p.dia)
                arq.write(';')
                arq.write(p.mes)
                arq.write(';')
                arq.write(p.ano)
                arq.write(';')    
                arq.write(p.sexo)
                arq.write(';')
                arq.write(p.curso_de_especializacao)
                arq.write(';')
                i = 0
                while i < len(p.email):
                    arq.write(p.email[i])
                    arq.write(';')
                    i += 1
                i = 0
                while i < len(p.telefone):
                    arq.write(p.telefone[i])
                    if i < len(p.telefone) - 1:
                        arq.write(';')
                    i += 1
                arq.write('\n')     
            i = i + 1
    arq.close()

def listar_piloto(p):
    #Função que apresenta as informações cadastradas
    print("Registro do piloto:",p.registro_do_piloto)
    print("Nome: ",p.nome)
    print("Nascimento: ",p.dia,'/',p.mes,'/',p.ano)
    print("Sexo: ",p.sexo)
    print("Curso de especialização: ",p.curso_de_especializacao)
    print("E-mail(s): ", end='')
    i = 0
    while i < len(p.email): # formata a apresentação dos emails
        print(p.email[i])
        i += 1
    print("Telefone(s): ", end='')
    i = 0
    while i < len(p.telefone): # formata a apresentação dos telefones
        print(p.telefone[i])
        i += 1
 
def imprimir_cadastros_piloto(lista_pilotos):
    #Função que imprime todos os pilotos cadastrados
    if len(lista_pilotos) > 0:
        print("Lista de pilotos")
        i = 0
        while i < len(lista_pilotos):
            listar_piloto(lista_pilotos[i])
            print("\n")
            i += 1
    else:
        print('Não há pilotos cadastrados \n')  

def imprime_registro_piloto(lista_pilotos):
    #função que apresenta os nomes dos pilotos 
    if len(lista_pilotos) > 0:
        i = 0
        while i < len(lista_pilotos):
            print(f'{i + 1} - Piloto: ', lista_pilotos[i].nome,f' registro: {lista_pilotos[i].registro_do_piloto}')
            print("\n")
            i += 1
        return True
    else:
        print('Não há pilotos cadastrados \n')
        return False
      
def imprimir_pilotos(lista_pilotos):
  #Função que permite apresentar o cadastro de algum piloto especifico
    if imprime_registro_piloto(lista_pilotos) == True:
        op = int(input('Digite o numero de um piloto para mostar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_pilotos):
            listar_piloto(lista_pilotos[op - 1])   

def excluir_piloto(lista_pilotos):
    #função que exclui um cadastro a ser escolhido pelo usuário
    if imprime_registro_piloto(lista_pilotos) == True:
        op = int(input('Digite o numero de um piloto para excluir seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_pilotos):
            del lista_pilotos[op - 1]
            print('Piloto excluido. \n')

def alterar_piloto(lista_pilotos):
    #função que permite alterar alguma informação com base na escolha do usuário
    if imprime_registro_piloto(lista_pilotos) == True:
        op = int(input('Digite o numero de um piloto para alterar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_pilotos): # define um layout com as opções
            listar_piloto(lista_pilotos[op - 1])
            print("Registro do piloto:......1")
            print("Nome:....................2")
            print("Dia......................3")
            print("Mês:.....................4")
            print("Ano:.....................5")
            print("Sexo:....................6")
            print("Curso de especialização:.7")
            print("E-mail(s):...............8")
            print("Telefone(s):.............9")

            alt = int(input('Utilize o indice para escolher qual informação será alterada: '))
            if alt == 1:
                registro = input("informe o registro do piloto: ") 
                
                if verifica_piloto(registro, lista_pilotos) == False:
                    lista_pilotos[op - 1].registro_do_piloto = registro
                else:
                    print('Já existe um piloto com esse registro cadastrado. \n')

            elif alt == 2:
                lista_pilotos[op - 1].nome = input("Informe o nome do piloto: ")
            elif alt == 3:
                lista_pilotos[op - 1].dia = str(input("Informe o dia de nascimento: "))
            elif alt == 4:
                lista_pilotos[op - 1].mes = str(input("Informe o mes de mês de nascimento: "))  
            elif alt == 5:
                lista_pilotos[op - 1].ano = str(input("Informe o ano de nascimento: "))
            elif alt == 6:
                lista_pilotos[op - 1].sexo = str(input("Informe o sexo do piloto: "))
            elif alt == 7:
                lista_pilotos[op - 1].curso_de_especializacao = str(input("informe o curso de especialização: "))
            elif alt == 8:
                lista_pilotos[op - 1].email = []
                lista_pilotos[op - 1].email.append(input("informe o e-mail(s): "))
                mail = True
                while mail == True:
                    pgt = (input("Deseja adicionar um novo email (S/N): "))
                    if  pgt == "S" or pgt == "s":
                        lista_pilotos[op - 1].email.append(input("Digite mais um e-mail: "))
                    else:
                        mail = False
            elif alt == 9:
                lista_pilotos[op - 1].telefone = []
                lista_pilotos[op - 1].telefone.append(input("informe o telefone(s): "))
                tel = True
                while tel == True:
                    pgt = (input("Deseja adicionar um novo telefone (S/N): "))
                    if  pgt == "S" or pgt == "s":
                        lista_pilotos[op - 1].telefone.append(input("Digite mais um telefone: "))
                    else:
                        tel = False           
            else:
                print('Opção inexistente.')
    else:
        print('Não há pilotos cadastrados \n')

def verifica_num_voo(registro, lista_voo):
    verificador = False
    i = 0
    while i < len(lista_voo): # Verifica se o valor informado já consta em outro cadastro
          if registro == lista_voo[i].voo_numero:
              verificador = True
          i += 1
    return verificador

def cria_arquivo_voo(lista_voo,lista_dados_voo):
    if existe_arquivo("arquivo_voo.txt"):
        arq = open("arquivo_voo.txt", "a")
    else:
        arq = open('arquivo_voo.txt', 'w') 
    i = 0
    verificador_dados_voo(lista_dados_voo)
    while i < len(lista_voo):
            p = lista_voo[i]
            verificador = False
            j = 0
            while j < len(lista_dados_voo): # Verifica se o valor informado já consta em outro cadastro no arquivo
                if p.voo_numero == lista_dados_voo[j][0]:
                    verificador = True
                j += 1
            if verificador == False:
                arq.write(p.voo_numero)
                arq.write(';')
                arq.write(p.origem)
                arq.write(';')
                arq.write(p.destino)
                arq.write(';')
                arq.write(p.distancia)
                arq.write(';')
                arq.write(p.tempo_medio)
                arq.write(';')
                arq.write(p.aeronave)
                arq.write(';')
                i = 0
                while i < len(p.escala):
                    arq.write(p.escala[i])
                    if i < len(p.escala) - 1:
                        arq.write(';')
                    i += 1
                arq.write('\n')    
            i = i + 1
    arq.close()

def cadastro_voo(lista_voo):
    #função para o cadastro de um voo
    p = voo()
    p.voo_numero = input("Informe o número do voo: ")
    
    if verifica_num_voo(p.voo_numero, lista_voo) == False:
        p.origem = str(input('Informe a cidade de origem: '))
        p.destino = str(input("Informe seu destino: "))
        p.distancia = str(input("Informe a distância a ser percorrida até seu destino (km): "))
        p.tempo_medio = str(input("Informe o tempo médio do voo (hrs): "))
        p.aeronave = str(input("Informe o modelo da aeronave: "))
        p.escala = []
        p.escala.append(input("Informe o nome de uma escala ou em branco caso não haja: ")) 
        verificador = True
        while verificador == True: # permite o usuario adicionar mais de uma escala
            pgt = (input("Deseja adicionar mais uma escala (S/N): "))
            if  pgt == "S" or pgt == "s":
                p.escala.append(input("Digite mais uma escala: "))
            else:
                verificador = False
        lista_voo.append(p)
        print("Fim das informações de voo. \n")
    else:
        print('Já existe um voo com esse registro cadastrado. \n')

def listar_voo(p):
    #função que apresenta as informações cadastradas
    print("Número do voo: ",p.voo_numero)
    print('cidade de origem: ',p.origem)
    print("Destino: ",p.destino)
    print("Distância: ",p.distancia,' km')
    print("Duração do voo: ",p.tempo_medio,' hrs')
    print("Aeronave: ",p.aeronave)
    print("Escala(s): ",end='')
    i = 0
    while i < len(p.escala):
        print(p.escala[i])
        i += 1

def imprimir_cadastros_voo(lista_voo):
    #função que imprime todos os cadastros de voos
    if len(lista_voo) > 0:
        print("Lista de voos")
        i = 0
        while i < len(lista_voo):
            listar_voo(lista_voo[i])
            print("\n")
            i += 1
    else:
        print('Não há voos cadastrados \n') 
      
def imprime_voos(lista_voo):
    if len(lista_voo) > 0:
        i = 0
        while i < len(lista_voo):
            print(f'{i + 1}.Numero do voo: ',lista_voo[i].voo_numero,'\n')
            i += 1
            return True
    else:
      print('Não há voos cadastrados \n')
      return False 
      
def imprimir_voos(lista_voo):
    #função que imprime os numeros de voos e permite escolher algum cadastro para ser exibido
      if imprime_voos(lista_voo) == True:
        op = int(input('Digite o numero do indice de voos para mostar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_voo):
            listar_voo(lista_voo[op - 1])    

def excluir_voo(lista_voo):
    #função que exclui um cadastro de voo, especificado pelo usuário
    if imprime_voos(lista_voo) == True:
        op = int(input('Digite o numero do indice de voos para mostar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_voo):
            del lista_voo[op - 1]  

def alterar_voo(lista_voo):
    #função que permite alterar uma informação especificada pelo usuario de algum cadastro
    if imprime_voos(lista_voo) == True:
        op = int(input('Digite o numero do indice de voos para alterar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op <= len(lista_voo): # exibe o layout de opções
            listar_voo(lista_voo[op - 1])
            print("Numero do voo:......1")
            print("Origem:.............2")
            print("Destino:............3")
            print("Distância...........4")
            print("Tempo médio:........5")
            print("Aeronave:...........6")
            print("escala:.............7")

            alt = int(input('Utilize o indice para escolher qual informação será alterada: ')) # pede qual informação a ser alterada
            if alt == 1:
                num_voo = input("informe o registro do piloto: ") 

                if verifica_num_voo(num_voo, lista_voo) == False:
                    lista_voo[op - 1].voo_numero = num_voo    
                else:
                    print('Já existe um voo com esse registro cadastrado. \n')

            elif alt == 2:
                lista_voo[op - 1].origem = str(input("Informe a origem: "))
            elif alt == 3:
                lista_voo[op - 1].destino = str(input("Informe o destino: "))
            elif alt == 4:
                lista_voo[op - 1].distancia = str(input("informe a distância(km): "))
            elif alt == 5:
                lista_voo[op - 1].tempo_medio(input("informe o tempo medio de voo: "))
            elif alt == 6:
                lista_voo[op - 1].aeronave = str(input("Informe o modelo da aeronave: "))
            elif alt == 7:
                lista_voo[op - 1].escala = []
                lista_voo[op - 1].escala.append(input("Informe o nome de uma escala ou em branco caso não haja: ")) 
                verificador = True
                while verificador == True:
                    pgt = (input("Deseja adicionar mais uma escala (S/N): "))
                    if  pgt == "S" or pgt == "s":
                        lista_voo[op - 1].escala.append(input("Digite mais uma escala: "))
                    else:
                        verificador= False
            else:
                print('Opção inexistente.')

def cria_arquivo_viagem(lista_viagem, lista_dados_viagem):
  if existe_arquivo("arquivo_viagem.txt"):
    arq = open("arquivo_viagem.txt", "a")
  else:
    arq = open('arquivo_viagem.txt', 'w')  
  i = 0
  verificador_dados_viagem(lista_dados_viagem)
  while i < len(lista_viagem):
        p = lista_viagem[i]
        verificador = False
        j = 0
        while j < len(lista_dados_viagem): # Verifica se o valor informado já consta em outro cadastro no arquivo
            if p.voo_numero == lista_dados_viagem[j][0]:
                verificador = True
            j += 1
            if verificador == False:
                arq.write(p.voo_numero)
                arq.write(';')
                arq.write(p.nome)
                arq.write(';')
                arq.write(p.registro)
                arq.write(';')
                arq.write(p.saida)
                arq.write(';')
                arq.write(p.hora_saida)
                arq.write(';')
                arq.write(p.hora_chegada)
                arq.write(';')
                i = 0
                while i < len(p.ocorrencia):
                    arq.write(p.ocorrencia[i])
                    if i < len(p.ocorrencia) - 1:
                        arq.write(';')
                    i += 1
                arq.write('\n')    
        i = i + 1
  arq.close()

def cadastro_viagem(lista_viagem, lista_voo, lista_piloto):
    p = viagem()
    p.voo_numero = input("Informe o número do voo: ")
    if verifica_num_voo(p.voo_numero, lista_voo) == True:
        p.nome = str(input("Informe o piloto: "))
        p.registro = str(input("Informe o registro do piloto: "))
        if verifica_piloto(p.registro, lista_piloto) == True:
            p.saida = str(input("Informe a data de saída(dd/mm/aaaa): "))
            p.hora_saida = str(input("Informe a hora de saída(hh:mm): "))
            rep = False
            i = 0
            while i < len(lista_viagem):
                if (p.saida == lista_viagem[i].saida and p.piloto == lista_viagem[i].piloto) or (p.saida == lista_viagem[i].saida and p.voo_numero == lista_viagem[i].voo_numero) or (p.saida == lista_viagem[i].saida and p.hora_saida == lista_viagem[i].hora_saida):
                    print('Algum dos dados inseridos não estará disponivel nessa data. \n')
                    rep = True
            i += 1

            if rep == False:
                p.hora_chegada = str(input("Informe a hora da chegada: "))
                p.ocorrencia = []
                p.ocorrencia.append(input("Informe uma ocorrência do voo: "))
                verificador = True
                while verificador == True:
                    pgt = (input("Deseja adicionar uma ocorrência (S/N): "))
                    if  pgt == "S" or pgt == "s":
                        p.ocorrencia.append(input("Digite mais uma ocorrência: "))
                    else:
                        verificador = False
                lista_viagem.append(p)
                print("Fim das informações de viagem. \n")
        else:
            print('Não existe um piloto com esse registro cadastrado. \n')
    else:
        print('Não existe um voo com esse registro cadastrado. \n')

def listar_viagem(p):
    print("Número do voo:",p.num_voo)
    print("Piloto: ",p.piloto)
    print("Data de saida: ",p.saida)
    print("Hora de saida: ",p.hora_saida)
    print("Hora de chegada: ",p.chegada)
    print("Ocorrências(s): ",p.ocorrencia,'\n')

def imprimir_cadastros_viagens(lista_viagem):
    if len(lista_viagem) > 0:
        print("Lista de viagens")
        i = 0
        while i < len(lista_viagem):
            listar_viagem(lista_viagem[i])
            print("\n")
            i += 1
    else:
        print('Não há viagens cadastrados \n')
      
def verifica_viagens(lista_viagem):
    if len(lista_viagem) > 0:
        i = 0
        while i < len(lista_viagem):
            print(f'{i + 1}.Numero da viagem: ',lista_viagem[i].voo_numero,'\n')
            i += 1
            return True
    else:
        print('Não há viagens cadastradas \n')
        return False 
      
def imprimir_viagens(lista_viagem):
      if verifica_viagens(lista_viagem) == True:
        op = int(input('Digite o numero do indice de viagens para mostar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op < len(lista_viagem) + 1:
            listar_viagem(lista_viagem[op - 1])

def alterar_viagem(lista_viagem):
    if verifica_viagens(lista_viagem) == True:
        op = int(input('Digite o numero do indice de viagens para alterar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op < len(lista_viagem) + 1:
            del lista_viagem[op - 1]
            print('Necessário fazer o cadastro novamente.')
            cadastro_viagem(viagem)
            
def excluir_viagem(lista_viagem):
    if verifica_viagens(lista_viagem) == True:
        op = int(input('Digite o numero do indice de viagens para alterar seu cadastro ou 0 para retornar ao menu : '))
        if op > 0 and op < len(lista_viagem) + 1:
            del lista_viagem[op - 1]  

def verificador_dados_piloto(lista_dados_pilotos):
    arq = open('arquivo_piloto.txt', 'r')
    linha = arq.readline()
    while linha:
        dados = linha.split(';')
        if dados not in lista_dados_pilotos:
            lista_dados_pilotos.append(dados)
        linha = arq.readline()
    arq.close()    

def relatorio_idade(lista_dados_pilotos):
    i = 0
    idade = int(input('Informe a idade minima dos pilotos, que se deseja obter os dados: \n'))
    while i < len(lista_dados_pilotos) and len(lista_dados_pilotos) > 0:
        if (2022 - (int(lista_dados_pilotos[i][4]))) >= idade:
                print("Registro do piloto:",lista_dados_pilotos[i][0])
                print("Nome: ",lista_dados_pilotos[i][1])
                print("Nascimento: ",lista_dados_pilotos[i][2],'/',lista_dados_pilotos[i][3],'/',lista_dados_pilotos[i][4])
                print("Sexo: ",lista_dados_pilotos[i][5])
                print("Curso de especialização: ",lista_dados_pilotos[i][6])
                print("E-mail: ",lista_dados_pilotos[i][7])
                print("Telefone: ",lista_dados_pilotos[i][-1])
                print()     
        i += 1    

def verificador_dados_voo(lista_dados_voo):
    arq = open('arquivo_voo.txt', 'r')
    linha = arq.readline()
    while linha:
        dados = linha.split(';')
        if dados not in lista_dados_voo:
            lista_dados_voo.append(dados)
        linha = arq.readline()
    arq.close()

def relatorio_escala(lista_dados_voo):
    i = 0
    escala = input('Informe a escala que se deseja verificar: \n')
    while i < len(lista_dados_voo) and len(lista_dados_voo) > 0:
        j = 0
        while j < len(lista_dados_voo[i]): 
            if (escala + '\n') == (lista_dados_voo[i][j]) or (escala) == (lista_dados_voo[i][j]):
                    print("Numero do Voo:",lista_dados_voo[i][0])
                    print("Origem: ",lista_dados_voo[i][1])
                    print("Destino: ",lista_dados_voo[i][2],)
                    print("Distância: ",lista_dados_voo[i][3])
                    print("Duração: ",lista_dados_voo[i][4])
                    print("Aeronave: ",lista_dados_voo[i][5])
                    print("Escalas: ",lista_dados_voo[i][6])
                    x = 7
                    while x < len(lista_dados_voo[i]):
                        print(lista_dados_voo[i][x])
                        x += 1
                    print()
            j += 1         
        i += 1 

def verificador_dados_viagem(lista_dados_viagem):
    arq = open('arquivo_viagem.txt', 'r')
    linha = arq.readline()
    while linha:
        dados = linha.split(';')
        if dados not in lista_dados_viagem:
            lista_dados_viagem.append(dados)
        linha = arq.readline()
    arq.close()    

def relatorio_viagem(lista_dados_viagem, lista_dados_voo):
    i = 0
    saida = input('Informe a primeira data de saida que se deseja verificar(dd-mm-aaaa): \n')
    saida2 = input('Informe a um prazo maximo de saida que se deseja verificar: \n')
    print()
    start = datetime.datetime.strptime(saida, "%d-%m-%Y")
    end = datetime.datetime.strptime(saida2, "%d-%m-%Y")  
   
    while i < len(lista_dados_viagem) and len(lista_dados_viagem) > 0:
        date = datetime.datetime.strptime(lista_dados_viagem[i][3], "%d-%m-%Y")
        if start <= date <= end:
                    print('--------------VOO--------------')
                    print("Numero do Voo:",lista_dados_viagem[i][0])
                    print("Piloto: ",lista_dados_viagem[i][1] )
                    print("Registro: ",lista_dados_viagem[i][2])
                    print("Data de saida: ",lista_dados_viagem[i][3])
                    print("Hora de saida: ",lista_dados_viagem[i][4])
                    print("Hora de chegada: ",lista_dados_viagem[i][5])
                    print("Ocorrencias: ",lista_dados_viagem[i][6])
                    x = 7
                    while x < (len(lista_dados_viagem[i])) - 1:
                        print(lista_dados_viagem[i][x])
                        x += 1

                    i = 0
                    num_voo = lista_dados_viagem[i][0]
                    while i < len(lista_dados_voo) and len(lista_dados_voo) > 0:
                        j = 0
                        while j < len(lista_dados_voo[i]): 
                            if num_voo == (lista_dados_voo[i][j]):
                                    print("Origem: ",lista_dados_voo[i][1])
                                    print("Destino: ",lista_dados_voo[i][2],)
                                    print("Distância: ",lista_dados_voo[i][3])
                                    print("Duração: ",lista_dados_voo[i][4])
                                    print("Aeronave: ",lista_dados_voo[i][5])
                                    print("Escalas: ",lista_dados_voo[i][6])
                                    x = 7
                                    while x < len(lista_dados_voo[i]):
                                        print(lista_dados_voo[i][x])
                                        x += 1
                                    print()
                            j += 1         
                        i += 1     
                    print() 
        i += 1 

def main():
    piloto = []
    voo = []
    viagem = []

    arq_pilotos = []
    arq_voo = []
    arq_viagem = []

    op = 0
    while op != '6':
        op = menu()
        if op == '1':
            op = menu_pilotos()
            if op == "1":
                imprimir_cadastros_piloto(piloto)
            elif op == "2":
                imprimir_pilotos(piloto)    
            elif op == "3":
                cadastro_piloto(piloto)
            elif op == '4':
                alterar_piloto(piloto)    
            elif op == '5':
                excluir_piloto(piloto)
            op = 0

        elif op == '2':
            op = menu_voos()
            if op == "1":
                imprimir_cadastros_voo(voo)
            elif op == "2":
                imprimir_voos(voo)    
            elif op == "3":
                cadastro_voo(voo)
            elif op == '4':
                alterar_voo(voo)
            elif op == '5':
                excluir_voo(voo)
            op = 0

        elif op == '3':
            op = menu_viagens()
            if op == "1":
                imprimir_cadastros_viagens(viagem)
            elif op == "2":
                imprimir_viagens(viagem)    
            elif op == "3":
                cadastro_viagem(viagem, voo, piloto)
            elif op == '4':
                alterar_viagem(viagem)
            elif op == '5':
                excluir_viagem(viagem)
            op = 0

        elif op == '4':
            op = menu_relatorios()
            if op == "1":
                relatorio_idade(arq_pilotos)
            elif op == "2":
                relatorio_escala(arq_voo)   
            elif op == "3":
                relatorio_viagem(arq_viagem, arq_voo)
            op = 0
      
        elif op == '5':
            cria_arquivo_piloto(piloto, arq_pilotos)
            verificador_dados_piloto(arq_pilotos)   
            cria_arquivo_voo(voo, arq_voo)
            verificador_dados_voo(arq_voo)
            cria_arquivo_viagem(viagem,arq_viagem)
            verificador_dados_viagem(arq_viagem)
            print(arq_viagem)
          
        elif op == '6':  
            print("Obrigado por usar nosso sistema!")

        else:
            print("Opcao invalida.")
                  
main()
