from generateCoordinate import generateCoordinate, printCoordinate
from displayCoordinate import displayCoordinate 
from bruteForce import closestPair
from divideAndConquer import solveDivideAndConquer
from utilities import calculateDistance, pointToStr
from time import time

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def validate_int(val):
    if val.isdigit():
        return True
    else:
        return False
    
def calculate_BF():
    n = int(entry_1.get())
    R = int(entry_2.get())
    if(n==0 or R==0):
        print("Error Message")
    else:
        Array = generateCoordinate(n, R)
        start = time() * 1000
        first, second = closestPair(Array)
        distance = calculateDistance(Array[first], Array[second], R)
        finish = time() * 1000
        time_taken = finish - start
        print("Closest Pair: ", end = '')
        printCoordinate(Array[first])
        printCoordinate(Array[second])
        print()

        print(f'Distance: {distance}')

        print("Executed Time: ", time_taken, "ms")
        show_execute_time(time_taken)
        show_results(Array[first], Array[second],distance)

        if (R == 3):
            displayCoordinate(Array, Array[first], Array[second])

def calculate_DnC():
    n = int(entry_1.get())
    R = int(entry_2.get())
    if(n==0 or R==0):
        print("Error Message")
    else:
        Array = generateCoordinate(n, R)
        start = time() * 1000
        first, second, distance = solveDivideAndConquer(Array, n, R)
        finish = time() * 1000
        time_taken = finish - start
        print("Closest Pair: ", end = '')
        printCoordinate(Array[first])
        printCoordinate(Array[second])
        print()

        print(f'Distance: {distance}')

        print("Executed Time: ", time_taken, "ms")

        show_execute_time(time_taken)
        show_results(Array[first], Array[second],distance)

        if (R == 3):
            displayCoordinate(Array, Array[first], Array[second])

def show_execute_time(time):
    executed = Label(window,
                     text = str(round(time,2)) + " ms", 
                     font=("Arial Black",10),
                     anchor="w",
                     bg="#393952",
                     fg="#DCFFC1")
    executed.place(
    x=200.0,
    y=649.0,
)

def show_results(point1,point2,dist):
    point_1 = pointToStr(point1)
    point_2 = pointToStr(point2)
    result_p1 = Label(window,
                     text = point_1, 
                     font=("Arial Black",10),
                     justify="left",
                     bg="#2E2E48",
                     fg="#DCFFC1")
    result_p1.place(
    x=450.0,
    y=480.0,
    )
    result_p2 = Label(window,
                     text = point_2, 
                     font=("Arial Black",10),
                     justify="left",
                     bg="#2E2E48",
                     fg="#DCFFC1")
    result_p2.place(
    x=450.0,
    y=510.0,
    )
    result_dist = Label(window,
                     text = str(round(dist,2)), 
                     font=("Arial Black",10),
                     justify="center",
                     bg="#2E2E48",
                     fg="#DCFFC1")
    result_dist.place(
    x=510.0,
    y=600.0,
    )

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#2E2E48")
window.title("Divide & Conquer")


canvas = Canvas(
    window,
    bg = "#2E2E48",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "flat"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    211.0,
    307.0,
    image=entry_image_1
)
entry_1 = Entry(
    window,
    bd=0,
    bg="#1E1E2E",
    fg="#FFFFFF",
    font=("Arial Black",20),
    selectbackground="#29293F",
    justify="center",
    insertbackground="#FFFFFF",
    highlightthickness=0,
    validate="key",
    validatecommand=(window.register(validate_int), '%S')
)

entry_1.place(
    x=56.0,
    y=281.0,
    width=310.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    211.0,
    480.0,
    image=entry_image_2
)
entry_2 = Entry(
    window,
    bd=0,
    bg="#1E1E2E",
    fg="#FFFFFF",
    font=("Arial Black",20),
    selectbackground="#29293F",
    justify="center",
    insertbackground="#FFFFFF",
    highlightthickness=0,
    validate="key",
    validatecommand=(window.register(validate_int), '%S')
)
entry_2.place(
    x=56.0,
    y=454.0,
    width=310.0,
    height=50.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_DnC,
    relief="flat"
)
button_1.place(
    x=24.0,
    y=539.0,
    width=182.0,
    height=73.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_BF,
    fg="#29293F",
    relief="flat"
)
button_2.place(
    x=215.0,
    y=539.0,
    width=182.0,
    height=73.0
)
window.resizable(True, True)
window.mainloop()
