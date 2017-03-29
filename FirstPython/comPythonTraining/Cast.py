tmax = 22
tmin = 3
ttrans = 1
i = 1

print('Iniciar con los procesos')

while True:
    ttotal = (ttrans + tmin) * i
    i += 1

    if ttotal < tmax:
        print('Minutos usados despues de la entrega: %s' % ttotal)
        print('Siguiente proceso')
    else:
        print('Ir al proceso A')

    if ttotal >= tmax:
        break


