# COLOR RULES
size(600,600)
background(1,1,1)
try:
    colors = ximport("colors")
except ImportError:
    colors = ximport("__init__")
    reload(colors)

var("H", NUMBER, 0.55, 0.0, 1.0)
var("S", NUMBER, 1.0, 0.0, 1.0)
var("B", NUMBER, 0.6, 0.0, 1.0)
clr = colors.hsb(H, S, B)

x = 10
y = 30

for name in colors.rules:
    
    transform(CORNER)
    translate(x, y)
    rotate(-90)
    push()
    fill(0,0,0)
    text(name, x+45, 250-x, fontsize=14)
    pop()
    reset()

    scheme = colors.rule(name, clr)
    scheme.swatch(x, y)
    x += 55

# Each of the names in colors.rules
# is also a command in the library, try out:
#scheme = colors.right_complement(clr)
#scheme.swarm(50,50)
