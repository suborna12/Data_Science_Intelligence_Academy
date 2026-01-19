from itertools import groupby

def group_chars(data):
    grouped = {}
    for k, l in groupby(data):
        grouped[k] = list(l)
    return grouped

data = sorted('yaaaebbdcsdtfsjhdliutfejdfjtaahjgk')
print(group_chars(data))
