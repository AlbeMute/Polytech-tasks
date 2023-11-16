'''
To introduce the problem think to my neighbor who drives a tanker truck. 
The level indicator is down and he is worried because he does not know if he will be able to make deliveries. 
We put the truck on a horizontal ground and measured the height of the liquid in the tank.

Fortunately the tank is a perfect cylinder and the vertical walls on each end are flat. 
The height of the remaining liquid is h, the diameter of the cylinder base is d, the total volume is vt (h, d, vt are positive or null integers). 
You can assume that h <= d.

Could you calculate the remaining volume of the liquid? 
Your function tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor) of your float calculation.
'''

import math

def tankvol(h, d, vt):
    radius = d / 2
    height = h

    if h >= d:
        return vt

    if h > radius:
        height = radius

    segment_area = radius**2 * math.acos((radius - height) / radius) - (radius - height) * math.sqrt((2 * radius * height) - (height**2))
    liquid_volume = vt * segment_area / (math.pi * radius**2)

    return int(round(liquid_volume))

print(tankvol(40, 120, 3500))  # Expected output: 1021
print(tankvol(60, 120, 3500))  # Expected output: 1750
print(tankvol(80, 120, 3500))  # Expected output: 2478












