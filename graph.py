from dataclasses import dataclass

@dataclass 
class quantidadePagamento:
    pix: int = 0
    car: int = 0 
    din: int = 0



def graph_unicode(pagamento: quantidadePagamento, total: int) -> None:
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

    for i in range(round(maxLayer/2)+1, 0, -1):
        if round(layerPix/2)+1 == i:
            print(f'    {formatPercentPix}   ', end='')
        elif i <= layerPix/2:
            if i == round(layerPix/2) and layerPix % 2 != 0:
                print(f'    {halfBar_code*5}   ', end='')
            else:
                print(f'    {bar_code*5}   ', end='')
        else:
            print('            ', end='')

        if round(layerCar/2)+1 == i:
            print(f'    {formatPercentCar}   ', end='')
        elif i <= layerCar/2:
            if i == round(layerCar/2) and layerCar % 2 != 0:
                print(f'    {halfBar_code*5}   ', end='')
            else:
                print(f'    {bar_code*5}   ', end='')
        else:
            print('            ', end='')
        
        if round(layerDin/2)+1 == i:
            print(f'     {formatPercentDin}')
        elif i <= layerDin/2:
            if i == round(layerDin/2) and layerDin % 2 != 0:
                print(f'     {halfBar_code*5}')
            else:
                print(f'     {bar_code*5}')
        else:
            print('              ')
    print('|    PIX    |  CARTÃO   |  DINHEIRO   |')

pagamentos = quantidadePagamento(79, 22, 56)
graph_unicode(pagamentos, 157)