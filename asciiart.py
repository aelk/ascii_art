from PIL import Image

imageName = "Fernando_noronha.jpg"
im = Image.open(imageName)
col, row = im.size

print("Successfully constructed pixel matrix!")
print("Pixel matrix size:", col, "x", row)

pixels = im.load()

