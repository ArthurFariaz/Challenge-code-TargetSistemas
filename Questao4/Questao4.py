def main():
    print("Calculo do faturamento em relação a estado ou regiões")
    
    dados = list()
    FaturamentoGlobal = 0
    print("Esses são os dados guardados")
    dadosCadastrados = [['SP',67836.43],['RJ',36678.66],['MG',29229.88],['ES',27165.48],['Outros',19849.53]]

    FaturamentoArmazenado = FaturamentoTotal(dadosCadastrados)
    Parcela(dadosCadastrados,FaturamentoArmazenado)
    
    print("Temos novos dados para cadastrar ?")
    continuar = input("Digite 'sim' para realizarmos um novo calculo: ")
    if(continuar == "sim"):
        dados = Cadastramento()
        FaturamentoGlobal = FaturamentoTotal(dados)
        Parcela(dados,FaturamentoGlobal)
    else:
        print("Se não temos o programa irá se encerrar")


def Cadastramento():
    estados = list()
    dados = list()
    totalEstados = int(input("Qual o número de estados que iremos calcular? "))
    for EstadoAtual in range(totalEstados):
        nome = input("Qual o nome do estado: ")
        faturamento = float(input("Faturamento do mesmo: "))
        estados.append(nome),estados.append(faturamento),dados.append(estados[:]),estados.clear()

    return dados
def FaturamentoTotal(dados):
    faturamento = 0
    for EstadoAtual in  dados:
        faturamento += EstadoAtual[1]
    return faturamento

def Parcela(dados,FaturamentoTotal):
    for CadaEstado in dados:
        Parcela = CadaEstado[1]
        Parcela = (Parcela * 100)/FaturamentoTotal
        print(f"O percentual do {CadaEstado[0]} é {Parcela:.4f}%")

main()
