def sub(arr, start, len):
    return arr[start:(start+len)]

def uniq(seq):
    seen = set()
    result = []
    for e in seq:
        if e in seen: continue
        seen.add(e)
        result.append(e)

    return result

def unpack(str):
    return long(str.encode('hex'), 16)

def odd(upto):
    return range(1, upto + 1, 2)

def even(upto):
    return range(0, upto + 1, 2)
