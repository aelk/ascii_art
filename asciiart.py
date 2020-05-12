import sys
from PIL import Image

MAX_PIXEL_VALUE = 255;
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";

def printASCIIart(asciiMatrix, col, row):
    for row in asciiMatrix:
        line = [p+p+p for p in row]
        print("".join(line))

def mapBrightnessToASCIIMatrix(brightness, col, row):
    asciiMatrix = [["" for x in range(col)] for y in range(row)] 
    for i in range(row):
        for j in range(col):
            asciiIndex = int((brightness[i][j] / MAX_PIXEL_VALUE) * (len(ASCII_CHARS) - 1))
            asciiMatrix[i][j] = ASCII_CHARS[asciiIndex]
    return asciiMatrix

def convertRGBtoBrightness(pixels, col, row):
    brightnessMatrix = [[0 for x in range(col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            r, g, b = pixels[i][j]
            brightnessMatrix[i][j] = (r + g + b) / 3.0
    return brightnessMatrix

def main(fileName):
    img = Image.open(fileName)

    img.thumbnail((1000, 200))
    pixels = list(img.getdata())
    pixels = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

    col, row = len(pixels[0]), len(pixels)
    brightnessMatrix = convertRGBtoBrightness(pixels, col, row)
    asciiMatrix = mapBrightnessToASCIIMatrix(brightnessMatrix, col, row)
    printASCIIart(asciiMatrix, col, row)

if __name__ == '__main__':
    main(sys.argv[1])
