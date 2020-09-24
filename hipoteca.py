# hipoteca.py
# Daniel T. Suarez - suarezdanieltomas@gmail.com
# Ejercicio 1.11: Hipoteca

saldo = 500000
tasa = 5/100
pago_mensual = 2684.11
adelanto = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
    
mes = 0
total_pagado = 0

print(f'{"Mes":^3} |{"Total":^10}|{"Saldo":^10}')
print('------------------------------------')

while saldo > 0:
#    mes += 1
    if saldo * (1+tasa/12) < pago_mensual: # Para corregir el ultimo mes
        total_pagado = total_pagado + saldo * (1+tasa/12)
        saldo = 0

    elif (mes <= pago_extra_mes_fin - 1) and (mes >= 
                                              pago_extra_mes_comienzo -1):
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    mes += 1
    print(f'{mes:^3} |{total_pagado:>10,.1f}|{saldo:>10,.1f}')

print(f'\nEl total a pagar es ${total_pagado:0.1f} en {mes} meses ({310/12:.1f} anios).')

#%%
# Solucion de Mati

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes_actual = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000


while saldo > 0:
    mes_actual = mes_actual + 1
    a_pagar = pago_mensual
    if (pago_extra_mes_comienzo <= mes_actual and 
            mes_actual <= pago_extra_mes_fin):
        print(mes_actual, "pago_extra")
        a_pagar = a_pagar + pago_extra
    # calculo el próximo saldo
    prox_saldo = saldo * (1+tasa/12)        
    if a_pagar > prox_saldo:
        print("Ultimo pago!!!")
        a_pagar = prox_saldo
    # y ahora lo que estaba antes
    saldo = saldo * (1+tasa/12) - a_pagar
    total_pagado = total_pagado + a_pagar

print('Total pagado', mes_actual,  round(saldo, 2), round(total_pagado, 2))