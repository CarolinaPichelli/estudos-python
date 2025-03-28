n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2 ) + (n2 * 3 ) + (n3 * 4 ) + (n4 * 1 ))/10

if media >= 7:
    print(f'Media: {media:.1f}')
    print(f'Aluno aprovado.')
elif media >= 5 and media <= 6:
    print(f'Media: {media:.1f}')
    print(f'Aluno em exame.')
    ne = float(input())
    mediafinal = (media + ne)/2
    if mediafinal >= 5:
        print(f'Nota do exame: {ne:.1f}')
        print(f'Aluno aprovado.')
        print(f'Media final: {mediafinal:.1f}')
    else:
        print(f'Nota do exame: {ne:.1f}')
        print(f'Aluno reprovado.')
        print(f'Media final: {mediafinal:.1f}')
else:
    print(f'Media: {media:.1f}')
    print(f'Aluno reprovado.')
