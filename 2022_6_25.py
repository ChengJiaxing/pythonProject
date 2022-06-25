# symbols="fsjdalkfsd"
# codes=[]
# for symbol in symbols:
#     codes.append(ord(symbol))
# print(codes)

#another

# symbols="asfdjsafl"
# codes=[ord(symbol) for symbol in symbols]
# print(codes)

# x='ABC'
# dummy=[ord(x) for x in x]
# print(x)
# print(dummy)

# symbols="afdfa"
# beyond_ascii=[ord(s) for s in symbols if ord(s)>100]
# print(beyond_ascii)
# beyond_ascii=list(filter(lambda c:c>100,map(ord,symbols)))
# print(beyond_ascii)
# beyond_ascii=list(filter(lambda c:c>90,map(ord,symbols)))
# print(beyond_ascii)

# colors=['black','white']
# sizes=['S','M','L']
# tshirts=[(color,size) for color in colors for size in sizes]
# print(tshirts)
#
# for color in colors:
#     for size in sizes:
#         print(color,size)

# symbols="agfdg"
# symbols_tuple=tuple((ord(symbol)for symbol in symbols))
# print(symbols_tuple)
# import array
# symbols_array=array.array('I',(ord(symbol)for symbol in symbols))
# print(symbols_array)

colors=['black','white']
sizes=['S','M','L']
for tshirt in ('%s %s'%(color,size)for color in colors for size in sizes):
    print(tshirt)


