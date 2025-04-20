from PIL import Image
import os
import time


def compress_image(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:
        compress_mode(output_image_path, img)


def compress_mode(output_image_path, img):
    ext = os.path.splitext(output_image_path)[1].lower()
    if ext in ('.jpg', '.jpeg'):
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')

        while True:
            try:
                quality = int(input("Elige la calidad de la imagen (0-100): "))
                if 0 <= quality <= 100:
                    break
                else:
                    print("Por favor, ingresa un valor entre 0 y 100.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        img.save(output_image_path, "JPEG", quality=quality)
    elif ext == '.png':
        while True:
            try:
                compress_level = int(
                    input("Elige el nivel de compresión (0-9): "))
                if 0 <= compress_level <= 9:
                    break
                else:
                    print("Por favor, ingresa un valor entre 0 y 9.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        img.save(output_image_path, "PNG", optimize=True,
                 compress_level=compress_level)
    else:
        img.save(output_image_path)


def compress_images_in_directory(input_directory, output_directory):
    if not os.path.exists(input_directory) or not os.listdir(input_directory):
        print("La carpeta de entrada está vacía o no existe.")
        time.sleep(2)
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        input_image_path = os.path.join(input_directory, filename)
        ext = os.path.splitext(filename)[1].lower()
        output_image_path = os.path.join(
            output_directory, os.path.splitext(filename)[0] + ext)

        try:
            compress_image(input_image_path, output_image_path)
            print(f"Imagen guardada exitosamente en {output_image_path}.")
        except Exception as e:
            print(f"No se pudo comprimir la imagen {input_image_path}: {e}")
    time.sleep(2)


if __name__ == "__main__":
    current_directory = os.getcwd()
    input_directory = os.path.join(current_directory, "ImagenesPesadas")
    output_directory = os.path.join(current_directory, "ImagenesComprimidas")

    compress_images_in_directory(input_directory, output_directory)
