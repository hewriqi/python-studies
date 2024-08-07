def dataExtenso(data):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
             ['maio', 31], ['junho', 30], ['julho', 31], [
                 'agosto', 31], ['setembro', 30],
             ['outubro', 31], ['novembro', 30], ['dezembro', 31]]

    data = data.split('/')
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')

# verifica se ano é bissexto


def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28


dataExtenso('12/04/2006')
dataExtenso('07/08/2024')
