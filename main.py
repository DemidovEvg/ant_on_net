# На белом поле размером 1024x1024 клеток, в позиции 512,512 находится “муравей”
#
# Муравей двигается по следующим правилам:
#
# * На белой клетке - поворачивает на 90° по часовой стрелке, инвертирует пиксель и перемещается вперед на одну клетку
# * На черной клетке - поворачиват на 90° против часовой стрелки, инвертирует пиксель и перемещается вперед на одну клетку
#
# Изначально муравей находится на белой клетке и смотрит вверх.
#
# Пришлите изображение пути муравья до границы поля в виде BMP или PNG файла глубиной цвета 1 бит и число черных клеток на нем.
#
# Программа должна минимизировать использование RAM
import numpy as np
from PIL import Image

from ant import Direction, Ant
from net import Net
from point import Point

net = Net(size=1024)
ant = Ant(position=Point(512, 512), direction=Direction.UP)

while not net.ran_away(ant.position):
    current_color = net.current_color(ant.position)
    net.invert_current_color_in(ant.position)
    ant.step(color=current_color)

image = Image.frombytes(mode='1', size=net.data.shape[::-1], data=np.packbits(net.data, axis=1))
image.save('ant_on_net.png')

print(net.black_count)
