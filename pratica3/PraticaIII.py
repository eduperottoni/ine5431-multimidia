from PIL import Image
from Cuif import Cuif
import math

def PSNR(original, decodificada, b):
    try:
        mse = MSE(original, decodificada) 

        if mse == 0:
            print('MSE => 0')
            return 0

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
    filepath = 'mandril.bmp'
    img = Image.open(filepath)
    matriculas = [21204003]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img, 2, matriculas)
    
    # imprime cabeçalho Cuif
    cuif.printHeader()
    
    # mostra imagem Cuif
    cuif.show()
    
    #gera o arquivo Cuif.1
    cuif.save('mandril2.cuif')
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    cuif1 = Cuif.openCUIF('mandril2.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    cuif1.saveBMP("mandril2.bmp")
    cuif1.show()
    
    img1 = Image.open("mandril2.bmp")

    psnr = PSNR(img, img1, 8)
    print(f'Cálculo do PSNR: {psnr}')