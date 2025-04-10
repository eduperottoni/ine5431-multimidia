"""
Prática II de INE5429 - SISTEMAS MULTIMÍDIA
Estudantes:
    - Eduardo Dani Perottoni - 21204003

Para executar o código, é necessário instalar a biblioteca Pillow.

```
pip install -r requirements.txt
```

Tendo a biblioteca no ambiente, execute:

```
python praticaii.py
```

"""

from urllib.request import urlopen
from PIL import Image  # package pillow


def resize_image(img: Image) -> Image:
    """Reduz a imagem em 3/4"""
    new_width = int(img.width * 0.25)
    new_height = int(img.height * 0.25)
    reduced_img = Image.new("RGB", (new_width, new_height))
    for i in range(new_width):
        for j in range(new_height):
            pixel = img.getpixel((i * 4, j * 4))
            reduced_img.putpixel((i, j), pixel)

    return reduced_img


def scale_in_gray(img: Image) -> Image:
    """Transforma a imagem em tons de cinza"""
    gray_img = Image.new("L", (img.width, img.height))
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            gray_value = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
            gray_img.putpixel((i, j), gray_value)

    return gray_img


def transform_in_binary(img: Image) -> Image:
    """Transforma a imagem em binária (preto e branco)"""
    img_in_gray_scale = scale_in_gray(img)
    binary_img = Image.new("1", (img.width, img.height))
    for i in range(img.width):
        for j in range(img.height):
            pixel = img_in_gray_scale.getpixel((i, j))
            if pixel > 127:
                binary_img.putpixel((i, j), 1)
            else:
                binary_img.putpixel((i, j), 0)

    return binary_img


def get_rgb_channels(img: Image) -> tuple:
    """Retorna os canais RGB da imagem"""
    r, g, b = [Image.new("RGB", (img.width, img.height)) for _ in range(3)]
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            r.putpixel((i, j), (pixel[0], 0, 0))
            g.putpixel((i, j), (0, pixel[1], 0))
            b.putpixel((i, j), (0, 0, pixel[2]))
    return r, g, b


circle_img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/circle.png"))


# ATIVIDADE 1 -> Reduzir a imagem para 1/4 do seu tamanho original
reduced_img = resize_image(circle_img)
reduced_img.show()

# ATIVIDADE 2 -> Transformar a imagem em tons de cinza
gray_scaled_img = scale_in_gray(circle_img)
gray_scaled_img.show()

# ATIVIDADE 3 -> Transformar a imagem em binária (preto e branco)
binary_img = transform_in_binary(circle_img)
binary_img.show()

# ATIVIDADE 4 -> Separar os canais RGB da imagem
for i in get_rgb_channels(circle_img):
    i.show()
