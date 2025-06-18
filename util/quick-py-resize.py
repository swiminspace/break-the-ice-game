from PIL import Image

width = 100
height = 100

penguin = Image.open("img/penguin.png")
iceberg = Image.open("img/iceberg.png")

new_size = (width, height)

resized_penguin_image = penguin.resize(new_size, Image.LANCZOS)
resized_iceberg_image = iceberg.resize(new_size, Image.LANCZOS)

resized_penguin_image.save("img/penguin_resized.png")
resized_iceberg_image.save("img/iceberg_resized.png")