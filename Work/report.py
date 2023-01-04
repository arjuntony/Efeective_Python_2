from file_parse import parse_csv
from product import Product
from table_format import TableFormatter, create_formater
from inventory import Inventory


def read_prices(filename:str) ->dict:
    '''
    Read prices from the file
    :param filename: str
    :return: dict
    '''

    with open(filename) as FH:
        return dict(parse_csv(FH, types=[str, float], has_headers=False))


def read_inventory(filename, **opts):
    '''
    Reads the inventory of the items form the given file
    :param filename: str
    :return: list of dict
    '''

    #**opts packing and unpacking dict
    with open(filename) as FH:
        # invdict =  parse_csv(FH, select=["name", "quant", "price"], types=[str, int, float], **opts)
        # my_inv = Inventory(None)
        # for p in invdict:
        #     pr = Product(**p)
        #     my_inv.append(pr)
        # return my_inv

        return Inventory.from_csv(FH, **opts)


def make_report(pdcts, prices):
    '''
    Generates report(formatting) from given list of products and list of prices
    :param pdcts: list
    :param prices: dict
    :return: list
    '''
    result = list()
    for pdct in pdcts:  # Calling __iter__ in Inventory Class
        name = pdct.name
        quant = pdct.quant
        latest_price = prices[pdct.name]
        change = latest_price - pdct.price
        item = (name, quant, latest_price, change)
        result.append(item)
    return result


def print_report(report, formatter):
    '''
    Print the report in tabular manner
    :param report: str
    :return: none
    '''
    headers = ("Name", "Quant", "Price", "Change")
    # print("%10s %10s %10s %10s" % headers)
    # print((("-" * 10 + " ") * len(headers)))
    formatter.headings(headers)
    for name, quant, price, change in report:
        price = '\u20B9' + f"{price:>0.2f}"
        rowdata = [name, str(quant), f"{price:s}", f"{change:>0.2f}"]
        formatter.row(rowdata)


def inventory_report(inv_file, price_file, fmt='xml'):
    '''
    A common function to stitch all other function and call
    :param inv_file: str
    :param price_file: str
    :return: none
    '''
    inventory = read_inventory(inv_file)
    prices = read_prices(price_file)
    report = make_report(inventory, prices)
    formatter = create_formater(fmt)
    print_report(report, formatter)


def main(argv):
    import logging
    logging.basicConfig(
        filename = 'app.log',
        filemode = 'a',
        level = logging.DEBUG,
        format='%(asctime)s %(filename)s %(message)s'
    )
    if len(argv) < 3:
        raise SystemExit("Usage: {} inv_file pricefile format(xt csv hml)".format(argv[0]))
    inv_file = argv[1]
    pricefile = argv[2]

    try:
        format = argv[3]
    except IndexError as e:
        format = "txt"

    inventory_report(inv_file, pricefile, format)

if __name__ == "__main__":
    import sys
    main(sys.argv)
