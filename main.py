from PIL import Image
import os

for photo in range(5):
    image = Image.open(f"photo_{photo}.jpg")
    instagram = image.resize((1080, 1080))
    coordinates = (10, 0, instagram.width-10, instagram.height)
    vk = image.resize((1400, 1000))
    instagram = instagram.crop(coordinates)
    facebook = image.resize((1200, 628))
    if not os.path.isdir(f"photo_{photo}_end"):
        os.mkdir(f"photo_{photo}_end")
    vk.save(f"photo_{photo}_end/photo_vk_{photo}.png", "png")
    instagram.save(f"photo_{photo}_end/photo_instagram_{photo}.png", "png")
    facebook.save(f"photo_{photo}_end/photo_facebook_{photo}.png", "png")

