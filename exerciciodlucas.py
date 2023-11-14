palavra1 = input().upper()
palavra2 = input().upper()
a = 0


for palavra in palavra1:
    if palavra.isalpha() is True:
        if palavra1.count(palavra) != palavra2.count(palavra):
            a = 1
            break
        else:
            a = a

if a == True:
    print("yes")
else:
    print("no")
