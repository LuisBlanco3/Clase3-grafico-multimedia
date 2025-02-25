from vpython import *
import asyncio
import random

scene = canvas(title="Combinación de Conceptos en VPython", width=800, height=600)

# variables de la posicon
posicion_original_cono = vector(-1, 0, 0)
posicion_original_cilindro = vector(2, 0, 0)

# colores
colores = [
    color.red, color.green, color.blue, color.yellow, color.cyan,
    color.magenta, color.orange, color.purple, color.black, color.white
]

def crear_conos_cilindro():
    tamaños = [(1, 1.5), (0.7, 1.2), (0.5, 1)]  # tamaño de los conos
    posiciones = [-1, 0, 1]  # posicion de cada cono
    
    conos = []
    for i in range(3):
        conos.append(cone(pos=vector(posiciones[i], 0, 0), axis=vector(0, tamaños[i][1], 0), radius=tamaños[i][0], color=color.orange))
    
    # un clon del primer cono
    clon_cono = cone(pos=vector(posiciones[0], 0, 0), axis=vector(0, tamaños[0][1], 0), radius=tamaños[0][0], color=color.orange)
    
    # tamaño del cilindro 
    base_cilindro = cylinder(pos=vector(2, 0, 0), axis=vector(0, 1, 0), radius=0.5, length=1, color=color.red)
    
    # un clon del cilindro 
    clon_cilindro = cylinder(pos=vector(2, 0, 0), axis=vector(0, 1, 0), radius=0.5, length=1, color=color.red)
    
    # unos 3 cilindros
    distancia = 1.5  # su separacion
    for i in range(1, 4):
        cylinder(pos=vector(2, i * distancia, 0), axis=vector(0, 1, 0), radius=0.5, length=1, color=color.red)
    
    return clon_cono, clon_cilindro

clon_cono, clon_cilindro = crear_conos_cilindro()

async def mover_objeto(objeto, direccion):
    while True:
        objeto.pos += direccion * 0.05
        await asyncio.sleep(0.1)

async def main():
    task1 = asyncio.create_task(mover_objeto(clon_cono, vector(1, 0, 0)))
    task2 = asyncio.create_task(mover_objeto(clon_cilindro, vector(1, 0, 0)))
    await asyncio.gather(task1, task2)

# al precionar la tecla R se reinicia a su posicion 
def teclas_presionadas(evt):
    if evt.key == 'r':
        clon_cono.pos = posicion_original_cono
        clon_cilindro.pos = posicion_original_cilindro
    elif evt.key == 'c':
        # cambion de color C
        clon_cono.color = random.choice(colores)
        clon_cilindro.color = random.choice(colores)

scene.bind('keydown', teclas_presionadas)

asyncio.run(main())
