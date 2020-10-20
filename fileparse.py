# -*- coding: utf-8 -*-

# fileparse.py
# Daniel T. Suarez
# comma-separated-values file parser
# now supports tab separated values with parse='tab'


def parse_csv(list_obj, has_headers=True, select=None,
              types=None, silence_errors=False, parse='csv'):
    '''
    Parses csv lines returning a dictionary list or
    a tuple list if there\'s no headers.
    With select you can get only the columns you want
    if you have headers, and with types you can
    convert the value types for every row.
    Pass parse='tab' if your data is separated by tabs.
    '''

    # raise if has_headers=False and select!=None
    if select and not has_headers:
        raise RuntimeError('Can\'t use select if there\'s no headers.')

    if parse.lower() == 'csv':
        import csv
        rows = csv.reader(list_obj)
    if parse.lower() == 'tab':
        rows = (row.strip().split('\t') for row in list_obj)

    # Assign headers
    if has_headers:
        headers = next(rows)

    # Create indexes list, becomes like a select bool
    if select:  # headers=True is implicit bc of previous raise
        indexes = [headers.index(header) for header in select]
    else:
        indexes = []

    # Begin records out
    records = []

    # headers=False
    if not has_headers:

        # types=True
        if types:
            for i, row in enumerate(rows, 1):
                # Skip blank lines
                if not row:
                    continue
                try:
                    record = tuple([func(col) for func, col
                                    in zip(types, row)])
                    records.append(record)
                except ValueError:
                    if not silence_errors:
                        print(f'Error parsing line {i}. '
                              f'Did not understand {row}.')
        # types=False
        else:
            for row in rows:
                # Skip blank lines
                if not row:
                    continue
                record = tuple([col for col in row])
                records.append(record)
    # headers=True
    else:
        # selec=True
        if indexes:
            # types=True
            if types:
                for i, row in enumerate(rows, 1):
                    if not row:
                        continue
                    try:
                        record = {headers[index]: func(row[index])
                                  for index, func
                                  in zip(indexes, types)}
                        records.append(record)
                    except ValueError:
                        if not silence_errors:
                            print(f'Error parsing line {i}. '
                                  f'Did not understand {row}.')
            # types=False
            else:
                records = [{headers[index]: val for index, val
                            in zip(indexes, row)}
                           for row in rows]
        # selec=False
        else:
            # types=True
            if types:
                for i, row in enumerate(rows, 1):
                    try:
                        record = {header: func(val) for header, func, val
                                  in zip(headers, types, row)}
                        records.append(record)
                    except ValueError:
                        print(f'Error parsing line {i}. '
                              f'Did not understand {row}.')
            # types=False
            else:
                for row in rows:
                    if not row:
                        continue
                    record = {header: val for header, val
                              in zip(headers, row)}
                    records.append(record)
    return records
