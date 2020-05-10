from PIL import Image
from math import floor

def brightnessToASCII(brightnessValue):
    asciiThinToBold = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";
    asciiIndex = floor((brightnessValue / 255) * (len(asciiThinToBold) - 1))
    return asciiThinToBold[asciiIndex]

def mapBrightnessToASCIIMatrix(brightness):
    col, row = len(brightness), len(brightness[0])
    asciiMatrix = [["" for x in range(row)] for y in range(col)] 
    for i in range(col):
        for j in range(row):
            asciiMatrix[i][j] = brightnessToASCII(brightness[i][j])
    return asciiMatrix

def convertRGBtoBrightness(pixels, col, row):
    brightnessMatrix = [[0 for x in range(row)] for y in range(col)]
    for i in range(col):
        for j in range(row):
            r, g, b = pixels[i, j]
            brightnessMatrix[i][j] = (r + g + b) // 3
    return brightnessMatrix

def main():
    imageName = "Fernando_noronha.jpg"
    im = Image.open(imageName)
    col, row = im.size
    print("Pixel matrix size:", col, "x", row)

    pixels = im.load()
    brightnessMatrix = convertRGBtoBrightness(pixels, col, row)
    asciiMatrix = mapBrightnessToASCIIMatrix(brightnessMatrix)
    print(asciiMatrix)
    print(len(asciiMatrix))
    print(len(asciiMatrix[0]))

if __name__ == '__main__':
    main()
