import json

def LerJson(arquivo):
    with open (arquivo) as dados_json:
        dados = json.load(dados_json)
        return dados

def PercorrerJson(dados):

    Media = NumeroDias = MaiorValor = NumeroDiasSuperior = 0
    DiaMenor = DiaMaior = 1
    MenorValor = float('inf')

    for PercorrerJson in dados:

        if(PercorrerJson['valor'] > 0 ):
            Media += PercorrerJson['valor']
            NumeroDias += 1
            
            if(PercorrerJson['valor'] > MaiorValor):
                MaiorValor = PercorrerJson['valor']
                DiaMaior = PercorrerJson['dia']

            if(PercorrerJson['valor'] < MenorValor ):
                MenorValor = PercorrerJson['valor']
                DiaMenor = PercorrerJson['dia']

    Media = Media/NumeroDias

    for PercorrerJson in dados:
        if(PercorrerJson['valor'] > Media):
            NumeroDiasSuperior += 1   

    return (MaiorValor,MenorValor,DiaMaior,DiaMenor,NumeroDiasSuperior)


def Main():
    
    Arquivo = "dados.json"
    dados = LerJson(Arquivo)
    MaiorValor,MenorValor,DiaMaior,DiaMenor,NumeroDiasSuperior = PercorrerJson(dados)

    print("O maior faturamento foi de valor", MaiorValor, "e ocorreu no dia", DiaMaior)
    print("O menor faturamento foi de valor", MenorValor, "e ocorreu no dia", DiaMenor)
    print("O número de dias que superou à média mensal foi de", NumeroDiasSuperior)

Main()
