# conversor de Medidas completo
m = float(input("Uma distância em metros: "))
cm = m * 100
mm = m * 1000
μm = m * 1e+6
nm = m * 1e+9
km = m / 1000
milha = m / 1609
Min = m / 1852
yd = m * 1.094
pé = m * 3.281
In = m * 39.37

print("{}m corresponde a {} cm e {} mm e {} km e {} jarda e {} pé e {} Polegada e {} Milha e {} Micrometro e {} Nanometro e {} Milha Nautica".format(m, cm, mm, km, yd, pé, In, milha, μm, nm, Min))

# Renato Barbosa
