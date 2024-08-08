from time import sleep


def media_saltos(lista_saltos):
    return sum(lista_saltos) / len(lista_saltos)


def main():
    while True:
        nome_atleta = str(input('Digite o nome do atleta: ')).strip()
        if not nome_atleta:
            print('Encerrando programa...')
            sleep(1.5)
            break
        lista_saltos = []
        for i in range(1, 6):
            while True:
                try:
                    saltos_atleta = float(
                        input(f'Digite a altura do {i}º salto: '))
                    lista_saltos.append(saltos_atleta)
                    break
                except ValueError:
                    print('Valor inválido, tente novamente.')
                    continue
        media = media_saltos(lista_saltos)
        print(f'Atleta: {nome_atleta}\n')
        print(f'\nPrimeiro Salto: {lista_saltos[0]}m')
        print(f'Segundo Salto: {lista_saltos[1]}m')
        print(f'Terceiro Salto: {lista_saltos[2]}m')
        print(f'Quarto Salto: {lista_saltos[3]}m')
        print(f'Quinto Salto: {lista_saltos[4]}m')

        print("\nResultado final:")
        print(f"Atleta: {nome_atleta}")
        print("Saltos: " +
              " - ".join(f"{salto:.1f}" for salto in lista_saltos))
        print(f"Média dos saltos: {media:.1f} m\n")

        sleep(2)
        pergunta_sair = input('Você deseja sair?: [s/n]')
        if pergunta_sair == 's':
            print('Saindo...')
            sleep(1)
            break
        else:
            print('Continuando o programa...')
            sleep(1)
            continue


main()
