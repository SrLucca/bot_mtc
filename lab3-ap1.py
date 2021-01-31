x = int(input())

if x < 999 or x > 9999:
    while (x < 999 or x > 9999):
        x = int(input())

        if (x >= 1000 and x <= 9999):
            
            div = x/100
            mod_div = div%10
            sub = div - mod_div
            resto = x%1000

            soma = sub + resto

            potencia = soma * soma

            if potencia == x:
                print('Apresenta a característica')
            else:
                print('Não apresenta a característica')
else:
    div = x/100
    mod_div = div%10
    sub = div - mod_div
    resto = x%1000

    soma = sub + resto

    potencia = soma * soma

    if potencia == x:
        print('Apresenta a característica')
    else:
        print('Não apresenta a característica')
