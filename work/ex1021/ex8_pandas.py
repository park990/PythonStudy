from pandas import Series, DataFrame

comp1 = Series([30,20,10],index=['sk','kt','lg'])
comp2 = Series([10,50,30],index=['kt','lg','sk'])

hap = comp1+comp2
print("comp1+comp2:\n{}" .format(hap))