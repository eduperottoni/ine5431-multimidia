''' 
INE5431 Sistemas Multim��dia
Prof. Roberto Willrich

Aula Pr�tica IV: Compress�o de Entropia

'''

from PIL import Image
from Cuif import Cuif
import math

def PSNR(original, decodificada, b):
    try:
        mse = MSE(original, decodificada) 
        psnr = 10*math.log10(((2**b-1)**2)/mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"


def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    sum_errors = 0
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
            sum_errors += ((ori_r - dec_r) ** 2 + (ori_g - dec_g) ** 2 + (ori_b - dec_b) ** 2)

    return sum_errors / nsymbols

if __name__ == "__main__":
    
    # Leitura da imagem 
    filepath = 'mandril.bmp'
    teste_filepath = "teste.bmp"

    mandril_img = Image.open(filepath)
    teste_img = Image.open(teste_filepath)
    
    # Indique a matr��cula dos alunos do grupo na lista abaixo
    matriculas = [21204003]
    
    # Gera��o do arquivo Cuif.1, converte o arquivo Cuif.1 em BMP, e calcula o PSNR
    cuif1 = Cuif(mandril_img, 1, matriculas)
    cuif1.printHeader()
    cuif1.show()
    cuif1.save('mandril1.cuif')
    cuif1.saveBMP('mandril1.bmp')
    img1 = Image.open('mandril1.bmp')

    # codificando test.bmp em CUIF1 => test1.bmp
    cuif1_test = Cuif(teste_img, 1, matriculas)
    cuif1_test.save("teste1.cuif")
    cuif1_test.saveBMP("teste1.bmp")
    teste1 = Image.open("teste1.bmp")

    print("------------PSNR do CUIF.1---------------")
    print(f"mandril {PSNR(mandril_img, img1, 8)}")
    print(f"teste {PSNR(teste_img, teste1, 8)}")

    cuif2_mandril = Cuif(mandril_img, 2, matriculas)
    cuif2_mandril.save("mandril2.cuif")
    cuif2_mandril.saveBMP("mandril2.bmp")

    cuif2_test = Cuif(teste_img, 2, matriculas)
    cuif2_test.save("teste2.cuif")
    cuif2_test.saveBMP("teste2.bmp")

    mandril2 = Image.open("mandril2.bmp")
    teste2 = Image.open("teste2.bmp")

    print("------------PSNR do CUIF.2---------------")
    print(f"mandril {PSNR(mandril_img, mandril2, 8)}")
    print(f"teste {PSNR(teste_img, teste2, 8)}")

    cuif3_mandril = Cuif(mandril_img, 3, matriculas)
    cuif3_mandril.save("mandril3.cuif")
    cuif3_mandril.saveBMP("mandril3.bmp")

    cuif3_test = Cuif(teste_img, 3, matriculas)
    cuif3_test.save("teste3.cuif")
    cuif3_test.saveBMP("teste3.bmp")

    mandril3 = Image.open("mandril3.bmp")
    teste3 = Image.open("teste3.bmp")

    print("------------PSNR do CUIF.3---------------")
    print(f"mandril {PSNR(mandril_img, mandril3, 8)}")
    print(f"teste {PSNR(teste_img, teste3, 8)}")

    cuif4_mandril = Cuif(mandril_img, 4, matriculas)
    cuif4_mandril.save("mandril4.cuif")
    cuif4_mandril.saveBMP("mandril4.bmp")

    cuif4_test = Cuif(teste_img, 4, matriculas)
    cuif4_test.save("teste4.cuif")
    cuif4_test.saveBMP("teste4.bmp")

    mandril4 = Image.open("mandril4.bmp")
    teste4 = Image.open("teste4.bmp")

    print("------------PSNR do CUIF.4---------------")
    print(f"mandril {PSNR(mandril_img, mandril4, 8)}")
    print(f"teste {PSNR(teste_img, teste4, 8)}")

    print("THE END")
