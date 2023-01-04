def filematch(filename, substr):
    with open(filename, "r") as FH:
        for line in FH:
            if substr in line:
                yield line

'''
>>> for line in filematch(filename,"MINT"):
...     print(line, end =" ")
...
"MINT",200,51.23
 "MINT",50,65.10
 >>>
'''