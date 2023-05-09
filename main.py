from PIL import Image
import os

files = '/Users/mac/PycharmProjects/image_manipulator/images'
new_file = '/Users/mac/PycharmProjects/image_manipulator/rotated_images'

if not os.path.exists(new_file):
    os.makedirs(new_file)

for filename in os.listdir(files):
    if filename.endswith('48dp'):
        filepath = os.path.join(files, filename)
        with Image.open(filepath) as img: #opening the image
            width, height = img.size
            new_size = (width // 2, height // 2)
            resized_img = img.resize(new_size)
            rotated_img = resized_img.rotate(270)
            if rotated_img.mode == 'LA':
                rotated_img = rotated_img.convert('RGB')
            new_filepath = os.path.join(new_file, os.path.splitext(filename)[0] + '_rotated.jpeg')
            rotated_img.save(new_filepath, 'JPEG')
            rotated_img.show()
