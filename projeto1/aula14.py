a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)

string2 = 'b={1} a={0} a={0} c={nome3:.2f}'
formato2 = string2.format(a, b, nome3=c)
print(formato2)