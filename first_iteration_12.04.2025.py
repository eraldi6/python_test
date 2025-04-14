import turtle


def square(turtle,x):
    turtle.down()
    for i in range(4):
        turtle.fd(x)
        turtle.rt(90)
    turtle.up() 

def rect(turtle,x,y):
    turtle.down()
    for i in range(2):
        turtle.fd(x)
        turtle.rt(90)
        turtle.fd(y)
        turtle.rt(90)
    turtle.up()


alex=turtle.Turtle()
wn=turtle.Screen()



alex.up()
alex.setpos(-400,300)
alex.down()
alex.forward(0)


def sequence(turtle,lpx,lpy,nobx, noby,m,inn):   #lpx=x, lpy=y, nob=number of boxes, m=outter margin, i=inner margin 
    x_seq=(lpx-(2*m)-inn*(nobx-1))/nobx
    y_seq=(lpy-(2*m)-inn*(noby-1))/noby
    
    def row():
        for i in range(nobx):
            rect(turtle,x_seq,y_seq)
            if i==nobx-1:
                pass
            else:
                turtle.fd(x_seq)
                turtle.fd(inn)
    
    rect(turtle,lpx,lpy)
    turtle.forward(m)
    turtle.rt(90)
    turtle.fd(m)
    turtle.lt(90)
    home=turtle.pos()

    for i in range(noby):
        row()    
        turtle.setpos(home)
        turtle.rt(90)
        turtle.fd(y_seq)
        turtle.fd(inn)
        turtle.lt(90)
        home= turtle.pos()
    
    
sequence(alex, 800, 500, 5, 8, 20, 10)







wn.mainloop()
