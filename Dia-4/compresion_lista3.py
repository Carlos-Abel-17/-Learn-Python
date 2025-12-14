temperatura_fahrenheit = [32, 212, 275]

grados_celsius = list((n-32)*(5/9) for n in temperatura_fahrenheit)

print(grados_celsius)