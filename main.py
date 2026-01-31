from nicegui import ui
import os

# gets all images with .png extension form provided path
def get_image_paths(folder_path, extensions=['.png']):
    image_paths = []
    for filename in os.listdir(folder_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in extensions:
            image_paths.append(os.path.join(folder_path, filename))
    return image_paths

# changes image 1
def next_image1():
    global index
    index = (index + 1) % len(images)
    img1.set_source(images[index])

# changes image 2
def next_image2():
    global index
    index = (index + 1) % len(images)
    img2.set_source(images[index])

images = get_image_paths("images/")
# start web page logic
index = 0
with ui.row():
    img1 = ui.image().classes('w-640 h-640')
    img2 = ui.image().classes('w-640 h-640')

# Start slideshow (change every 3 seconds)
ui.timer(3.0, next_image1)
ui.timer(3.0, next_image2)

ui.run()