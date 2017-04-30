def baseconverter(number,base):
    s = []
    digits = "0123456789ABCDEF"

    while number > 0:
        rem = number % base
        s.append(rem)
        number = number // base

    baseconverted = ""

    while len(s) > 0:
        baseconverted = baseconverted + digits[s.pop()]
    print baseconverted

baseconverter(25,8)
baseconverter(256,16)
baseconverter(26,26)
