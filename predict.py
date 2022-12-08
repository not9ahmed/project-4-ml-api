# imports
import numpy as np
import pandas as pd
from joblib import dump, load
from PIL import Image
from io import BytesIO
from tensorflow.keras.preprocessing import image

input_shape = (224, 224)

def read_image(image_encoded):
    pil_image = Image.open(Bytes(image_encoded))

    return pil_image


def preprocess(image_api: Image.Image):

    img_width, img_height = 224, 224
    img = image.load_img(image_api, target_size = input_shape)
    img = image.img_to_array(img)

# function to retrieve the most similar products for a given product
def get_recipe_class(name_en):

    # closest_imgs_scores_visual = cos_similarities_df_visual[productID].sort_values(ascending=False)[1:number_of_closest_products+1]
    # closest_imgs_scores_text = cos_similarities_df_text[productID].sort_values(ascending=False)[1:number_of_closest_products+1]

    # closest_imgs_scores = pd.concat([closest_imgs_scores_visual, closest_imgs_scores_text], ignore_index=False)
    # dictResponse = closest_imgs_scores.to_dict()

    pass


