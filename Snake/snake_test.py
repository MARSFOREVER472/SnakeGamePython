import turtle # LIBRERÍA PARA UN VIDEOJUEGO.
import time # LIBRERÍA PARA TEMPORIZADOR.

delay = 0.1

wn = turtle.Screen() # PANTALLA DEL JUEGO INCLUIDO DESDE UNA LIBRERÍA.

wn.title("SNAKE GAME") # TÍTULO DEL JUEGO.

wn.setup(width=600, height=600) # TAMAÑO DE LA VENTANA DEL JUEGO (ANCHO * ALTURA).

wn.bgcolor("yellow") # COLOR DE FONDO DEL JUEGO.

# AJUSTES DE LA CABEZA PARA LA SERPIENTE.

# OBJETO "Turtle".

head = turtle.Turtle()

# PARA QUE SE QUEDE FIJO:

head.speed(0)

# FIGURA DE LA SERPIENTE.

head.shape('square')

# COLOR DE LA CABEZA.

head.color('green')

# PARA NO DEJAR RASTROS DE LA ANIMACIÓN DE LA SERPIENTE.

head.penup()

# CENTRO DE LA CABEZA.

head.goto(0, 0)

# PARA HACER QUE EL PROGRAMA ESPERE A QUE YO LE DE A OTRA DIRECCIÓN.

head.direction = "stop"

def mov():
    if head.direction == "Up":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.ycor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES ARRIBA.

        head.sety(y + 10)

    if head.direction == "down":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.ycor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES ABAJO.

        head.sety(y - 10)

    if head.direction == "right":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.xcor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES A LA DERECHA.

        head.setx(y + 10)

    if head.direction == "left":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.xcor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES A LA IZQUIERDA.

        head.setx(y - 10)

def dirUp(): # SE VA HACIA ARRIBA.
    head.direction = "Up"

# CONECTAR CON EL TECLADO MEDIANTE TECLAS DE ARRIBA, ABAJO, IZQUIERDA O DERECHA.

wn.listen() # DETECTA BOTONES DEL TECLADO MEDIANTE UNA VARIABLE.
wn.onkeypress(dirUp, "Up") # SE PRESIONA LA TECLA DE MOVER HACIA ARRIBA.


while True:
    wn.update()
    mov()
    time.sleep(delay)

turtle.done() # EL PROGRAMA SE EJECUTA CORRECTAMENTE.

