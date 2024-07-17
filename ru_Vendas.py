from enum import Enum, auto
from dataclasses import dataclass
import subprocess
import time


# Tipos compostos (Dados) -------------------------------------------------------------------------------------------

class tipoCliente(Enum):
    ALU = auto()
    SER = auto()
    SE3 = auto()
    DOC = auto()
    EXT = auto()

@dataclass 
class tipoPagamento(Enum):
    PIX = auto()
    CAR = auto() 
    DIN = auto()

@dataclass
class vendas:
    cliente: tipoCliente 
    pagamento: tipoPagamento
    tickets: int


# Funções de uso geral ----------------------------------------------------------------------------------------------

def imprimeTabelas(tipo: int) -> str:
    '''Imprime uma tabela de tipos de cliente no terminal se a entrada da função 'tipo' for 0. 
    Se a entrada da função 'tipo' for 1 imprime uma tabela de formas de pagamento.
    Se a entrada da função 'tipo' for 2 imprime uma tabela de tipos de serviços que o sistema oferece.
    >>> imprimeTabelas(0)
    <BLANKLINE>
    |            TIPOS DE CLIENTES            |
    |ALUNO                                -> 0|
    |SERVIDOR com salário <= 3 mil reais  -> 1|
    |SERVIDOR com salário > 3 mil reais   -> 2|
    |DOCENTE                              -> 3|
    |EXTERNO                              -> 4|
    <BLANKLINE>
    >>> imprimeTabelas(1)
    <BLANKLINE>
    |  PAGAMENTO  |
    |PIX      -> 0|
    |CARTÃO   -> 1|
    |DINHEIRO -> 2|
    <BLANKLINE>
    >>> imprimeTabelas(2)
    <BLANKLINE>
    |        SERVIÇOS        |
    |NOVA VENDA          -> V|
    |RELATORIO DE VENDAS -> R|
    |SAIR DO SISTEMA     -> S|
    <BLANKLINE>
    '''

    if tipo == 0:
        print("""\n|            TIPOS DE CLIENTES            |
|ALUNO                                -> 0|
|SERVIDOR com salário <= 3 mil reais  -> 1|
|SERVIDOR com salário > 3 mil reais   -> 2|
|DOCENTE                              -> 3|
|EXTERNO                              -> 4|\n""")
    elif tipo == 1:
        print("""\n|  PAGAMENTO  |
|PIX      -> 0|
|CARTÃO   -> 1|
|DINHEIRO -> 2|\n""")
    elif tipo == 2:
        print("""\n|        SERVIÇOS        |
|NOVA VENDA          -> V|
|RELATORIO DE VENDAS -> R|
|SAIR DO SISTEMA     -> S|\n""")

def limp() -> None:
    '''Executa o comando 'clear' no shell independente do OS a fim de limpar todo histórico deixado 
    no terminal.
    '''
    subprocess.run(['clear'], shell=True, check=True)


# Fuções para uma *NOVA VENDA* --------------------------------------------------------------------------------------

def armazena_venda(tip_cliente: tipoCliente, tip_pagamento: tip_pagamento, tickets: int, base_de_dados: vendas) -> None:
    '''Recebe o 'valor' de uma venda, quantidade de 'tickets', tipo de pagamento no 'index_pagamento', 
    tipo de cliente no 'index_cliente'. Esses dados são utilizados para armazenar dentro de base de dados que é
    inserida pela input 'base_de_dados' do tipo dados. E são armazenadas de acordo com alguns critérios: 

    'valor' de uma venda será armazenada no atributo total_valorVendido da 'base_de_dados';
    quantidades de 'tickets' será armazenada no atributo total_tickets da 'base_de_dados'; 
    'index_pagamento' serve para decidir onde irá armazenar o 'valor' da vende de acordo com o tipo de pagamento
    'index_pagamento' serve para decidir onde irá armazenar a quantidade de 'tickets' de acordo com o tipo de cliente
    >>> meusClientes: quantidadeCliente = quantidadeCliente(12,4,2,4,1)
    >>> pagamentos: quantidadePagamento = quantidadePagamento(23,72,19)
    >>> meusDados: dados = dados(pagamentos, meusClientes, 23, 114)
    >>> armazena_dados(45, 9, 1, 1, meusDados)

    '''
    
    veda_dados: vendas = vendas(tip_cliente, tip_pagamento, tickets)
    base_de_dados.apend(venda_dados)

def valor_ticket(tip_cliente: int) ->int:
    '''Essa função retorna o valor do ticket em função da entrada 'index_cliente'. Clientes do tipo Aluno e Servidor que
    um salário menor ou igual a 3 mil reais, são representados pelo index 0 e 1 respectivamente e retornam como valor de
    ticket 5 reais. Clientes do tipo Servidor que ganha mais de 3 mil de salário e Docentes, são representados pelo index
    2 e 3 respectivamente e retornam como valor do ticket 10 reais. Clientes do tipo Externo, são representados pelo 
    index 4 e retornam como valor do ticket 19 reais.
    >>> valor_ticket(0) == valor_ticket(1)
    True
    >>> valor_ticket(0)
    5
    >>> valor_ticket(3)
    10
    >>> valor_ticket(4)
    19
    '''

    valor_ticket: int = 0
    if tip_cliente == tipoCliente.ALU or tip_cliente == tipoCliente.SER:
        valor_ticket = 5
    elif tip_cliente == tipoCliente.SE3 or tip_cliente == tipo.Cliente.DOC:
        valor_ticket = 10
    else: 
        valor_ticket = 19
    
    return valor_ticket

def indexTOcliente(index_cliente: int) -> tipoCliente:
    '''Recebe um número que é referente a um tipo de cliente e associa esse número a `tipoCliente` correspondente.'''

        res: tipoCliente
        if index_cliente == 0:
            res = tipoCliente.ALU
        elif index_cliente == 1:
            res = tipoCliente.SER
        elif inde_cliente == 2: 
            res = tipoCliente.SE3
        elif index_cliente == 3: 
            res = tipoCliente.DOC
        else: 
            res = tipoCliente.EXT
        return res

def indexTOpagamento(index_pagamento: int) -> tipoPagamento:
    '''Recebe um número que é referente a uma forma de pagamento e associa esse número a `tipoPagamento` correspondente.'''

    res: tipoPagamento
    if index_pagamento == 0:
        res = tipoPagamento.PIX
    elif index_pagamento == 1:
        res = tipoPagamento.CAR
    else: 
        res = tipoPagamento.DIN
    return res

def nova_venda(base_de_dados: dados) -> str:
    '''Essa função executa todo o processo de uma nova venda, ela recebe por meio de input do teclado qual o tipo de 
    cliente, quantos tickets da venda e qual a forma de pagamento. E ao final da operação, chama uma função que armazena
    os dados da venda em 'base_de_dados'. Caso execute o DocTest para esse função, forneça 0 para primeira entrada, 10 
    para a segunda e 1 para a terceira e última entrada.
    '''

    print('NOVA VENDA')
    imprimeTabelas(0)
    index_cliente: int = int(input('Qual é o tipo do cliente? (0,1,2,3 ou 4): '))

    tip_cliente: tipoCliente = indexTOcliente(index_cliente)
    tickets: int = int(input('Quantos tickets o cliente deseja comprar? '))

    sub_total: int = valor_ticket(tip_cliente)*tickets

    print(f'\n{tickets} tickets no valor de R${valor_ticket(tip_cliente)}. \nValor à pagar: R${sub_total}.')
    imprimeTabelas(1)

    index_pagamento: int = int(input('Qual seria a forma de pagamento? (0,1 ou 2): '))
    tip_pagamento: tipoPagamento = indexTOpagamento(index_pagamento)

    armazena_venda(sub_total, tickets, tip_pagamento, tip_cliente, base_de_dados)


# Funções para gerar *RELATÓRIO* ------------------------------------------------------------------------------------

def ascii_in_line(number: int, total: int) -> str:
    '''Recebe um certo valor 'number' que é obrigatóriamente menor que 'total', e a função retornará uma gráfico em
    string ascii ('=') com a proporção do 'number' pelo 'total' em porcentagem no final do gráfico. Nesse gráfico,
    cada barra representa 5% por cento, podendo ser arredondado caso não seja multiplo de 5.
    >>> ascii_in_line(20,34)
    '[============        ] 58.8%'
    >>> ascii_in_line(23,78)
    '[======              ] 29.5%'
    '''
    percent: float = 100*number/total
    Nspaces: int = round((100-percent)/5)
    Nbars: int = round(percent/5)
    spaces: str = Nspaces*' '
    bars: str = Nbars*'='
    return f'[{bars}{spaces}] {percent:.1f}%'

def graph_ascii(tickets_clientes: quantidadeCliente, total_ticket: int) -> str:
    '''Recebe a um conjunto composto que está armazenando o número de tickets vendidos para cada tipo cliente pela
    input 'tickets_clientes' do tipo quantidadeCliente e imprime no terminal um gráfico em ASCII com quantos por centos dos tickets foram 
    vedidos para cada tipo de cliente.
    >>> meusClientes: quantidadeCliente = quantidadeCliente(12,4,2,4,1)
    >>> graph_ascii(meusClientes, 23)
    Aluno       [==========          ] 52.2%
    Servidor<=3 [===                 ] 17.4%
    Servidor>3  [==                  ] 8.7%
    Docentes    [===                 ] 17.4%
    Externo     [=                   ] 4.3%
    <BLANKLINE>
    '''

    print(f'Aluno       {ascii_in_line(tickets_clientes.alu, total_ticket)}')
    print(f'Servidor<=3 {ascii_in_line(tickets_clientes.ser, total_ticket)}')
    print(f'Servidor>3  {ascii_in_line(tickets_clientes.se3, total_ticket)}')
    print(f'Docentes    {ascii_in_line(tickets_clientes.doc, total_ticket)}')
    print(f'Externo     {ascii_in_line(tickets_clientes.ext, total_ticket)}\n')

def graph_unicode(pagamento: quantidadePagamento, total: int) -> str:
    '''Essa função escreve na tela um gráfico vertical em unicode block. Ele recebe em 'pagamento' uma entrada do tipo
    quantidadePagamento, onde está armazenado os dados da quantidade do valor vendido para cada tipo de forma de 
    pagamentos e recebe em 'total' a quantidade do valor total vendido. Esses dados serão processados pela função e
    irá imprimir um gráfico vertical onde mostra o percentual de cada forma de pagamento em relação ao valor total e 
    barras verticais sendo meio bloco representando 5% e um bloco inteiro representando a soma de dois meios blocos, 
    sendo assim representa 10%.
    >>> pagamentos: quantidadePagamento = quantidadePagamento(23,72,19) 
    >>> graph_unicode(pagamentos, 114)
                    63.2%                 
                    ▄▄▄▄▄                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
        20.2%       █████                 
        █████       █████        16.7%
        █████       █████        ▄▄▄▄▄
        █████       █████        █████
        █████       █████        █████
    |    PIX    |  CARTÃO   |  DINHEIRO   |
    '''

    bar_code: str = '\u2588'
    halfBar_code: str =  '\u2584'
    pix: int = pagamento.pix
    car: int = pagamento.car
    din: int = pagamento.din

    percentPix: float = 100*pix/total
    percentCar: float = 100*car/total
    percentDin: float = 100*din/total
    formatPercentPix: str = f'{percentPix:.1f}%'
    formatPercentCar: str = f'{percentCar:.1f}%'
    formatPercentDin: str = f'{percentDin:.1f}%'
    if len(formatPercentPix) < 5:
        formatPercentPix = f'0{percentPix:.1f}%'
    if len(formatPercentCar) < 5:
        formatPercentCar = f'0{percentCar:.1f}%'
    if len(formatPercentDin) < 5:
        formatPercentDin = f'0{percentDin:.1f}%'
    

    layerPix: int = round(percentPix/5)
    layerCar: int = round(percentCar/5)
    layerDin: int = round(percentDin/5)
    
    maxLayer: int = 0

    if layerPix>layerCar and layerPix>layerDin:
        maxLayer = layerPix
    elif layerCar>layerPix and layerCar>layerDin:
        maxLayer = layerCar
    else: 
        maxLayer = layerDin

    for i in range(maxLayer+1, 0, -1):
        if layerPix+1 == i:
            print(f'    {formatPercentPix}   ', end='')
        elif i <= layerPix:
            if i == layerPix and layerPix % 2 != 0:
                print(f'    {halfBar_code*5}   ', end='')
            else:
                print(f'    {bar_code*5}   ', end='')
        else:
            print('            ', end='')

        if layerCar+1 == i:
            print(f'    {formatPercentCar}   ', end='')
        elif i <= layerCar:
            if i == layerCar and layerCar % 2 != 0:
                print(f'    {halfBar_code*5}   ', end='')
            else:
                print(f'    {bar_code*5}   ', end='')
        else:
            print('            ', end='')
        
        if layerDin+1 == i:
            print(f'     {formatPercentDin}')
        elif i <= layerDin:
            if i == layerDin and layerDin % 2 != 0:
                print(f'     {halfBar_code*5}')
            else:
                print(f'     {bar_code*5}')
        else:
            print('              ')
    print('|    PIX    |  CARTÃO   |  DINHEIRO   |')

def relatorio(base_de_dados: dados) -> None:
    '''Essa função imprime um das vendas que contém: Número total de tickets vendidos; número total da receita de 
    tickets vendidos; um gráfico horizontal em ASCII que mostra a porcentagem de tickets vendido para cada tipo
    de cliente em relação ao número total de tickets vendido e mostra um gráfico vertical em unicode block que 
    mostra a porcentagem do valor vendido de tickets para cada tipo de forma de pagamento em relação ao valor total de
    tickets vendidos.
    >>> meusClientes: quantidadeCliente = quantidadeCliente(12,4,2,4,1)
    >>> pagamentos: quantidadePagamento = quantidadePagamento(23,72,19)
    >>> meusDados: dados = dados(pagamentos, meusClientes, 23, 114)
    >>> relatorio(meusDados)
    RELATÓRIO
    <BLANKLINE>
    Total de tickets: 23
    Total de receita: R$114
    <BLANKLINE>
    Aluno       [==========          ] 52.2%
    Servidor<=3 [===                 ] 17.4%
    Servidor>3  [==                  ] 8.7%
    Docentes    [===                 ] 17.4%
    Externo     [=                   ] 4.3%
    <BLANKLINE>
                    63.2%                 
                    ▄▄▄▄▄                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
                    █████                 
        20.2%       █████                 
        █████       █████        16.7%
        █████       █████        ▄▄▄▄▄
        █████       █████        █████
        █████       █████        █████
    |    PIX    |  CARTÃO   |  DINHEIRO   |
    Precione ENTER quando estiver pronto...
    '''

    print('RELATÓRIO\n')
    print(f'Total de tickets: {base_de_dados.total_ticket}')
    print(f'Total de receita: R${base_de_dados.total_valorVendido}\n')
    graph_ascii(base_de_dados.total_cliente, base_de_dados.total_ticket)
    graph_unicode(base_de_dados.total_pagamentos, base_de_dados.total_valorVendido)
    
    command: int = input('Precione ENTER quando estiver pronto...')


# MAIN =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def main():
    limp()
    dadosRU: list = []
    print('Bem vindo ao sistema de controle de vendas do restaurante univesitário da UEM!')

    while True:
        imprimeTabelas(2)
        modo: str = input('Selecione o serviço (V, R ou S): ').upper()

        if modo == 'V':
            limp()
            nova_venda(dadosRU)
        elif modo == 'R':
            limp()
            if dadosRu.total_valorVendido != 0 and dadosRu.total_ticket != 0:
                relatorio(dadosRU)
        elif modo == 'S':
            break
        limp()

if __name__ == "__main__":
    main()
