from tkinter import *

root = Tk()

def resetfun():
    canvas.delete("a")

def graphit():
    global x 
    global n
    
    try:
        xval = float(entline.get())
        nval = float(entline2.get())
        x = xval
        n = nval
    except:
        print('nope!')

    eithereq()

def cx(x):
    return x+250

def cy(y):
    return 250-y

def eithereq():
    if n==1:
        canvas.create_line(cx(-250),cy(-250*x + 5*b),cx(250),cy(x*250 + 5*b),fill="red",width=3,tag = 'a') #Linear check
    else:
        insco = [cx(-250),cy(pow(-250*x,n) + 5*b)] #other power
        for i in range(50):
            insco.append(cx(-250 + 10*(i+1)))
            insco.append(cy((pow((-250 + 10*(i+1))*x,n) + 5*b)))
        canvas.create_line(insco,fill="red",width=3,tag = 'a')        

frame1 = Frame(root,width=60,height=100)
canvas = Canvas(root, width=500,height=500)
buttongraph = Button(frame1, text = "graph", command = graphit)
buttonclear = Button(frame1, text = "reset", command = resetfun)

entline = Entry(frame1, width=5)
entline2 = Entry(frame1, width=5)
canvas.pack()
frame1.pack()
entline.focus_set()
entline2.focus_set()
entline.pack(side = LEFT,padx=5)
entline2.pack(side=LEFT,pady=5)
buttonclear.pack(padx=5,side=RIGHT)
buttongraph.pack(padx=3,side=RIGHT)

x = 0
b = 0
n = 0

canvas.create_line(250,500,250,0,fill="black",width=3)
canvas.create_line(0,250,500,250,fill="black",width=3)

root.mainloop()