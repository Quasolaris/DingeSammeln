from nicegui import ui
from nicegui import ui, events
import random
import os

# parameters
# default 640
image_size="640"

# default 60
gap_size="60"

# default 3.0
timer = 10.0 


def handle_key(event: events.KeyEventArguments):
    global timer
    global timer_state

    if event.action.keydown and event.key.name == ',':
        set_imageL()
    elif event.action.keydown and event.key.name == '.':
        if timer_state < 1:
            timer_state = 1
        else:
            timer_state = 0
    elif event.action.keydown and event.key.name == '-':
        set_imageR()
    elif event.action.keydown and event.key.name == '$':
        set_imageL()
        set_imageR()


def set_imageL():

    global index
    global not_used_images
    global already_used_images

    index = (index + 1) % len(not_used_images)
    print("Printing Image LEFT: " + not_used_images[index])
    imgL.set_source(not_used_images[index])
    already_used_images.append(not_used_images[index])
    del not_used_images[index]
    check_image_que()

def set_imageR():

    global index
    global not_used_images
    global already_used_images

    index = (index + 1) % len(not_used_images)
    print("Printing Image RIGHT: " + not_used_images[index])
    imgR.set_source(not_used_images[index])
    already_used_images.append(not_used_images[index])
    del not_used_images[index]
    check_image_que()

def check_image_que():
    global not_used_images
    global already_used_images

    if len(not_used_images) <= 1:
        not_used_images.extend(already_used_images)
        already_used_images = []
        random.shuffle(not_used_images)
        print("==============================")
        print("RESTART IMAGES")
        print("==============================")

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
    global timer

    if timer_state == 1:
        set_imageL()
        set_imageR()

    else:
        print("TIMER OFF")

    print("-----------------------------")


already_used_images =  []
not_used_images = get_image_paths("images/")
random.shuffle(not_used_images)

# list index
index = 0

# timer on/off - 1 is ON 0 is OFF
timer_state = 1


with ui.column().classes('w-full h-screen items-center justify-center'):
    with ui.row().classes('gap-'+gap_size):
        imgL = ui.image().style('width: '+image_size+'px; height: '+image_size+'px;')
        imgR = ui.image().style('width: '+image_size+'px; height: '+image_size+'px;')


ui.keyboard(on_key=handle_key)
# Start slide show (change every 3 seconds)
ui.timer(timer, change_images)

ui.run()