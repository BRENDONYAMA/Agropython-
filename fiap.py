def menu():
    print(
        "O desenvolvimento desse programa teve como foco o estado de São Paulo. Os dados apresentados são uma mescla de dados reais e fictícios.")

    while True:
        print('\n========== Menu de Culturas Agrícolas ==========')
        print('1. Cultura de Hortaliças - Tomate')
        print('2. Cultura de Grãos - Café')
        print('3. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            tomate_info()
        elif opcao == '2':
            cafe_info()
        elif opcao == '3':
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida! Por favor, escolha novamente.')


def tomate_info():
    while True:
        print('\n========== Menu do Tomate ==========')
        print('0.1. Informações Gerais')
        print('0.2. Cálculos estatísticos')
        print('0.3. Estrutura e componentes da plantação')
        print('0.4. Voltar ao menu principal')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            print("Informações gerais sobre o tomate.")
        elif opcao == '2':
            print("Plantação com espaçamento de 1m X 1m.")
            area_t = float(input("Digite a área disponível para a plantação em metros quadrados:"))
            area_ut = area_t * 0.25
            num_tomate = area_ut * 2
            rua = (area_t / 10000) * 50
            print(f"A área útil é de {area_ut} m², número estimado de pés de tomate: {num_tomate}, comprimento das ruas: {rua} m.")
        elif opcao == '3':
            print("Cálculos estatísticos para o tomate.")

        elif opcao == '4':
            break
        else:
            print('Opção inválida!')


def cafe_info():
    print("Informações sobre o café.")


if __name__ == '__main__':
    menu()