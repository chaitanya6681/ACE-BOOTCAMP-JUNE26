l_methods=[m for m in dir(tuple) if not m.startswith('__')]
for m in l_methods:
    print(m)

