# bibliotecas ussadas
# pandas
# openpyxl
# twilio

import pandas

client = Client(account_sid, auth_token)

lista_of = ['controlequalidade']

lista_peca = pandas.read_excel('controlequalidade.xlsx')
print(lista_peca)
if (lista_peca['newadd'] > 0.9).any():
    peca = lista_peca.loc[lista_peca['newadd'] > 0.9, 'codpeca'].values[0]
    cliente = lista_peca.loc[lista_peca['newadd'] > 0.9, 'cliente'].values[0]
    of = lista_peca.loc[lista_peca['newadd'] > 0.9, 'of'].values[0]
    pr = lista_peca.loc[lista_peca['newadd'] > 0.9, 'pr'].values[0]
    print(f'Foi encontrada uma peça com erro 1. A peça de numero: {peca}, do cliente: {cliente}, da OF: {of} e o problema em questão foi: {pr}. Agora o mesmo aguarda ação. Obrigado.')


#proximo passo sera criar uma IA para que o servico manual nao seja mais executado, tornando um software inteligente que pode ser comercializado com uma valor ainda a definir