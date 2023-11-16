import turtle # LIBRERÍA PARA UN VIDEOJUEGO.

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

head.direction = "up"

turtle.done() # EL PROGRAMA SE EJECUTA CORRECTAMENTE.

