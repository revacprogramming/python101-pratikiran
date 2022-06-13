def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def main():
  print('INPUT\n')
  inst = int(input('Enter Instances - '))
  ans = list()
  for i in range(0, inst):
    x = inho()
    inp = add_eg_frac(x)
    ans.append(outgoing(x, inp))
  print('\nOUTPUT\n')
  print(*ans, sep = '\n')

def outgoing(data, ans):
  ans = str(str(ans[0])+'/'+str(ans[1]))
  temp = list()
  for l in data:
      p = '1/'+ str(l)
      temp.append(p)
  s = ''
  for f in temp:
    if s != '':
      s = s +' + '+ f
    else:
      s = s + f
  s = s + ' = ' + ans
  return s

def inho():
  n = int(input('Enter how many unit frac - '))
  frac = input('Enter frac - ')
  frac = frac.split()
  data = list()
  for i in range(0, n):
    frac[i] = int(frac[i])
    data.append(frac[i])
  return data

def add_eg_frac(data):
  # finding the denominator 
  den = 1
  for z in range(0, len(data)):
    den = den * data[z]
  # finding the numerator
  num = 0
  for j in range(0, len(data)):
    temp = 1
    for k in range(0, len(data)):
      if data[j] != data[k]:
        temp = temp * data[k]
    num += temp
  # taking GCD
  temp_gcd = gcd(num, den)
  num = int(num/temp_gcd)
  den = int(den/temp_gcd)
  return ([num, den])

main()