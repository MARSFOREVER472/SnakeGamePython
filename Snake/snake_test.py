import turtle # LIBRERÍA PARA UN VIDEOJUEGO.
import time # LIBRERÍA PARA TEMPORIZADOR.
import random # LIBRERÍA ALEATORIA.

delay = 0.1

wn = turtle.Screen() # PANTALLA DEL JUEGO INCLUIDO DESDE UNA LIBRERÍA.

wn.title("SNAKE GAME") # TÍTULO DEL JUEGO.

wn.setup(width=600, height=500) # TAMAÑO DE LA VENTANA DEL JUEGO (ANCHO * ALTURA).

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

# CONFIGURACIÓN DE LA COMIDA:

food = turtle.Turtle() # LA COMIDA SE APRECIARÁ EN LA VENTANA DEL JUEGO.
food.speed(0) # VELOCIDAD DE LA COMIDA.
food.shape("circle") # LA FORMA DE LA COMIDA LO DEJARÉ POR DEFECTO EN UN CÍRCULO.
food.color("Red") # EL COLOR DE LA COMIDA SERÁ RELLENADO CON COLOR ROJO.
food.penup() # DIBUJAREMOS LA COMIDA EN LA VENTANA DEL JUEGO.
food.goto(0, 100) # LA COMIDA SERÁ POSICIONADA EN X = 0 E Y = 100.
food.direction = "Stop" # INTERRUMPE LA EJECUCIÓN DE SU COMIDA.

def mov():
    if head.direction == "Up":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.ycor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES ARRIBA.

        head.sety(y + 10)

    if head.direction == "Down":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.ycor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES ABAJO.

        head.sety(y - 10)

    if head.direction == "Right":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.xcor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES A LA DERECHA.

        head.setx(y + 10)

    if head.direction == "Left":

        # ALMACENAR EL VALOR ACTUAL DE LA COORDENADA EN "Y".

        y = head.xcor()

        # EL MOVIMIENTO DE LA CABEZA ES 10 VECES A LA IZQUIERDA.

        head.setx(y - 10)

def dirUp(): # SE VA HACIA ARRIBA.
    head.direction = "Up"

def dirDown(): # SE VA HACIA ABAJO.
    head.direction = "Down"

def dirRight(): # SE VA HACIA LA DERECHA.
    head.direction = "Right"

def dirLeft(): # SE VA HACIA LA IZQUIERDA.
    head.direction = "Left"

# CONECTAR CON EL TECLADO MEDIANTE TECLAS DE ARRIBA, ABAJO, IZQUIERDA O DERECHA.

wn.listen() # DETECTA BOTONES DEL TECLADO MEDIANTE UNA VARIABLE.
wn.onkeypress(dirUp, "Up") # SE PRESIONA LA TECLA DE MOVER HACIA ARRIBA.
wn.onkeypress(dirDown, "Down") # SE PRESIONA LA TECLA DE MOVER HACIA ABAJO.
wn.onkeypress(dirRight, "Right") # SE PRESIONA LA TECLA DE MOVER HACIA LA DERECHA.
wn.onkeypress(dirLeft, "Left") # SE PRESIONA LA TECLA DE MOVER HACIA LA IZQUIERDA.


while True:
    wn.update() # ACTUALIZA EL PROGRAMA.

    # ACIERTA A CUALQUIER POSICIÓN DE LAS COMIDAS SI LA PUNTUACIÓN QUE COLISIONA CON ELLAS MISMAS ES MENOR QUE 20 PUNTOS.

    if head.distance(food) < 20:
        x = random.randint(-280, 280) # COMIDA MEDIANTE POSICIÓN EN X.
        y = random.randint(-280, 280) # COMIDA MEDIANTE POSICIÓN EN Y.
        food.goto(x, y)


    mov() # LLAMA AL MÉTODO DE MOVER SU CABEZA.
    time.sleep(delay) # DUERME EL PROGRAMA DURANTE 0.1 FRAMES POR SEGUNDO.

turtle.done() # EL PROGRAMA SE EJECUTA CORRECTAMENTE.

