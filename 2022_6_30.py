# metro_areas=['Tokyo','JP',36.933,(34,56),
#              ('Delhi Ncr','IN',34,(32,13)),
#              ('Mexico City','MX',20,(19,-99)),
#              ('New York-Newark','US',20,(40,-74)),
#              ('Sao paulo','BR',20,(-23,-46))]
# print('{:15}|{:^9}|{:^9}'.format('','lat','long.'))
# fmt='{:15}|{9.4f}|{:9.4f}'
# for name,cc,pop,(latitude,longitude) in metro_areas:
#     if longitude<=0:
#         print(fmt.format(name,latitude,longitude))

from collections import namedtuple
import collections
City=namedtuple('City','name country population coordinates')
# tokyo=City('Tokyo','JP',36.933,(35.689722,139.691667))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(City._fields)
LatLong=namedtuple('LatLong','lat long')
delhi_data=('Delhi NCR','IN',21.935,LatLong(28.613889,77.208889))
delhi=City._make(delhi_data)
# print(delhi._asdict())
collections.OrderedDict([('name','Delhi NCR'),('country','IN'),('population',21.935),('coordinates',
LatLong(lat=28.613889,long=77.208889))])
for key,value in delhi._asdict().items():
    print(key+':',value)

