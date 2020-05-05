import os

import cv2
import cloudinary as cldn
import cloudinary.uploader as uploader
from dotenv import load_dotenv


load_dotenv()

cldn.config(
    cloud_name=os.getenv("CLDN_CLOUD_NAME"),
    api_key=os.getenv("CLDN_API_KEY"),
    api_secret=os.getenv("CLDN_API_SECRET")
)


def upload_to_cldn(img):
    img_path = 'test-imgs/temp_snap.jpg'
    cv2.imwrite(img_path, img)
    try:
        response = uploader.upload(
            img_path,
            use_filename=1,
            unique_filename=0,
            folder=f'planttypey'
        )
        print(f'[INFO] uploaded {img_path}')  # use logging instead
        return response['secure_url']
    except:
        # print(f'[INFO] error uploading {img_path}...skipping')  # use logging instead
        # raise Exception("Error uploading image...")
        raise

