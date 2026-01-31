from nicegui import ui
import random
import os

# gets all images with .png extension form provided path
def get_image_paths(folder_path, extensions=['.png']):
    image_paths = []
    for filename in os.listdir(folder_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in extensions:
            image_paths.append(os.path.join(folder_path, filename))
    return image_paths

def change_images():
    global index
    global not_used_images
    global already_used_images

    index = (index + 1) % len(not_used_images)
    img1.set_source(not_used_images[index])
    already_used_images.append(not_used_images[index])
    del not_used_images[index]

    index = (index + 1) % len(not_used_images)
    img2.set_source(not_used_images[index])
    already_used_images.append(not_used_images[index])
    del not_used_images[index]

    print("ALREADY")
    print(already_used_images)
    print("NOT USED")
    print(not_used_images)

    if len(not_used_images) <= 1:
        not_used_images.extend(already_used_images)
        already_used_images = []
        random.shuffle(not_used_images)
        print("==============================")
        print("RESTART IMAGES")
        print("==============================")


already_used_images =  []
not_used_images = get_image_paths("images/")
random.shuffle(not_used_images)

# start web page logic
index = 0
with ui.column().classes('w-full h-screen items-center justify-center'):
    with ui.row().classes('gap-60'):
        img1 = ui.image().style('width: 640px; height: 640px;')
        img2 = ui.image().style('width: 640px; height: 640px;')
# Start slideshow (change every 3 seconds)
ui.timer(3.0, change_images)

ui.run()