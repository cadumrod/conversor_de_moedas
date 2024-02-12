from forex_python.converter import CurrencyRates



#Def para solicitar quais moedas converter
def escolher_moeda():
    moeda_base = input("Digite o código da moeda base ( Ex: USD, BRL): ").upper()
    moeda_alvo = input("Digite o código da moeda de câmbio ( Ex: USD, BRL): ").upper()
    return moeda_base, moeda_alvo


#Função para converter a moeda
def conversao_moeda(moeda_base, moeda_alvo, quantia):
    c = CurrencyRates()
    return c.convert(moeda_base,moeda_alvo,quantia)


# Função para apresentar lista de moedas disponíveis
def moedas_disponiveis():
    c = CurrencyRates()
    moedas = c.get_rates('BRL')
    return moedas.keys()




# Função principal
def main():
    while True:
        print("Lista de moedas disponíveis para conversão: ")
        lista_moedas_disponiveis = moedas_disponiveis()
        for moeda in lista_moedas_disponiveis:
            print(moeda)

        moeda_base, moeda_alvo = escolher_moeda()
        amount_str = input("Digite a quantidade de moeda base que você deseja converter: ")
        
        # Substituir ',' por '.' ou vice-versa, se necessário
        amount_str = amount_str.replace(',', '.') if ',' in amount_str else amount_str.replace('.', ',')
        
        # Converter para float
        amount = float(amount_str)
        
        quantia_convertida = conversao_moeda(moeda_base, moeda_alvo, amount)
        print(f"{amount} {moeda_base} equivale a aproximadamente {quantia_convertida:,.2f} {moeda_alvo}")

        nova_consulta = input("Você deseja realizar nova conversão? Digite [S] para Sim ou [N] para Não: ")
        if nova_consulta.upper() == 'S':
            continue
        elif nova_consulta.upper() != 'N':
            print("Digite [S] ou [N].")
            continue
        else:
            break

        



if __name__ == "__main__":
    main()