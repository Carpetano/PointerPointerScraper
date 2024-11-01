import requests
import os
import time
import threading


def download_image(url, image_name):
    """
        Download the image from the url
    """
    try:
        # Obtain the HTTP response
        response = requests.get(url)

        # Check if the response is OK
        if response.status_code == 200:

            # Create the file path for the image
            file_path = os.path.join(IMAGES_FOLDER, f"{image_name}.jpg")

            # Download the image
            with open(file_path, "wb") as img:
                img.write(response.content)
            print(f"Image {image_name} downloaded")
                
        else:
            print(f"Image {image_name} not downloaded - Status code: {response.status_code}")

    except Exception as e:
        print(f"Error downloading image {image_name}: {e}")



# PointerPointer website's url
PREFIX = "https://pointerpointer.com/images/"
SUFFIX = ".jpg"

# Folder where we will save the downloaded images
IMAGES_FOLDER = 'Images/'

# Number of images that we want to download, in this case there's 707 images in pointerpointer.com
NUMBER_OF_IMAGES = 707

if __name__ == "__main__":

    # Create Images folder if not exists
    if not os.path.exists(IMAGES_FOLDER):
        os.makedirs(IMAGES_FOLDER)

    # List to hold all threads
    threads = []

    # Iterarate as many times as images we want to download
    for i in range(NUMBER_OF_IMAGES + 1): 

        # Create the URL to download the image from
        url = PREFIX + str(i) + SUFFIX

        # Start a new thread for each download
        image_downloader = threading.Thread(target=download_image, args=(url, i)).start()

        # Add the thread to the threads list
        threads.append(image_downloader)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All images downloaded.")
    