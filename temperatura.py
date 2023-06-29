def exibir_histograma(variacao_temperatura):
    print("Histograma da Variação da Temperatura")
    print("------------------------------------")
    
    for dia, variacao in variacao_temperatura.items():
        barra = "#" * variacao
        print(f"{dia}: {barra}")

def main():
    variacao_temperatura = {
        "Segunda-feira": 13,
        "Terça-feira": 25,
        "Quarta-feira": 22,
        "Quinta-feira": 21,
        "Sexta-feira": 26,
        "Sábado": 25,
        "Domingo": 20
    }
    
    exibir_histograma(variacao_temperatura)

if __name__ == "__main__":
    main()

