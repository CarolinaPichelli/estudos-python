a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print(f'aguia')
        else:
            print(f'pomba') 
    else:
        if c == 'onivoro':
            print(f'homem')
        else: 
            print(f'vaca')
else:
    if b == 'inseto':
        if c == 'hematofago':
            print(f'pulga')
        else:
            print(f'lagarta')
    else:
        if c == 'hematofago':
            print(f'sanguessuga')
        else:
            print(f'minhoca')