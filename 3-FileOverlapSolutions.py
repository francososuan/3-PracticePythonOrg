def filetolist(file):
    list_return = []
    with open(file) as f:
        line = f.readline()
        while line:
            list_return.append(int(line))
            line = f.readline()
    return list_return

prime_nums = filetolist("primenum.txt")
happy_nums = filetolist("happynum.txt")

overlaplist = [element for element in prime_nums if element in happy_nums]
print(overlaplist)
