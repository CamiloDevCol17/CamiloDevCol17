import random
iterar = [1,2,3,4,5] 
for i in iterar:
    minus = "zxcvbnmasdfghjklñqwertyuiop"
    mayus ="ZXVBNMASDFGHJKLÑQWERTYUIOP"
    numb="1234567890"
    simbo=",.-}{}´+¿'|'"
    generate= minus + mayus + numb +simbo
    lenght = 9

    mail= ["@gmail.com","@Hotmail.com","@yahoo.com"]
    inicial = "".join(random.sample(minus, 10))
    nume= "".join(random.sample(numb, 5))
    num = inicial +nume
    mail2 = "".join(random.sample(mail, 1))
    mail3="".join(random.sample(mail, 1))
    generate2=num+mail3
    contraseña ="".join(random.sample(generate, lenght))
    print("El email generado es: ", generate2, "------La contraseña es: ", contraseña)
    