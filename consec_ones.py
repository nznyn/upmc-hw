#solve "most consecutive ones" using lambda function

f = lambda x: len(max(x.split('0')))


print(f('1011101101'))
print(f('11111'))
print(f('000000'))
print(f('101'))
print(f(''))

