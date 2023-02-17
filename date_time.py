def date():
    import datetime
    n = datetime.datetime.now
    return (str(n().date()))

def time():
    import datetime
    n = datetime.datetime.now
    return str(n().time())