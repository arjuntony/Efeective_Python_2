class Formaterror(Exception):
    # print(("Unknown Format"))
    pass

def create_formater(name):

    fmt_dict =    {
        "txt": TextTableFormatter,
        "csv": CSVTableFormatter,
        "html": HTMLTableFormatter

    }
    def f():
        raise Formaterror("Unknown Format")

    return fmt_dict.get(name, f)()

    # if name == 'txt':
    #     formatter = TextTableFormatter()
    # elif name == 'csv':
    #     formatter = CSVTableFormatter()
    # elif name == 'html':
    #     formatter = HTMLTableFormatter()
    # else:
    #     raise RuntimeError("Unknown Format")
    #
    # return formatter


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        :param headers:
        :return:
        '''

        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of data
        :param rowdata:
        :return:
        '''

        raise NotImplementedError()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("HTML Headers <br>{}</br>".format(headers))

    def row(self, rowdata):
        print("HTML Rows", rowdata)


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(('-'*10 + " ") * len(headers))

    def row(self, rowdata):
        for field in rowdata:
            print(f"{field:>10s}", end=" ")
        print()