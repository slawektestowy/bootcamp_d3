def formatuj(*args, **kwargs):
    napis = '\n'.join(args)
    for i in kwargs:
        napis = napis.replace(f"${i}", str(kwargs[i]))
    return napis

print(formatuj("tu jakis $napis", "jakis innny $napis", napis="asdf"))