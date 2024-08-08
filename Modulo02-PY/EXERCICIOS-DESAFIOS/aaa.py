def calcular_media(saltos):
    """
    Função que calcula a média dos saltos.

    Parâmetros:
    saltos (list of float): Lista com as distâncias dos saltos.

    Retorna:
    float: A média dos saltos.
    """
    return sum(saltos) / len(saltos)


def main():
    while True:
        nome_atleta = input(
            "Digite o nome do atleta (ou deixe em branco para encerrar): ").strip()
        if not nome_atleta:
            print("Programa encerrado.")
            break

        saltos = []
        for i in range(1, 6):
            while True:
                try:
                    salto = float(input(f"Digite o {i}º salto (em metros): "))
                    saltos.append(salto)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")

        media = calcular_media(saltos)

        # Formatação da saída
        print(f"\nAtleta: {nome_atleta}\n")
        for i, salto in enumerate(saltos, start=1):
            print(f"{['Primeiro', 'Segundo', 'Terceiro',
                  'Quarto', 'Quinto'][i-1]} Salto: {salto:.1f} m")

        print("\nResultado final:")
        print(f"Atleta: {nome_atleta}")
        print("Saltos: " + " - ".join(f"{salto:.1f}" for salto in saltos))
        print(f"Média dos saltos: {media:.1f} m\n")


if __name__ == "__main__":
    main()
