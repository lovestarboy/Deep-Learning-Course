from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = "SimHei"

img=Image.open("F:\\python666\\Lena.tiff")
img_r,img_g,img_b=img.split()
plt.figure(figsize=(10,10))

img_r1 = img_r.resize((50,50))
plt.subplot(221)
plt.axis("off")
plt.imshow(img_r1,cmap="gray")
plt.title("R-缩放",fontsize=14)

img_g1 = img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_g2 = img_g1.transpose(Image.ROTATE_270)
plt.subplot(222)
plt.axis("off")
plt.imshow(img_g2,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

img_b1 = img_b.crop((0,0,150,150))
plt.subplot(223)
plt.axis("off")
plt.imshow(img_b1,cmap="gray")
plt.title("B-裁剪",fontsize=14)

img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
img_rgb.save("test.png")
plt.subplot(224)
plt.axis("off")
plt.imshow(img_rgb)
plt.title("图像的色彩模式",fontsize=14)

plt.suptitle("图像基本操作",color="blue",fontsize=20)

plt.show()