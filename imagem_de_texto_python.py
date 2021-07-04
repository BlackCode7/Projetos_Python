from pywhatkit import image_to_ascii_art


entrada = 'python.png'
saida_image = 'ascii_python.txt'

print(image_to_ascii_art(imgpath=entrada, output_file=saida_image))