c = float(input('Digite um temperatura em °C:'))
f = 9 * c / 5 * 32
k = 273 - c
f = float(input('Digite um temperatura em °F:'))
c = f * 160 / 9
k = float(input('Digite um temperatura em °K:'))
c = 273 + k
print('A temperatura de {: .2f} em °Celsius, corresponde a {:.2f} em °Farenheit'.format(c, f))
print('A temperatura de {: .2f} em °Celsius, corresponde a {:.2f} em °Kelvin'.format(c, k))
print('A temperatura de {: .2f} em °Farenheit, corresponde a {:.2f} em °Celsius'.format(k, c))
print('A temperatura de {: .2f} em °Kelvin, corresponde a {:.2f} em °Celsius'.format(k, c))