numero1=int(float(input('Primera Calificacion: ')))
numero2=int(float(input('Segunda Calificacion: ')))
numero3=int(float(input('Tercera Calificacion: ')))
resultado=numero1+numero2+numero3/3
if resultado<6:
  print('reprobaste')
if resultado>=6:
  print('aprobado')
if resultado>=9:
  print('Felicidades, sacaste exelente calificacion')