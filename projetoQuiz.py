
print('Bem vindo ao Quiz DZAU!')
entr_user = input('Você quer iniciar? (S/N)')

if entr_user.strip().upper() != 'S':
    quit()
pontuação = 0

print('O que gostaria de treinar hoje?\n')
print('''
       ┌──────────────────────────────────┐
       │       O que deseja treinar?      │
       │                                  │
       │  1 - [ Matemática ]              │
       │  2 - [ Python ]                  │
       │  3 - [ Introdução à Computação ] │
       │  4 - [ Soft Skills ]             |
       │  5 - [ Mix de perguntas ]        |
       └──────────────────────────────────┘
       ''')
MATEMÁTICA = '1'
PYTHON = '2'
INTRO_À_COMPUT = '3'
SS = '4'
MIX = '5'
opcao_user = input('Digite o número da opção: ')
if opcao_user == MATEMÁTICA:
 print('Quiz de Matemática do DZAU iniciando' )
 print('Pela definição, o que é um número e um numeral?\n (A)Um número é uma representação abstrata (o desenho ou simbolo) do que queremos quantificar, enquanto o numeral é a quatidade em sí do que queremos mostrar.\n (B)TESTE.\n (C)teste.\n')
 resp_1 = input('Resposta: ').strip().upper()
 
 if resp_1 == 'A':
     print('correto!')
     pontuação = pontuação + 1
 else:
     print('Incorreto!')
     pontuação = max(0, pontuação - 1)
 
elif opcao_user == PYTHON:
 print('Quiz de Python do DZAU iniciando')
 print('Qual o comando para mostrar a saída do nosso código na tela para o usuário em Python:\n (A)show\n (B)cat\n (C)print\n')
 resp_1 = input('Resposta: ').strip().upper()
 
 if resp_1 == 'C':
     print('correto!')
     pontuação = pontuação + 1
 else:
     print('Incorreto!')
     pontuação = max(0, pontuação - 1)

elif opcao_user == INTRO_À_COMPUT:
    print('Quiz de Introdução à Computação iniciando')
    print('O que quer dizer a sigla HD:\n (A)Hot Dog\n (B)Hard Fish\n (C)Hard Disk\n')
    resp_1 = input('Resposta: ').strip().upper()
   
    if resp_1 == 'C':
        print('correto!')
        pontuação = pontuação + 1
    else:
        print('Incorreto!')
        pontuação = max(0, pontuação - 1)
   
elif opcao_user == SS:
    print('Quiz de Soft Skills iniciando')
    print('Qual a sigla comumente usada para representar Soft Skills?\n (A)SK\n (B)SSL\n (C)SS\n')
    resp_1 = input('Resposta: ').strip().upper()
     
    if resp_1 == 'C':
        print('correto!')
        pontuação = pontuação + 1
    else:
        print('Incorreto!')
        pontuação = max(0, pontuação - 1)

elif opcao_user == MIX:
    print('Quiz de Mix de perguntas iniciando')
    print('O que quer dizer a sigla "HD":\n (A)Hot Dog\n (B)Hard Fish\n (C)Hard Disk\n')
    resp_1 = input('Resposta: ').strip().upper()
    
    if resp_1 == 'C':
         print('correto!')
         pontuação = pontuação + 1
    else:
         print('Incorreto!')
         pontuação = max(0, pontuação - 1)
       
print(f'Seu pontuação atual é de {pontuação}!')
