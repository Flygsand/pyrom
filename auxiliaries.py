def sub(arr, start, len):
    return arr[start:(start+len)]

def uniq(iter):
    return (x for x in set(iter))

def unpack(str):
    return long(str.encode('hex'), 16)

def odd(upto):
    return range(1, upto + 1, 2)

def even(upto):
    return range(0, upto + 1, 2)

def unispace(str):
    return ' '.join(str.split())

def istrip(str):
    return str.replace(' ', '')
