from __future__ import division 
from visual import * 

scene.width =1024 
scene.height = 760 

#CONSTANTS 
G = 6.7e-11 
mEarth = 6e24 
mcraft = 15e3
mMoon = 7e22 
deltat = 60
pscale = 40000

#OBJECTS AND INITIAL VALUES
Moon = sphere(pos=vector(0,4e8,0), radius=1.75e6, color=color.white)
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan) 
craft = sphere(pos=vector(-13e7, 6.5e7,0),radius =3e6, color=color.yellow) 
vcraft = vector(0,0,0) 
pcraft = mcraft*vcraft 
trail = curve(color=craft.color)    ## craft trail: starts with no points 
t = 0 
scene.autoscale = 0       ## do not allow camera to zoom in or out
parr = arrow(color=color.green)

#CALCULATIONS 
while t < 10*365*24*60*60: 
    rate(200)       ## slow down motion to make animation look nicer
    r = vector(craft.pos - Earth.pos)
    rmag = sqrt((r.x**2)+(r.y**2)+ (r.z**2))
    rhat = vector(r.x/rmag,r.y/rmag,r.z/rmag)
    pcraft = pcraft + -G*((mMoon*mcraft)/(rmag**2))*rhat*deltat
    pcraft = pcraft + -G*((mEarth*mcraft)/(rmag**2))*rhat*deltat## you must add statements for the iterative update of 
    craft.pos = craft.pos + (pcraft/mcraft)*deltat## gravitational force, momentum, and position 
    if rmag < Earth.radius: ## check to see if the spacecraft has crashed on the Earth. 
        break ## if so, get out of the calculation loop 
    
    trail.append(pos=craft.pos) ## this adds the new position of the spacecraft to the trail 
    t = t+deltat 
print( 'Calculations finished after '),t,#('"seconds'")
