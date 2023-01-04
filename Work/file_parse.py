import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=",", silence_errors=False):
    '''
    Parse the csv file if not a list of records
    :param filename: str
    :return:
    '''
    if select and not has_headers:
        raise RuntimeError("Select Requires Column Headers")

    rows = csv.reader(lines, delimiter= delimiter)
    if has_headers:
        headers = next(rows)
    else:
        headers = []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = list()
    for num, row in enumerate(rows, start =1):
        if not row:
            continue

        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    # print("Row {} Could not convert : {}".format(num, row))
                    # print("Row {} : Reason {}".format(num, e))
                    log.warning("Row %d Could not convert : %s" % (num,row))
                    log.debug("Row %d : Reason %s" %(num,e))
                continue
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records