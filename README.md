def maior_bloco():
    compmax = 0
    n = int(input()) #numero de valores que ainda tem de ler
    elem = int(input()) #vslor que se esta a repetir
    n = n-1
    comp = 1 #comprimento do bloco corrente
    while n > 0:
        atual = int(input()) # vslor que acabou de ler
        n = n-1
        if atual == elem:
            comp += 1
        else:
            if comp > compmax:
                compmax = comp
                elemmax = elem
            comp = 1
            elem = atual
    if comp > compmax:
        compmax = comp
        elemmax = elem
    return elemmax, compmax

def divisores(n):
    n = int(input())
    print(1) # o 1 e divisor de todos os numeros
    for i in range(2,n+1):
        if n %i==0:
            print(i)
    print(n)
def conta_divisores(n):
    qtd= 0
    for i in range(1,n+1):
        if n%i==0:
            qtd +=1
    return qtd

def primo(k):
    if k == 1:
        return False
    else:
        if conta_divisores(k) == 2:
            return (1,k)
        else:
            return False

def imprime_primos():
    for k in range(2,21):
        if primo(k):
            print(k)

def sequencia(n): #n: 2,3,4,,4,,5,46,634
    for i in n:
        if primo(i):
            print(i)

def divisor(n):
    divisores = []
    for i in range(1,n+1):
        if n%i== 0:
            divisores.append(i)
    return divisores

def mdc(a,b):
    div_a = divisor(a) # 1 2 4 8
    div_b = divisor(b) # 1 2 3 4 6 12
    max_divisor = 0
    for x in div_a:
        if x in div_b:
            max_divisor = x
    return max_divisor

def fatorizar(n):
    lista_primos = []
    divisor = 2 #DIVISOR PRIMO MAIS BAIXO QUE EXISTE
    while divisor <= n:
        if n % divisor == 0:
            lista_primos.append(divisor) # ADICIONAR O DIVISOR DE N A LISTA ...
            n = n // divisor # 60//2 = 30 ATUALIZA O NUMERO N
        else:
            divisor += 1 #INCREMENTACAO DO DIVISOR: 2 -> 3 ...
    return lista_primos

def cravoErastotenes(): # retornar todos os primos de uma lista
    ''' 1 - criar uma lista de limite n
        2 - verificar quais desses sao primos e printa-los'''

    limite = int(input()) #valor maximo da lista
    lista_numeros = []
    for i in range(limite+1): #loop para criar lista com limite numeros
        lista_numeros.append(True) # dei valor true para identificar mais facilmente

    #colocar como false os numeros que nao sao primos
    for k in range(2, int(len(lista_numeros)//2)):#loop para percorrer metade da lista pois o primo do ultimo el da metade e o ult el da lista
        for j in range(2*k,len(lista_numeros),k):#loop para transformar os multiplos de 2k em falso: 2 3 4 5 6 7 8 9 10
            if lista_numeros[j] == True:
                lista_numeros[j] = False

    for h in range(len(lista_numeros)):#loop para retornar os valores True
        if h >=2:# esta  condicao esta aqui pois nao queremos o numero 0 1 da lista inicial
            if lista_numeros[h] == True:
                print(h)

def lista_primos(): #semelhante ao crivo
    n = int(input())
    o = []
    for i in range(n+1):
        o.append(i)
    for k in range(len(o)):
        if conta_divisores(k) == 2:
            print(k)


def horner_rule(coefficients, x):#avaliar polinomios de grau superior a 3
    result = coefficients[0]

    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]
        '''2x^3 -5x^3 +3x -7
            1a iteracao: coeficiente[0] = 2*x(2) -5 = -1
            2a iteracao: -1*x(2) +3 = 1
            3a iteracao: 1*x(2) -7 = -5

            2(2)^3 -5(2)^2 +3(2)-7 = 2*8-5*4 +6-7 = 16-20-1=-5'''
    return result

def matriz(l,c):
    matriz = [] # onde a matriz vai ficar
    for i in range(l): # loop pelas linhas
        linhas = [] # onde cada valor vai ficar das linhas
        for k in range(c): #loop pelas colunas
            valores = int(input())
            linhas.append(valores) #adicionar as linhas os valores
        matriz.append(linhas) # adicionar as linhas a matriz
    for row in matriz: # reestruturar a matriz
        print(row)

def print_diag(c):# imprimir a diagonal principal
    mat = [[1,2,-1],
           [3,1,+0],
           [0,1,-2]]
    for i in range(c):
        print(mat[i][i])

def soma_coluna(coluna): # somar os el de uma coluna
    mat = [[1,2,-1],
           [3,1,+0],
           [0,1,-2]]
    soma = 0
    # 1a = 4 2a = 4 3a = -3
    for i in range(len(mat)):
        soma += mat[i][coluna]
    return soma

def soma_tudo(mat,l,c):
    soma = 0
    for i in range(l):
        for j in range(c):
            soma += mat[i][j]
    return soma


def iguais(a,b,l,c):
    for i in range(l):
        for j in range(c):
            if a[i][j] != b[i][j]:
                return False
    return True


def txt():
    txt = 'Banana'
    for i in range(len(txt)):
        print(i) # B a n a n a

def primeira(ch,txt): # ver se uma letra esta na string se sim retorna a sua posicao senao retorna -1
    for i in range(len(txt)):
        if txt[i] == ch:
            return i
    return -1

def encaixa(x:str,y:str,i:int):
    '''verifica se x ocorre em y a partir da posição i,
    sabendo que i+len(x) <= len(y)
    'nana' encaixa em 'banana' apartir de certa posicao '''
    for k in range(len(x)):
        if x[k] != y[i+k]:
            return False
    return True

def subs(x,y): # se x esta em y retorna a posicao em que x comeca em y
    for i in range(len(y)+1):
        if encaixa(x,y,i):
            return i
    return -1

def imprime_nx(c:str,n:int): # repete c n vezes
    s = ""
    for i in range(n):
        s+= c
    print(s)

def codigosLetras(): #Escreve os codigos das letras
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in abc:
        print(c+": ", ord(c))
    print("\n")

    abc = "abcdefghijklmnopqrstuvxyz"
    for c in abc:
        print(c + ": ", ord(c))
    print("\n")

def codigosCaracteres(): # imprime os simbolos dos caracteres
    for i in range(33,128):
        print(i,":",chr(i))

def minuscula(c:str):
    if len(c) == 1 and c.islower(): # len(c) == 1 serve para verificar se c é apenas 1 caractere
         return True
    return False

def maiuscula(c:str):
    if len(c) == 1 and c.isupper():
        return True
    return False

def tudoMaiuscula(x:str): # igual para minuscula
    for i in x:
        if not maiuscula(i): # if not pois sem o not, se a primeira letra fosse maiuscula dava true
            return False
    return True


def min2mai(x:str): #converter sem usar is.upper() se for ao cont troca minuscula() e 'A' por 'a' e vice-versa
    resp = ""
    for i in x:
        if minuscula(i):
            novoc = chr(ord(i) + ord('A')-ord('a'))
        else:
            novoc = i
        resp += novoc
    return resp
#print(ord('A')-ord('a')) = -32
#print(ord('l') - 32) = 76
#print(chr(76)) = L

def converte10(x:str): #-> int: 'lucas'
    inteiro = 0
    for d in x:
        inteiro = inteiro*10 + ord(d) -ord('0') #0 + ord(l)-ord(0)+ ord(l)-ord(0)* 10 + ord(u) -ord(0)...
    return inteiro

def rodar(k:int, c:str):
    "Rodar um carater c por k posições."
    if c >= 'a' and c <= 'z':
        n = ord(c) - ord('a')
        return chr((n+k)%26 + ord('a'))
    return c


def cifrar(k,txt): #cifrar txt rodando k posicoes
    msg = ""
    for ch in txt:
        msg += rodar(k,ch)
    return msg

calores = [-1,2,3,4,23]
lists = [1+x**2 for x in calores] #1+(-1)^2 = 2 1+2^2 = 5 ....

multiplos_5_nao_3 = [x  for x in range(100)if x%5==0 and x%3!= 0]

def acrescentar(nome,email):
    agenda = [('Pedro Vasconcelos', 'pbv@dcc.fc.up.pt'),
('Pedro Brandão', 'pbrandao@dcc.fc.up.pt'),
('João Pedro Pedroso', 'jpp@dcc.fc.up.pt')]
    agenda.append((nome,email))
    return agenda

def procurar(txt):
    agenda = [('Pedro Vasconcelos', 'pbv@dcc.fc.up.pt'),
              ('Pedro Brandão', 'pbrandao@dcc.fc.up.pt'),
              ('João Pedro Pedroso', 'jpp@dcc.fc.up.pt')]
    emails  = []
    for c in agenda:
        if txt in c[0]:
            emails.append(c[1])
    return emails

inv = {'bananas':25,'laranjas':10,'peras':12}
#for chaves in inv.keys():
    #print(chaves)
# #for valores in inv.values():
    #print(values)
#for fruit,quant in inv.items():
    #print(fruit,quant)

def ler_ramos(r):
    ramos = {}
    while r > 0:
        i,j,v = map(int,input().split()) # I J SAO INICIO E FIM DO RAMO e V É comprimento
        ramos[(i,j)] = v
        r -= 1
    return ramos

def man_dic(k):
    dici = {}
    while k > 0:
        a,b = map(int,input().split())
        dici[(a)] = b
        k -= 1
    return dici

def compPercurso(percurso,grafo):
    compr = 0
    for k in range(len(percurso)-1): #PERCORRE O PERCURSO
        aresta = (percurso[k],percurso[k+1]) # UMA ARESTA +E O VALOR DE P0 A P1 -> A B OU B C OU A C OU B A -> CHAVE
        compr += grafo[aresta] #VALOR DA CHEVE INDICADA
    return compr

grafo = {('A', 'B'): 10, ('B', 'C'): 15, ('A', 'C'): 5,('B','A'): 7}
percurso = ['A', 'B', 'A','C'] # 10+7+5 = 22

def troca(vm,dm,n,q):
    i = 0
    while q > 0 and i < n: # 60 > 0 e 0 < len(vm)
        usar = q//vm[i] #nr notas utilizadas 60//50 = 1 usa 1 nota
        if usar > dm[i]: #1 nota > qtd de notas existentes usa todas as notas
            usar = dm[i] # usa todas notas
        q -= usar*vm[i] # 60 - nr notas * seu valor
        i += 1 # anda uma nota para a frente
    return q

vm = [200,100,50,20,10,5,2,1]
n = len(vm)
dm = [5,3,2,3,0,0,1,1]
q = 60
#print(troca(vm,dm,n,q))

def procurar_oc(txt,nomefich): #procurar txt num fcheiro
    f = open(nomefich, "r")
    n = 1
    while True:
        linha = f.readline()
        if txt in linha:
            print(n, linha)
        if linha == "":
            break
        n += 1
    f.close()

#import matplotlib.pyplot as plt

#x = [2,3,4,5,6,2] # se 1o == ult em x e y a curva fecha
#y = [1.5, 6.5,1,2,5,1.5]
#plt.plot(x,y)
#plt.xlabel('x') # legendas em x
#plt.ylabel('f(x)') # legenda em y
#plt.savefig("teste1.png") #salva a imagem
#plt.show()

def tentaabrir(fich):
    try:#tenta abrir o ficheiro e le-lo
        f = open(fich,"r")
        cont = f.read()
        f.close()
    except IOError:#se nao conseguir lanca o erro e o cont e vazio
        cont = ""
    return cont

def fatorial(n):
    if n < 0:
        raise ValueError("argumento negativo")
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def binarySearch(x,y): # x valor pretendido y lista de numeros ordenada
    a = 0 # limite inferior
    b = len(y)-1 #limite superior
    while a<=b:
        m = (a+b)//2 #ponto medio, serve de comparacao sempre
        if y[m] == x: #se o ponto medio da lista for = valor de x retorna m
            return m
        if y[m]<x: #
            a = m+1
        else:
            b=m-1
    return -1

def linearSearch(x,y):
    for i in range(len(y)):
        if y[i] == x:
            return i
    return -1

def bissect(f,a,b,tol):#vai dividindo sempre o intervalo a meio ate achar a solucao
    #se usar f troco o por lambda x: funcao
    while b-a < tol:
        m = (a+b)/2
        fm = f(m) #definir a funcao f
        if fm == 0:
            return m
        if fm*f(a) > 0: #se esta entre m e b
        #if fm*f(a)<0 -> se esta entre a e b
            a=m
        else:
            b=m
    return (a+b)/2

def selectionSort(): #organizar lista de ordem crescente ou decrescente
    numbers = [4,9,3,6,2]
    for i in range(len(numbers)): #loop para percorrer todos os numeros
        min_idx = i # prim el de numbers é o minimo
        for j in range(i+1,len(numbers)): #loop a partir do 2 elem
            if numbers[j] < numbers[min_idx]: # se o 2 el ... < que o 1 troca
                min_idx = j
        numbers[i],numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

def insertionSort():
    numbers = [4, 9, 3, 6, 2]
    for i in range(1,len(numbers)):#comecamos no 1 pq o primeiro é o i
        while numbers[i-1] > numbers[i] and i>0:# i = 3 i-1 = 9
            numbers[i-1],numbers[i] = numbers[i],numbers[i-1]
            i -= 1
    return numbers

def quickSort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()
    menors = []
    maiors = []
    for i in range(len(numbers)):
        if numbers[i] > pivot:
            maiors.append(numbers[i])
        else:
            menors.append(numbers[i])
    return quickSort(menors) + [pivot] + quickSort(maiors)

def bubbleSort():
    numbers = [4, 9, 3, 6, 2]
    ordenado = False
    while not ordenado:#enquanto ordenado for falso ele corre o programa
        ordenado = True # se ordenado for true ele assume que a lista esta ordenada
        for i in range(0,len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                ordenado = False#se ainda houve trocas possiveis e porque a lista nao esta ordenada
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i] # faz troca
    return numbers

class Retangle:
    '''classe para representar pontos no plano'''
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#box = Retangle(5,10)
#print(box.area())

class Fraction: #representar fracoes somar mult comparar...
    def __init__(self,num,denom):
        if denom == 0: # 2/0 = erro
            raise ValueError("denominador nao pode ser zero")
        if denom < 0: # 2/-3 = -2/3
            denom = -denom # -3 = -(-3) = 3
            num = -num #-3 = 3 ou 3 = -3
        d = mdc(abs(num),denom)
        self.num =num//d
        self.denom = denom//d

    def __str__(self):
        return "%d/%d" % (self.num,self.denom)

    def __add__(self,other):
        r = Fraction(self.num*other.denom + self.denom * other.num,self.denom*other.denom)
        return r

    def __mul__(self,other):
        j = Fraction(self.num*other.num,self.denom*other.denom)
        return j

    def __eq__(self,other):
        return self.num*other.denom == self.denom*other.num

    def __lt__(self,other):
        return self.num*other.denom < self.denom*other.num

    def __le__(self,other):
        return self.num*other.denom <= self.denom*other.num

    def __ne__(self,other):
        return self.num*other.denom != self.denom*other.num

    def __gt__(self,other):
        return self.num*other.denom > self.denom*other.num

    def __ge__(self,other):
        return self.num*other.denom >= self.denom*other.num
#v = Fraction(1,2)
#l = v.__ge__(Fraction(1,3))
#print(l)
#print(Fraction(-2,-4))
