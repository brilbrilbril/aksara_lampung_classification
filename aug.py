# this is a file to externally augmented the images
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img

source_dir = "./Aksara Lampung"
output_dir = "./Aksara Lampung Augmented"

datagen = ImageDataGenerator(
    rotation_range=25,  
    width_shift_range=0.2, 
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

for subfolder in os.listdir(source_dir):
    subfolder_path = os.path.join(source_dir, subfolder)
    output_subfolder = os.path.join(output_dir, subfolder)

    if os.path.isdir(subfolder_path):
        os.makedirs(output_subfolder, exist_ok=True)

        for filename in os.listdir(subfolder_path):
            img_path = os.path.join(subfolder_path, filename)
            try:
                img = load_img(img_path) 
                img_array = img_to_array(img)
                img_array = img_array.reshape((1,) + img_array.shape)
                aug_iter = datagen.flow(img_array, batch_size=1, save_to_dir=output_subfolder, 
                                        save_prefix="aug", save_format="png")
                
                # each image being augmented 20 times
                for _ in range(20):
                    next(aug_iter)
                print(f"Successfully generate {filename}")
            except Exception as e:
                print(f"Skipping {filename}: {e}")

print("Image augmentation completed!")