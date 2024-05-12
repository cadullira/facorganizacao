
# declarando uma função
def saudacao():
  print('Olá Mundo!')

# função com parâmetro
def saudacao_para(saudacao, pessoa):
  print(f'{saudacao}, {pessoa}?')

def mensagem_boas_vindas_nomeado(mensagem, nome_pessoa):
  print(f"{mensagem}, {nome_pessoa}")

def mensagem_boas_vindas_valores_padrao(mensagem = 'é 10', nome = 'João'):
  print(f'{nome} {mensagem}')

# chamando uma funcao
saudacao()
saudacao_para('Tudo bem', 'Cadu')
# chamando função nomeando os parâmetros
mensagem_boas_vindas_nomeado(nome_pessoa='Melissa', mensagem='Papai te ama')
# chamando função com parâmetros com valores padrão
mensagem_boas_vindas_valores_padrao()
