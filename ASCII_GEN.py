from PIL import Image
import sys

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def main(image_path, x, y):
    try:
        image = Image.open(image_path)
        image = image.resize((int(width), int(height)))
        ascii_art = convert_to_ascii_art(image)
        save_as_text(ascii_art, image_path)
    except Exception as e:
        print(f"Error: {e}")


def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art


def convert_pixel_to_character(pixel):
    (r, g, b, a) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art, image_path):
    output_path = f"{image_path.split('.')[0]}.txt"
    with open(output_path, "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
    print(f"ASCII art saved to {output_path}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python ASCII_GEN.py <path_to_image> <width of desires ascii> <height of desired ascii>")
    else:
        image_path = sys.argv[1]
        width = sys.argv[2]
        height = sys.argv[3]
        main(image_path,width,height)