from PIL import Image

def printASCIIart(asciiMatrix, col, row):
    for row in asciiMatrix:
        line = [p+p for p in row]
        print("".join(line))

def brightnessToASCII(brightnessValue):
    asciiThinToBold = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";
    asciiIndex = int((brightnessValue / 255) * (len(asciiThinToBold) - 1))
    return asciiThinToBold[asciiIndex]

def mapBrightnessToASCIIMatrix(brightness, col, row):
    asciiMatrix = [["" for x in range(col)] for y in range(row)] 
    for i in range(row):
        for j in range(col):
            asciiMatrix[i][j] = brightnessToASCII(brightness[i][j])
    return asciiMatrix

def convertRGBtoBrightness(pixels, col, row):
    brightnessMatrix = [[0 for x in range(col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            r, g, b = pixels[i][j]
            brightnessMatrix[i][j] = (r + g + b) / 3.0
    return brightnessMatrix

def main():
    imgName = "halo.jpg"
    img = Image.open(imgName)

    img.thumbnail((640, 480))
    pixels = list(img.getdata())
    pixels = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

    col, row = len(pixels[0]), len(pixels)
    print("Pixel matrix size:", col, "x", row)

    brightnessMatrix = convertRGBtoBrightness(pixels, col, row)
    asciiMatrix = mapBrightnessToASCIIMatrix(brightnessMatrix, col, row)
    printASCIIart(asciiMatrix, col, row)

if __name__ == '__main__':
    main()
