import os
import matplotlib.pyplot as plt
import random
os.system("clear") 

movimentos_possiveis = ["Burpee", "Squat", "Push-up", "Pull-up", "Lunge","Sit-up", "Deadlift", "Snatch", "Clean", "Kettlebell Swing"]   

def arquivo_esta_vazio(nome_arquivo):
    return not os.path.exists(nome_arquivo) or os.stat(nome_arquivo).st_size == 0
nome_arquivo = 'treinos.txt'

def validacao_treino():
    treinos_validos = ["AMRAP", "EMOM", "FOR TIME"]  
    while True:
        tipo_de_treino = input("Tipo de treino (AMRAP, EMOM ou FOR TIME): ").upper()
        if tipo_de_treino in treinos_validos:
            return tipo_de_treino
        print("Tipo Inválido! Por favor, digite exatamente AMRAP, EMOM ou FOR TIME.")

def adicionar_meta():
    with open("metas.txt", "a") as file:
        tipo_de_treino = validacao_treino()
        objetivo = input("Qual é a sua meta para esse tipo de treino? ")
        file.write(f"Tipo: {tipo_de_treino} | Meta: {objetivo}\n")
        print("Meta adicionada com sucesso!")

def validacao_tempo():
    while True: 
        try:
            tempo_do_treino = float(input("Duração em minutos do treino: "))
            if tempo_do_treino > 0:
                return tempo_do_treino
            else: 
                print("Digite um número maior que 0.")
        except ValueError:
            print("Digite um número válido.")

def gerar_treino_aleatorio(tipo_de_treino, tempo_do_treino):
    movimentos_escolhidos = random.sample(movimentos_possiveis, 3)
    return {
        "tipo": tipo_de_treino,
        "tempo": tempo_do_treino,
        "movimentos": movimentos_escolhidos
    }

def sugestao_wod():
    tipo_de_treino = random.choice(["AMRAP", "EMOM", "FOR TIME"])
    tempo_do_treino = random.choice([10, 15, 20, 25])
    treino = gerar_treino_aleatorio(tipo_de_treino, tempo_do_treino)
    with open("treinos.txt", "a") as file:
        file.write("\nSugestão de WOD Aleatório: ")
        file.write(f"Tipo: {treino['tipo']} ")
        file.write(f" Duração: {treino['tempo']} minutos ")
        file.write(" Movimentos: ")
        for movimento in treino['movimentos']:
            file.write(f" {movimento}-")
        print("\n")

def selecionar_treino_por_criterio(linhas):
    while True:
        criterio = validacao_treino()
        treinos_encontrados = [linha.strip() for linha in linhas if criterio.lower() in linha.lower()]
        
        if not treinos_encontrados:
            print("Não existe um treino com esse tipo. Tente novamente.")
            continue
        
        print("\nTreinos encontrados:")
        for i, treino in enumerate(treinos_encontrados, start=1):
            print(f"\n{i}. {treino}")

        while True:
            try:
                escolha = int(input(f"\nEscolha o número do treino que deseja selecionar (1-{len(treinos_encontrados)}): ").strip())
                if 1 <= escolha <= len(treinos_encontrados):
                    indice = escolha - 1
                    return indice, treinos_encontrados
                else:
                    print(f"Escolha um número entre 1 e {len(treinos_encontrados)}.")
            except ValueError:
                print("Por favor, digite um número válido.")

cont_amrap = 0
cont_emom = 0
cont_for_time = 0

print("\nOlá, Thiago! Seja bem-vindo.")
print("\nVamos treinar? Você deseja:")

while True:
    print("\n1- Adicionar \n2- Vizualizar \n3- Editar \n4- Excluir \n5- Gráfico dos Treinos \n6- Adicionar Metas \n7- Gerar Treinos Aleatorios \n8- Encerrar")

    try:
        opcao = int(input("\nDigite a opção: "))
    except ValueError:
        opcao = int(input("\nDigite o número de cada opção, ex: 1 para adicionar um novo treino: "))
        continue

    if opcao == 1:
        file = open("treinos.txt" , "a")
        data = input("Data do treino (dd/mm/aaaa): ")
        tipo_de_treino = validacao_treino()
            
        if tipo_de_treino == "AMRAP":
            cont_amrap += 1
        elif tipo_de_treino == "EMOM":
            cont_emom += 1
        elif tipo_de_treino == "FOR TIME":
            cont_for_time += 1

        tempo_do_treino = validacao_tempo()
        movimentos = input("Movimentos: ")

        file.write("Data: " + data + " | Tipo: " + tipo_de_treino + " | Duração: " + str(tempo_do_treino) + " minutos | Movimentos: " + movimentos + "\n")
        print("\nTreino adicionado com sucesso!")
        file.close()
    
    elif opcao == 2:
        if arquivo_esta_vazio(nome_arquivo):
            print("\nNenhum treino encontrado.\nAdicione um treino antes de visualizar.")
        else:    
            print("\n------ Treinos Crossfit ------")
            file = open("treinos.txt" , "r")
            print(f"\n{file.read()}")
            file.close()

    elif opcao == 3:
        if arquivo_esta_vazio(nome_arquivo):
            print("\nNenhum treino encontrado.\nAdicione um treino antes de editar.")
        else:    
            file = open("treinos.txt", "r")
            linhas = file.readlines() 
            file.close() 
                
            indice, treinos_encontrados = selecionar_treino_por_criterio(linhas)
            treino_selecionado = treinos_encontrados[indice]
            divisao_linha = treino_selecionado.split(" | ")

            print("\n1 - Data \n2 - Tipo de Treino \n3 - Tempo de Treino \n4 - Movimentos")
            while True:
                try: 
                    editar = int(input("\nDigite a opção do tópico que deseja editar (1-4): "))
                except ValueError:
                    print("\nOpção Inválida. Tente novamente.")
                    continue

                if editar == 1:
                    nova_data = input("Digite a nova data (dd/mm/aaaa): ")
                    divisao_linha[0] = "Data: " + nova_data 
                    print("\nData editada com sucesso!")
                    break
                    
                elif editar == 2:
                    novo_tipo_de_treino = validacao_treino()
                    divisao_linha[1] = " Tipo: " + novo_tipo_de_treino
                    print("\nTipo de treino editado com sucesso!") 
                    break

                elif editar == 3:
                    novo_tempo_do_treino = validacao_tempo()
                    divisao_linha[2] = "Duração: " + str(novo_tempo_do_treino) + " minutos"
                    print("\nTempo de treino editado com sucesso!")
                    break

                elif editar == 4:
                    novo_movimento = input("Digite os novos movimentos: ")
                    divisao_linha[3] = " Movimentos: " + novo_movimento 
                    print("\nMovimentos editados com sucesso!")
                    break

                else:
                    print("Opção Inválida! Tente novamente.")

            file = open("treinos.txt", "w")
            indice_original = linhas.index(treino_selecionado + "\n") 
            linhas[indice_original] = " | ".join(divisao_linha) + "\n" 
            file.writelines(linhas) 
            file.close()

    elif opcao == 4:
        if arquivo_esta_vazio(nome_arquivo):
            print("\nNenhum treino encontrado.\nAdicione um treino antes de excluir.")
        else: 

            try:
                escolha_remover = int(input("\nDigite '1' para remover o treino completo ou '2' para remover um item do treino: "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                continue


            if escolha_remover == 1:
                file = open("treinos.txt", "r")
                linhas = file.readlines()
                file.close()

                indice, treinos_encontrados = selecionar_treino_por_criterio(linhas)
                treino_selecionado = treinos_encontrados[indice]

                linhas.remove(treino_selecionado + "\n") 
                print("\nTreino removido com sucesso!")
                file = open("treinos.txt", "w")
                file.writelines(linhas)
                file.close()

            elif escolha_remover == 2:
                file = open("treinos.txt", "r")
                linhas = file.readlines()
                file.close()
                
                indice, treinos_encontrados = selecionar_treino_por_criterio(linhas)
                treino_selecionado = treinos_encontrados[indice]
                partes = treino_selecionado.split(" | ")

                print("\n1 - Data \n2 - Tipo de Treino \n3 - Tempo de Treino \n4 - Movimentos")

                while True:
                    try:
                        topico = int(input("Digite o número do tópico que deseja remover: "))

                        if topico <= 0 or topico > 4:
                            print("Digite um número válido: ")
                            continue
                            
                        elif topico == 1:
                            partes.pop(0)

                        elif topico == 2:
                            partes.pop(1)

                        elif topico == 3:
                            partes.pop(2)

                        else:
                            partes.pop(3)

                        break
                    
                    except ValueError:
                        print("Digite o número inteiro do tópico desejado.")
                    except IndexError:
                        print("Esse tópico já foi removido ou não existe.")

                linhas[indice] = " | ".join(partes) + "\n"
                file = open("treinos.txt", "w")
                file.writelines(linhas)
                file.close()
                print("\nTópico removido com sucesso!")
    
    elif opcao == 5:
        try:
            with open("treinos.txt", "r") as file:
                linhas = file.readlines()

            cont_amrap = cont_emom = cont_for_time = 0

            for linha in linhas:
                if 'AMRAP' in linha:
                    cont_amrap += 1
                elif 'EMOM' in linha:
                    cont_emom += 1
                elif 'FOR TIME' in linha:
                    cont_for_time += 1

            if cont_amrap == 0 and cont_emom == 0 and cont_for_time == 0:
                print("\nNenhum treino encontrado para gerar o gráfico.")
            else:
                tipos = ['AMRAP', 'EMOM', 'FOR TIME']
                valores = [cont_amrap, cont_emom, cont_for_time]

                plt.pie(valores, labels=tipos, autopct='%1.1f%%', startangle=90)
                plt.title('Distribuição dos Tipos de Treino')
                plt.axis('equal')
                plt.show()
        except FileNotFoundError:
            print("\nArquivo 'treinos.txt' não encontrado.")

    elif opcao == 6:
        adicionar_meta()
        resposta = input("Deseja visualizá-las? 1 - Sim | 2 - Não: ")
        if resposta == "1":
            with open("metas.txt", "r") as file:
                print("\nSuas metas:")
                print(file.read())
    
    elif opcao == 7:
        sugestao_wod()
        print("\nTreino aleatório gerado com sucesso!\nDigite 2 para visualiza-lo!")
            
    elif opcao == 8:
        break

    else:
        print("\nEssa opção não exite. Tente Novamente.")
        try:
            opcao = int(input("\nDigite a opção: "))
        except ValueError:
            opcao = int(input("\nDigite o número de cada opção, ex: 1 para adicionar um novo treino: "))