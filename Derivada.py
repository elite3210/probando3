
def f(x):
    return (1/3)*(x+3)**4+x

def diff(x):
    # <---calcula la primera derivada de la funcion--->
    dx = 0.00001
    return (f(x + dx) - f(x))/dx

def diff2(x):
    #<---calcula la segunda deriva en el punto x, se puede incluir en la funcion de primera derivada--->
    h = 0.0001
    return (diff(x+h)-diff(x))/h


def raiz(n):
    #<---Hallamos raiz de funcion con metodo de newton raphson--->
    x0 = n
    Df = f(x0)
    while Df != 0.0:
        x1 = x0 - f(x0)/diff(x0)
        x0 = x1
        Df = f(x1)
    return x0

def optimiza(n):

#<----- esta primera parte la funcion calcula la primera derivada  y encuentra las races de la funcion----->
    x0 = n
    Df = f(x0)
    while Df != 0.0:
        x1 = x0 - f(x0) / diff(x0)
        x0 = x1
        Df = f(x1)
#<--- hallamos el minimo global hallando la raiz de de la funcion derivada
    y0 = x0
    Df = diff(y0)
    while Df != 0.0:
        y1 = y0 - diff(y0) / diff2(y0)
        y0 = y1
        Df = diff(y1)
    return y0


print(f(2))
print(diff(2))
print('segunda derivada es: ',diff2(2))
print('Una raiz es: ', round(raiz(-1),2))
print('Un punto optimo es: ', round(optimiza(-1),2))
