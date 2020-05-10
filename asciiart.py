from PIL import Image

def convertRGBtoBrightness(pixels, col, row):
    brightnessMatrix = [0] * (col * row)
    idx = 0
    for i in range(col):
        for j in range(row):
            r, g, b = pixels[i, j]
            brightnessMatrix[idx] = (r + g + b) // 3
            idx += 1
    return brightnessMatrix

def main():
    imageName = "Fernando_noronha.jpg"
    im = Image.open(imageName)
    col, row = im.size

    print("Successfully constructed pixel matrix!")
    print("Pixel matrix size:", col, "x", row)
    pixels = im.load()
    brightnessMatrix = convertRGBtoBrightness(pixels, col, row)
    print(brightnessMatrix)
    print(len(brightnessMatrix))

if __name__ == '__main__':
    main()
