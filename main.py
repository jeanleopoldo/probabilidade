import math
import sys

UM_NUMERO_MUITO_GRANDE = math.pow(2, 31)-1
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
    print("media: {}".format(average))
    return average

def variancia(values):
    m   = media(values)
    sum = 0
    for index in range(len(values)):
        value = values[index]
        v     = abs(value - m)**2
        sum   = sum + v

    var = sum / (len(values)-1)
    print("variancia: {}".format(var))
    return var

def erro(e):
    return 1/(e**2)
def tam_populacao(N, epsilon):
    epsilon = epsilon/100
    e = erro(epsilon)
    print("erro: {}".format(e))
    ret = math.ceil((e*N)/(e+N))
    print("tam pop: {}".format(ret))
    
def erro_relativo(values):
    print("booh yah")
def desvio_padrao(values):
    var = variancia(values)
    desv = math.sqrt(var)
    print("desvio padrao: {}".format(desv))
    return desv

def erro_padrao(values):
    dp = desvio_padrao(values)
    ep = dp/len(values)
    print("erro padrao: {}".format(ep))
def curtosis(quartis, centris):
    Q = (quartis[1] - quartis[0]) / [centris[1]-centris[0]]
    return Q
def coeficiente_de_variacao(values):
    dp = desvio_padrao(values)
    m  = media(values)
    cv = abs(dp/m)*100
    print("c. variacao: {}".format(cv))

def moda(values):
    data = {}

    for i in range(len(values)):
        value = values[i]
        if not value in data:
            data[value] = 0
        amount = data[value]
        data[value] = (amount+1)
    
    limit = 0
    moda  = UM_NUMERO_MUITO_GRANDE
    for value in data:
        amount = data[value]
        if limit < amount:
            moda = value
            limit = amount

    print("moda: {}".format(moda))
    print("valor da moda: {}".format(limit))
    return moda


def mediana(values):
    values.sort()
    md = UM_NUMERO_MUITO_GRANDE
    index = int(len(values)/2)
    if len(values) % 2 == 0:
        v1 = values[index-1]
        v2 = values[index]

        md = (v1+v2)/2
    else:
        md = values[index]
    
    print("mediana: {}".format(md))


def coeficiente_de_assimetria(values):
    m  = media(values)
    mo = moda(values)
    dp = desvio_padrao(values)
    coef_ass = (m-mo)/dp
    print("c. assimetria: {}".format(coef_ass))

def surtges_n_classes(values):
    n = len(values)
    r = amplitude(values)
    value    = 1 + (3.322 * math.log10(n))
    interval = r/value
    print("numero de classes: {}".format(value))
    print("intervalo de classes: {}".format(interval))
    return interval
def n_classes(n):
    return math.sqrt(n)

def amplitude(values):
    values.sort()
    amp = values[len(values)-1] - values[0]
    print("amplitude dos dados: {}".format(amp))
    return amp

def print_sorted(values):
    values.sort()
    for i in range(len(values)):
        print(values[i])
def get_number_of_elements_in_class(values, init, fin):
    elements = []
    for i in range(len(values)):
        element = values[i]

        if element >= init and element < fin:
            elements.append(values[i])
    print("numero de elementos na classe: {}".format(len(elements)))



def ponto_medio_de_classe(i, f):
    n = (f - i)/2
    m = i + n
    print("ponto_medio_de_classe: {}".format(m))
if __name__ == "__main__":
    
    file = sys.argv[1]
    values = get_formatted_data(file)

    data_number = len(values)
    print("numero de dados: {}".format(data_number))
    media(values)
    variancia(values)
    desvio_padrao(values)
    surtges_n_classes(values)
    tam_populacao(len(values), 4)
    moda(values)
    mediana(values)
    coeficiente_de_assimetria(values)
    erro_padrao(values)
    coeficiente_de_variacao(values)
    # get_number_of_elements_in_class(values, 5.399, 5.579)
    # ponto_medio_de_classe(5.399, 5.579)
    # get_number_of_elements_in_class(values, 5.579, 5.759)
    # ponto_medio_de_classe(5.579, 5.759)
    # get_number_of_elements_in_class(values, 5.759, 5.939)
    # ponto_medio_de_classe(5.759, 5.939)
    # get_number_of_elements_in_class(values, 5.939, 6.119)
    # ponto_medio_de_classe(5.939, 6.119)
    # get_number_of_elements_in_class(values, 6.119, 6.299)
    # ponto_medio_de_classe(6.119, 6.299)
    # get_number_of_elements_in_class(values, 6.299, 6.479)
    # ponto_medio_de_classe(6.299, 6.479)
    # get_number_of_elements_in_class(values, 6.479, 6.659)
    # ponto_medio_de_classe(6.479, 6.659)
    # get_number_of_elements_in_class(values, 6.659, 6.839)
    # ponto_medio_de_classe(6.659, 6.839)
    # get_number_of_elements_in_class(values, 6.839, 7.019)
    # ponto_medio_de_classe(6.839, 7.019)
    # print_sorted(values)
    

    # surtges_n_classes(values)
    # n    = int(input("1-media\n2-variancia\n3-desvio padrao\n4-erro\n"))

    
    # # if n == 1:
    # med    = media(values)
    # print("media: {}".format(med))
    # # if n == 2:
    # var    = variancia(values)
    # print("variancia: {}".format(var))
    # # if n == 3:
    # desv   = desvio_padrao(values)
    # print("desvio padrao: {}".format(desv))
    # # if n == 4:
    # #     epsilon = float(input("informe erro a ser considerado:\n"))
    # #     pop     = float(input("informe o tamanho da populacao:\n"))
    # #     n = tam_populacao(pop, epsilon)
    # #     print(n)