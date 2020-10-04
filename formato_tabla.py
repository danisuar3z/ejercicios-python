# -*- coding: utf-8 -*-

# formato_tabla.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 8.5: Un problema de extensibilidad


class FormatoTabla:

    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    '''
    Genera una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def fila(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    '''
    Genera una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, rowdata):
        print(','.join(rowdata))


class FormatoTablaHTML(FormatoTabla):
    '''
    Genera una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')


    def fila(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')


def crear_formateador(fmt):
    if fmt.upper() not in ['TXT', 'CSV', 'HTML']:
        raise RuntimeError(f'Format "{fmt}" not supported')

    if fmt.upper() == 'TXT':
        formateador = FormatoTablaTXT()
    elif fmt.upper() == 'CSV':
        formateador = FormatoTablaCSV()
    elif fmt.upper() == 'HTML':
        formateador = FormatoTablaHTML()

    return formateador


def imprimir_tabla(camion, headers, formateador):
    formateador.encabezado(headers)
    # tengo paja