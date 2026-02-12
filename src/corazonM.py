import numpy as np
import matplotlib.pyplot as plt

N = 0   # negro (contorno)
R = 1   # rojo
O = 2   # rojo oscuro
B = 3   # blanco (brillo)
_ = -1  # vacio

heart = [
    [ _,  _,  N,  N,  N,  _,  _,  _,  N,  N,  N,  _,  _],
    [ _,  N,  R,  R,  R,  N,  _,  N,  R,  R,  R,  N,  _],
    [ N,  R,  R,  B,  R,  R,  N,  R,  R,  B,  R,  R,  N],
    [ N,  R,  B,  B,  R,  R,  R,  R,  R,  R,  R,  R,  N],
    [ N,  R,  R,  R,  R,  R,  R,  R,  R,  R,  R,  R,  N],
    [ N,  R,  R,  R,  R,  R,  R,  R,  R,  R,  R,  R,  N],
    [ _,  N,  R,  R,  R,  R,  R,  R,  R,  R,  R,  N,  _],
    [ _,  _,  N,  R,  R,  R,  R,  R,  R,  R,  N,  _,  _],
    [ _,  _,  _,  N,  R,  R,  R,  R,  R,  N,  _,  _,  _],
    [ _,  _,  _,  _,  N,  O,  R,  O,  N,  _,  _,  _,  _],
    [ _,  _,  _,  _,  _,  N,  O,  N,  _,  _,  _,  _,  _],
    [ _,  _,  _,  _,  _,  _,  N,  _,  _,  _,  _,  _,  _],
]

colores = {
    N: [20, 20, 20],
    R: [210, 30, 30],
    O: [160, 20, 20],
    B: [255, 255, 255],
}

filas = len(heart)
cols = len(heart[0])

imagen = np.ones((filas, cols, 3), dtype=np.uint8) * 240

for y in range(filas):
    for x in range(cols):
        if heart[y][x] != _:
            imagen[y, x] = colores[heart[y][x]]

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(imagen, interpolation='nearest')
ax.set_title('Corazón 8-bit — Graficación', fontsize=13, fontweight='bold', pad=12)
ax.axis('off')
plt.tight_layout()
plt.savefig('output/corazon_pixel.png', dpi=150, bbox_inches='tight', pad_inches=0.3)
print("Imagen guardada en output/corazon_pixel.png")
plt.show()