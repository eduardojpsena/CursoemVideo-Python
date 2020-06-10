'''Realizar conversao de °Celsius para °Fahrenheit e Kelvin.'''

print(">>>> CONVERSÃO DE TEMPERATURA <<<<")

c = float(input("Informe a temperatura em °C: "))
f = ((9*c)/5)+32
k = c + 273.15
print("A temperatura de {}°Celsius, corresponde a {}°Fahrenheit e {} Kelvin".format(c, f, k))
