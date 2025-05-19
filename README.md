#Manual do Usuário


WOD Tracker
O WOD Tracker é uma forma prática, utilizando aplicações em Python, para registrar e acompanhar desempenhos em treinos (WODs). O sistema roda no VS Code, armazena os dados localmente em um arquivo(.txt), feito de maneira simples e interativa.
Funcionalidades
1. Adicionar treinos:
O usuário insere: data do treino, tipo de treino, tempo/duração e os movimentos realizados. Os dados são gravados no arquivo treinos.txt.
2. Visualizar treinos:
Exibe todos os treinos cadastrados. Se não houver nenhum treino registrado o programa avisa ao usuário.
3. Editar treinos: 
O usuário filtra o treino pelo seu tipo. E ele pode alterar todos os tópicos do treino, sendo eles: data, tipo, tempo/duração e movimentos.
4. Excluir treinos:
O usuário possui duas opções: excluir o treino completo ou um tópico dele. A seleção é feita pelo tipo do treino .
5. Gráfico de WODs:
O sistema contabiliza quantos treinos de cada tipo foram cadastrados e gera um gráfico de pizza com a distribuição deles.
Ex: 
  



6. Adicionar Metas:
O sistema armazena as metas de desempenho definidas pelo usuário, permitindo acompanhar a evolução e melhorar o rendimento nos treinos.
7. Treinos aleatórios:
O sistema gera treinos aleatórios para diversificar a rotina do usuário e estimular diferentes capacidades físicas.
8. Encerrar:
Encerra o programa com segurança, garantido que os treinos foram salvos.


Restrições
* O tipo de treino deve ser escrito exatamente como indicado: AMRAP, EMOM, FOR TIME. Podem ser escritos em letras maiúsculas ou minúsculas.
* O arquivo txt não deve ser deletado manualmente, pois pode afetar o armazenamento do histórico.
* Não é possível adicionar treinos duplicados automaticamente, o usuário deve gerenciar isso.
Requisitos
* Desenvolvido em Python puro, com exceção do uso da biblioteca matplotlib para o gráfico de WODs.
* Interação via linha de comando (terminal).
* Utiliza os.system(“cls”) para limpar a tela (ajustável para “clear” para usuários de MacOS).
* Armazena os treinos em arquivo txt.


Validações e Segurança


* Validação tipo de treino: AMRAP, EMOM, FOR TIME.
* Validação de tempo: exige um número positivo.
* Tratamento de erros: evita falhas com entradas inválidas.
* Verificação de arquivos: impede ações como visualizar, editar ou excluir sem treinos registrados.
Como Utilizar
* Execute o Script Python no terminal.
* Escolha uma das opções no menu.
* Siga as instruções que aparecem na tela.
* Instale o matplotlib no Python:
Abra o terminal ou prompt de comando (dependendo do seu sistema operacional):
Windows: você pode usar o Prompt de Comando (cmd) ou o PowerShell.
macOS/Linux: use o Terminal.
Se estiver usando um editor como o VS Code, você pode abrir o terminal integrado.
Digite o seguinte comando: pip install matplotlib ou pip3 install matplotlib
        
Estrutura do Arquivo txt
Data: 14/05/2025 | Tipo: AMRAP | Duração: 20.0 minutos | Movimentos: burpees, pull-ups
