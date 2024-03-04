
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
import serial ,time

Puerto = 'COM5'

app = tk.Tk()
app.title("Python and arduino")
app.geometry("250x250")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

Comunicacion = serial.Serial(port=Puerto,baudrate=9600,)
time.sleep(2)
xs = [0]
ys = [1]

#definicion de la animacion 
def animar(i,xs,ys):
    valor= Comunicacion.readline()
    ValorString = str(valor,'UTF-8')
    ValorFloat = float(ValorString.strip())

    y = ValorFloat
    x = xs[-1] + 1
    
    xs.append(x)
    ys.append(y)

    ax.clear()
    ax.plot(xs,ys)

ani = animation.FuncAnimation(fig,animar, fargs=(xs,ys), interval = 300,cache_frame_data=False)

#Funcion que escribe Serialmente un valor que sera leido por el arduino.
def proceso(boton,accion):
    if boton== 1 and accion == "ON":
        Comunicacion.write(b'1')
    elif boton== 1 and accion == "OFF":
        Comunicacion.write(b'2')
    elif boton== 2 and accion == "ON":
        Comunicacion.write(b'A')
    elif boton== 2 and accion == "OFF":
        Comunicacion.write(b'B')
        
#propiedades de la app

Label1 = tk.Label(app,text="DIODO LED 1")
Label1.place(x=10,y=10)

Label2 = tk.Label(app,text="DIODO LED 2")
Label2.place(x=150,y=10)

b1on = tk.Button(app,text = 'encendido',bg = 'green',command = lambda: proceso(1,"ON"))
b1on.place(x=10,y=50)

b1off = tk.Button(app,text = 'apagado',bg = 'red',command = lambda: proceso(1,"OFF"))
b1off.place(x=10,y=100)

b2on = tk.Button(app,text = 'encendido',bg = 'green',command = lambda: proceso(2,"ON"))
b2on.place(x=150,y=50)

b2off = tk.Button(app,text = 'apagado',bg = 'red',command = lambda: proceso(2,"OFF"))
b2off.place(x=150,y=100)

plt.show()

app.mainloop()


