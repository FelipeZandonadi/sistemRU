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