from math import *
import turtle as tr

def func(x):
    if -9 <= x < -5:
        return 2 - sqrt(4 - pow(x + 7, 2))
    elif -5 <= x <= -4:
        return 2
    elif -4 < x < 0:
        return -x / 2
    elif 0 <= x < pi:
        return 1 - 4 * pow(x - pi / 2, 2) / pow(pi, 2)
    else:
        return x - pi

def Axis(txy, ax='X'):
    
    min_value = txy[0]
    max_value = txy[1]
    tr.up()

    if (ax == 'X'):
        start = [min_value, 0]
        end = [max_value, 0]
    else:
        start = [0, min_value]
        end = [0, max_value]

    tr.goto(start)
    tr.down()
    tr.goto(end)

def Mark(txy, ax='X'):

     min_value = txy[0]
     max_value = txy[1]
     tr.up()

     for t in range(min_value, max_value):
         if (ax == 'X'):
             pb = [t, 0]
             pe = [t, 0.2]
             pw = [t, -0.5]
         else:
             pb = [0, t]
             pe = [0.2, t]
             pw = [0.2, t]

     tr.goto(pb)
     tr.down()
     tr.goto(pe)
     tr.up()
     tr.goto(pw)
     tr.write(str(t))

def Arrow(txy, ax='X'):

     a = [0.1, 0, -0.1]
     b = [-0.1, 0.3, -0.1]

     tr.up()
     tr.goto(0, 0) 
     tr.begin_poly()

     for i in range(2):
        tr.goto(a[i], b[i])

     tr.end_poly()
     p = tr.get_poly()

     tr.register_shape("myArrow", p)
     tr.resizemode("myArrow")
     tr.shapesize(1, 2, 1)

     if ax == 'X':
         tr.tiltangle(0)
         tr.goto(txy[1] + 0.2, 0)
         pw = [int(txy[1]), -1.0]
     else:
         tr.tiltangle(90)
         tr.goto(0, txy[1] + 0.2)
         pw = [0.2, int(txy[1])]

     tr.stamp()

     tr.goto(pw)
     tr.write(ax, font=("Arial", 14, "bold"))


def main():
     aX = [-9, 5]
     aY = [-1, 3]

     Dx = 800
     Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
     tr.setup(Dx, Dy)
     tr.reset()

     Nmax = 1000

     tr.setworldcoordinates(aX[0], aY[0],
     aX[1], aY[1])
     
     tr.title("Lab_10_1")
     tr.width(2)
     tr.color("blue", "blue")
     tr.ht()
     tr.tracer(0, 0)
     Axis(aX, 'X')
     Mark(aX, 'X')
     Arrow(aX, 'X')

     Axis(aY, 'Y')
     Mark(aY, 'Y')
     Arrow(aY, 'Y')

     tr.color("red")
     tr.width(3)
     dx = (aX[1] - aX[0]) / Nmax

     x = aX[0]
     y = func(x)

     if (y is None):
        tr.up()
        tr.goto(x, 0)
     else:
        tr.goto(x, y)
        tr.down()

     while x <= aX[1]:
         x = x + dx
         y = func(x)
         if (y is None):
            tr.up()
            continue
         else:
             tr.goto(x, y)
             tr.down()

if __name__ == "__main__":
    main()
    tr.mainloop()