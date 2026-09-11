def calcular_media(nota1,  nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media > 7:
        situacao = "Aprovado"
    elif media >= 5 and media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao

media, resultado = calcular_media(10, 5, 8)
print(f"A sua media é: {media:.2f}")
print(f"Voce está: {resultado}")