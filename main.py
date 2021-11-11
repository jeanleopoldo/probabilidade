import math
import sys

def get_formatted_data(file_name):
    file = open(file_name)
    data = file.readlines()

    values = []

    for index in range(len(data)):
        value = data[index]
        value = float(value)
        values.append(value)
    
    return values

def media(values):
    sum = 0

    for index in range(len(values)):
        value = values[index]
        sum   = sum + value

    average = sum / len(values)
    return average

def variancia(values):
    m   = media(values)
    sum = 0
    for index in range(len(values)):
        value = values[index]
        v     = abs(value - m)**2
        sum   = sum + v

    var = sum / (len(values)-1)
    return var

def erro(e):
    return 1/(e**2)
def tam_populacao(N, epsilon):
    epsilon = epsilon/100
    e = erro(epsilon)
    return math.ceil((e*N)/(e+N))

def desvio_padrao(values):
    var = variancia(values)
    desv = math.sqrt(var)
    return desv

def surtges_n_classes(r, n):
    value = 1 + (3.322 * math.log10(n))

    return r/value
def n_classes(n):
    return math.sqrt(n)

if __name__ == "__main__":

    print(surtges_n_classes(9.4, 50))
    file = sys.argv[1]
    values = get_formatted_data(file)
    n    = int(input("1-media\n2-variancia\n3-desvio padrao\n4-erro\n"))

    
    if n == 1:
        med    = media(values)
        print("media: {}".format(med))
    if n == 2:
        var    = variancia(values)
        print("variancia: {}".format(var))
    if n == 3:
        desv   = desvio_padrao(values)
        print("desvio padrao: {}".format(desv))
    if n == 4:
        epsilon = float(input("informe erro a ser considerado:\n"))
        pop     = float(input("informe o tamanho da populacao:\n"))
        n = tam_populacao(pop, epsilon)
        print(n)