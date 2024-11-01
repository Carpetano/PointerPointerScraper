import requests
import os

# PointerPointer website's url
PREFIX = "https://pointerpointer.com/images/"
SUFIX = ".jpg"

# Folder where we will save the downloaded images
IMAGES_FOLDER = 'Images/'

# Number of images that we want to download, in this case there's 707 images in pointerpointer.com
NUMBER_OF_IMAGES = 707

# Create Images folder if not exists
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

# Iterarate as many times as images we want to download
for i in range(NUMBER_OF_IMAGES + 1): # +1 because we want to download the first image

    # Create the url to download the image from
    url = PREFIX + str(i) + SUFIX

    try:

        # Obtain the http response
        response = requests.get(url)

        # Check if the response is OK
        if response.status_code == 200:

            # Create the file path for the image
            file_path = os.path.join(IMAGES_FOLDER, f"{i}.jpg")

            # Download the image
            with open(file_path, "wb") as img:
                img.write(response.content)
            print(f"{i} Downloaded")
                
        else:

            print(f"{i} Not Downloaded")

    except Exception as e:
        print("Error:",e)