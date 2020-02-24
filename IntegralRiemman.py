from math import sin, sqrt
# Integracion numerica
def f(x):
    return sin(x**2)


def diff(x):
    h = 0.0001
    return (f(x+h)-f(x))/h


def diff2(x):
    h = 0.0001
    return (diff(x+h)-diff(x))/h


def intervalos(x_min, x_max, e):
    a = x_min
    b = x_max
    c = (x_max-x_min)/2
    return round(sqrt(((b-a)**3*abs(diff2(c)))/(12*e)))


def integralIzquierdo(x_min,x_max,n):             # Integral definida con rectangulos internos
    dx = (x_max-x_min)/n
    area_total = 0.0
    x = x_min
    for i in range(n):
        area_total += f(x) * dx
        x += dx
    return round(area_total,2)


def integralDerecho(x_min,x_max,n):
    dx = (x_max-x_min)/n
    area_total = 0.0
    x = x_min
    for i in range(n):
        area_total += f(x + dx) * dx
        x += dx
    return round(area_total,2)


def integralTrapecio(x_min,x_max,e):                   # Integral definida con trapecios
    n = intervalos(x_min, x_max, e)
    dx = (x_max-x_min)/n
    area_total = 0.0
    x = x_min
    for i in range(n):
        area_total += (1/2) * (f(x) + f(x + dx)) * dx
        x += dx
    return area_total


print('rango en punto 2 es: ',round(f(2),3))
print('primera derivada en punto 2 es: ',round(diff(2),3))
print('segunda derivada en punto 2 es: ',round(diff2(2),3))
print('numero de intervalos = ', intervalos(0, 6, 0.01))
print('integral de 0 a 6 error = 0.01 es: ',round(integralTrapecio(0,1.7,0.001),4))

