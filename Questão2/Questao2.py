def fibonacci():
    inicio = 0
    adiciona = 1
    total = 1    
    numero = int(input("Escreva o número que verificaremos que faz parte da sequência de fibonacci "))
    #numero = 1548008755919
    while (inicio <= numero):
        print(inicio)
        total = adiciona + inicio
        inicio = adiciona
        adiciona = total
        if(inicio == numero):
            print(numero,"pertence a sequência de fibonacci")
            break
    if(inicio > numero):
        print(numero,"não pertence a sequência de fibonacci") 

def main():
    contiua = True
    while(contiua):
        fibonacci()
        print("Deseja continuar testando números?")
        resposta = input("Se deseja parar escreva 'nao' e de Enter, se não só de Enter: ")
        if(resposta == "nao"):
            break

main()
