from __future__ import division
from visual import *

G = 6.7e-11
mplanet = 6e24 
mcraft = 15e3
Fscale = 40000

planet = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.yellow)
craft = sphere(pos=vector(-13e7, 6.5e7, 0), radius=3e6, color=color.red)
r = vector(craft.pos - planet.pos)
rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
Fmag = G*((mplanet*mcraft)/(rmag**2))
rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
Fnet = vector(-Fmag*rhat.x,-Fmag*rhat.y,-Fmag*rhat.z)
arr2 = arrow(pos=craft.pos, axis=Fnet*Fscale, color=color.yellow)

craft1 = sphere(pos=vector(-6.5e7, 6.5e7, 0), radius=3e6, color=color.red)
r = vector(craft1.pos - planet.pos)
rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
Fmag = G*((mplanet*mcraft)/(rmag**2))
rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
Fnet = vector(-Fmag*rhat.x,-Fmag*rhat.y,-Fmag*rhat.z)
arr2 = arrow(pos=craft1.pos, axis=Fnet*Fscale, color=color.yellow)

craft2 = sphere(pos=vector(0, 6.5e7, 0), radius=3e6, color=color.red)
r = vector(craft2.pos - planet.pos)
rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
Fmag = G*((mplanet*mcraft)/(rmag**2))
rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
Fnet = vector(-Fmag*rhat.x,-Fmag*rhat.y,-Fmag*rhat.z)
arr2 = arrow(pos=craft2.pos, axis=Fnet*Fscale, color=color.yellow)

craft3 = sphere(pos=vector(6.5e7, 6.5e7, 0), radius=3e6, color=color.red)
r = vector(craft3.pos - planet.pos)
rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
Fmag = G*((mplanet*mcraft)/(rmag**2))
rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
Fnet = vector(-Fmag*rhat.x,-Fmag*rhat.y,-Fmag*rhat.z)
arr2 = arrow(pos=craft3.pos, axis=Fnet*Fscale, color=color.yellow)

craft4 = sphere(pos=vector(13e7, 6.5e7, 0), radius=3e6, color=color.red)
r = vector(craft4.pos - planet.pos)
rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
Fmag = G*((mplanet*mcraft)/(rmag**2))
rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
Fnet = vector(-Fmag*rhat.x,-Fmag*rhat.y,-Fmag*rhat.z)
arr2 = arrow(pos=craft4.pos, axis=Fnet*Fscale, color=color.yellow)
print rmag
print Fmag
print rhat
print Fnet

