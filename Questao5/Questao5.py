def main():
    #palavra = palavra[::-1]
    while(True):
        
        palavra = input("Digite a palavra ou frase que será invertida: ")
        palavra = list(palavra)
        palavra = inverter(palavra)
        palavra = "".join(palavra)
        
        print(palavra)
        
        continuar = input("Quer continuar escrevendo ? Digite 'sim' para continuar: ")
        
        if(continuar != "sim"):
            break


def inverter(palavra):
    tamanho = len(palavra)
    fim = tamanho - 1 

    for inicio in range(tamanho//2):

        palavra[inicio],palavra[fim] = palavra[fim],palavra[inicio]
        fim -= 1
    return palavra

main()
