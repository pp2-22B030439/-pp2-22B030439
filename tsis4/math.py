'''import math
degree=float(input())
radian=degree*(math.pi/180)
print(radian)
'''
'''
base_1 = 5
base_2 = 6
height = float(input())
base_1 = float(input())
base_2 = float(input())
area = ((base_1 + base_2) / 2) * height
print(area)
'''
'''
import math
n_sides = int(input())
s_length = float(input())
p_area = n_sides * (s_length ** 2) / (4 * math.tan(math.pi / n_sides))
print(round(p_area, 2))
'''
'''
a=float(input())
b=float(input())
S=a*b
print(round(S, 2))
'''
'''
import json
jsondata = open('sample-data.json').read()
aasas=json.loads(jsondata)
print("=======================================================================================" "\n"
      "DN                                                 Description           Speed    MTU" "\n"
      "-------------------------------------------------- --------------------  ------  ------"
      )
imdata = aasas["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0} {1} {2} {3}".format(dn,descr,speed,mtu))
        if dn=="topology/pod-1/node-201/sys/phys-[eth1/35]":
            break
   '''     

