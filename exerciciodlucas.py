palavra1 = input().upper()
palavra2 = input().upper()
a = True


for palavra in palavra1:
    if palavra.isalpha() is True:
        if palavra1.count(palavra) != palavra2.count(palavra):
            a = False
            break
        else:
            a = a

if a is True:
    print("yes")
else:
    print("no")
