from classes import *
from items import *

#special case and order for starting location




#instantiate ALL locations, connecting them and adding attributes will occur later
#test = location()

a1 = location()
a2 = location()
a3 = location()
a4 = location()
a5 = location()
b1 = location()
b2 = location()
b3 = location()
b4 = location()
b5 = location()
c1 = location()
c2 = location()
c3 = location()
c4 = location()
c5 = location()
d1 = location()
d2 = location()
d3 = location()
d4 = location()
d5 = location()
e1 = location()
e2 = location()
e3 = location()
e4 = location()
e5 = location()




#connect ALL locations here
#a1.east = a2         a2.west = a1

#first column vertical connections
a1.north = b1
b1.north = c1
c1.north = d1
d1.north = e1

e1.south = d1
d1.south = c1
c1.south = b1
b1.south = a1

#second column vertical connections
a2.north = b2
b2.north = c2
c2.north = d2
d2.north = e2

e2.south = d2
d2.south = c2
c2.south = b2
b2.south = a2

#third column vertical connections

a3.north = b3

c3.north = d3
d3.north = e3

e3.south = d3

c3.south = b3
b3.south = a3

#fourth col vert con

a4.north = b4
b4.north = c4
c4.north = d4
d4.north = e4

e4.south = d4
d4.south = c4
c4.south = b4
b4.south = a4

#fifth col vert con

a5.north = b5
b5.north = c5

c5.south = b5
b5.south = a5

#first (bottom) row lateral connections

a1.east = a2
a2.east = a3
a3.east = a4
a4.east = a5

a5.west = a4
a4.west = a3
a3.west = a2
a2.west = a1

#second row lat con

b1.east = b2
b2.east = b3
b3.east = b4
b4.east = b5

b5.west = b4
b4.west = b3
b3.west = b2
b2.west = b1

#third row lat con

c1.east = c2
#c2.east = c3
#c3.east = c4
c4.east = c5

c5.west = c4
#c4.west = c3
#c3.west = c2
c2.west = c1

#4th row lat con

d1.east = d2
d2.east = d3
d3.east = d4
d4.east = d5

d5.west = d4
d4.west = d3
d3.west = d2
d2.west = d1

#fifth row lat con

e1.east = e2
e2.east = e3
e3.east = e4
e4.east = e5

e5.west = e4
e4.west = e3
e3.west = e2
e2.west = e1



























#apply all greetings here attributes in next section
a3.greeting = "ROVER:This is your docking station. To the south is an ir0n fence extending in the West and East directions beyond current LidoVision range. \
to the North is more flat rubble. The same is true of the East and West. I am surrounded by rubble."




















#b4.greeting = "Whatever"

a1.hasmineral = True


