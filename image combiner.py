import os
from PIL import Image

dirs =  os.listdir("src")
combinacao = 1

try:
    os.makedirs("out")
except OSError as error:
    print(error)

for f1 in os.listdir("src/" + dirs[0]):
    img1 = Image.open("src/" + dirs[0] + "/" + f1)

    for f2 in os.listdir("src/" + dirs[1]):
        img2 = Image.open("src/" + dirs[1] + "/" + f2)

        for f3 in os.listdir("src/" + dirs[2]):
            img3 = Image.open("src/" + dirs[2] + "/" + f3)

            for f4 in os.listdir("src/" + dirs[3]):
                img4 = Image.open("src/" + dirs[3] + "/" + f4)

                final_img = Image.alpha_composite(img1, img2)
                final_img = Image.alpha_composite(final_img, img3)
                final_img = Image.alpha_composite(final_img, img4)
                final_img.save("out/" + str(combinacao) + ".png")

                print("combinações feitas: " + str(combinacao))               
                combinacao += 1