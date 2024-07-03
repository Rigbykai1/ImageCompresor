from PIL import Image
import os
import time


def compress_image(input_image_path, output_image_path, quality=85):
    with Image.open(input_image_path) as img:
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')
        img.save(output_image_path, "JPEG", quality=quality) if output_image_path.lower().endswith(
            '.jpg') else img.save(output_image_path, "PNG", optimize=True, compress_level=9)


def compress_images_in_directory(input_directory, output_directory, quality=85):
    if not os.path.exists(input_directory) or not os.listdir(input_directory):
        print("La carpeta de entrada está vacía o no existe.")
        time.sleep(2)
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        input_image_path = os.path.join(input_directory, filename)
        output_image_path = os.path.join(
            output_directory, os.path.splitext(filename)[0] + '.jpg')

        try:
            compress_image(input_image_path, output_image_path, quality)
            print(f"Imagen guardada exitosamente en {output_image_path}.")
        except Exception as e:
            print(f"No se pudo comprimir la imagen {input_image_path}: {e}")
    time.sleep(2)


if __name__ == "__main__":
    quality = int(input("Elige la calidad de la imagen (0-100): "))

    current_directory = os.getcwd()
    input_directory = os.path.join(current_directory, "ImagenesPesadas")
    output_directory = os.path.join(current_directory, "ImagenesComprimidas")

    compress_images_in_directory(input_directory, output_directory, quality)
