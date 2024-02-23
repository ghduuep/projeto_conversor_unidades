import os

def nome_do_programa():
    '''Exibe o nome do programa'''
    print('''
█▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█
█▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄\n''')

def converter_celsius(temperatura):
    '''Recebe uma temperatura em celsius fornecida e transforma em fahrenheit'''
    resultado = (temperatura * 1.8) + 32
    print(f'\nA conversão de {temperatura}ºC em Fahrenheit é {resultado}\n')

def converter_km(quilometros):
    '''Recebe uma quilometragem e transforma em milhas'''
    resultado = quilometros * 0.62
    print(f'A conversão de {quilometros}Km em milhas é {resultado}')

def converter_kg(quilogramas):
    '''Recebe um peso em quilogramas e transforma em libras'''
    resultado = quilogramas * 2.20
    libra = 'Lbs' if resultado > 1 else 'Lb'
    print(f'A conversão de {quilogramas}Kg é {resultado:.2f}{libra}')

def sair_do_programa():
    '''Limpa a tela e sai do programa'''
    os.system('cls')
    print('Saindo do programa...')

def opcao_invalida():
    '''Mensagem de opcao invalida'''
    print('Parece que você digitou uma opção inválida, tente novamente!')
    voltar_ao_menu()

def voltar_ao_menu():
    '''Usuario digita qualquer tecla e volta para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def mensagem_opcoes():
    '''Exibe as opcoes do usuario e recebe a opcao escolhida'''
    print('''Escolha uma das opções:\n
1 - Celsius para Fahrenheit
2 - Quilômetros para milhas
3 - Quilogramas para libras
4- Sair\n''')

def opcao_escolhida():
    '''Recebe a opcao escolhida pelo usuario e a manda para suas respectivas funcoes'''
    try:
        escolha_usuario = int(input('Escolha uma opção: '))
        if escolha_usuario == 1:
            temperatura = int(input('Digite a temperatura em Celsius(ºC): '))
            converter_celsius(temperatura)
        elif escolha_usuario == 2:
            quilometros = float(input('Digite a quantidade de Quilômetros(Km): '))
            converter_km(quilometros)
        elif escolha_usuario == 3:
            quilogramas = float(input('Digite a quantidade de Quilogramas(Kg): '))
            converter_kg(quilogramas)
        elif escolha_usuario == 4:
            sair_do_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Pagina inicial do programa'''
    os.system('cls')
    nome_do_programa()
    mensagem_opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()