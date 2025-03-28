nome = input()
salfixo = float(input())
totalvendas = float(input())

bonus = totalvendas * 0.15
salbonus = salfixo + bonus

print(f'TOTAL = R$ {salbonus:.2f}')