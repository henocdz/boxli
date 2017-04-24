import string

def base_convert(number, base):
    digs = string.digits + string.ascii_letters + '-_'
    digits = []
    while number:
        digits.append(digs[number % base])
        number //= base
    return ''.join(digits)
