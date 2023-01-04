import csv
import sys
from report import read_inventory

def inventory_cost(filename):
    # with open(filename) as FH:
    #     rows = csv.reader(FH)
    #     headers = next(rows)
    #     total = 0.0
    #     for num, row in enumerate(rows, start =1):
    #         pdct = dict(zip(headers, row))
    #         try:
    #             quant = int(pdct["quant"])
    #             price = float(pdct["price"])
    #             total += quant * price
    #         except ValueError as e:
    #             print("Row {} Could not convert : {}".format(num,row))
    # return total

    inv = read_inventory(filename)
    # total = 0.0
    # for p in inv:
    #     total += p.quant * p.price
    return inv.total_cost()


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/inventory.csv"

    result = inventory_cost(filename)
    print(result)


if __name__ == "__main__":
    import sys
    main(sys.argv)
