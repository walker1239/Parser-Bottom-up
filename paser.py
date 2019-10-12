table=[ [['T','X'],[],[],['T','X'],[],[]],
        [[],[],['+','E'],[],['e'],['e']],
        [['int','Y'],[],[],['(','E',')'],[],[]],
        [[],['*','T'],['e'],[],['e'],['e']]]

terminales=['int','(',')','*','+','$',]
indices={
  'T': 2,
  'E': 0,
  'X': 1,
  'Y': 3,
  'int': 0,
  '(': 3,
  ')': 4,
  '*': 1,
  '+': 2,
  'e': 6,
  '$': 5,
}

cadena=['(','int', '+', 'int',')','$']
c=0
i=0
b=0
temp=table[i][indices[cadena[c]]]
pila=[]
for u in temp:
  pila.append(u)
pila.append('$')
while 1:
  #print(pila,'|',cadena, '|',temp)
  if(pila[0] in terminales):
    if pila[0]=='$' and cadena[0]=='$':
      break
    elif pila[0]==cadena[0]:
      cadena.remove(cadena[0])
      pila.remove(pila[0])
      c+=1
      continue
    else:
      b=1
      break
  else:
    i=indices[pila[0]]
    temp=table[i][indices[cadena[0]]]
    pila.remove(pila[0])
    if len(temp)==0:
      b=1
      break
    pila.reverse()
    temp.reverse()
    for u in temp:
      pila.append(u)
    pila.reverse()
    temp.reverse()
    if(pila[0]=='e'):
      pila.remove('e')
  if len(pila)==0:
    break
if b:
  print('no funciona')
else:
  print('si')
