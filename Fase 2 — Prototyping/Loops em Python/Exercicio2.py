#2. Observando o mercado de educação infantil, você e sua equipe decidem criar um aplicativo por meio do qual as crianças aprendam a controlar os seus gastos. 
# Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou
#No final do programa, ele deve mostrar ao usuário o total gasto durante todas as transações, além de calcular e apresentar a média do valor de cada transação realizada.

print("====BEM VINDO AO APP DE CONTROLE FINANCEIRO====")
qnt_transacoes = int(input("Informe a quantidade de movimentações efetuadas hoje: "))
i = 0
total_transacoes = 0
while i < qnt_transacoes:
    i += 1
    transacao = int(input(f"Informe o valor da transação {i}º: "))
    total_transacoes += transacao
print(f"O seu gasto total de hoje foi de R${total_transacoes:.2f}")