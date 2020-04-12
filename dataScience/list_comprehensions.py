print( sum( v for v in {'a': 1, 'b':2, 'c': 3}.values() ) )

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]