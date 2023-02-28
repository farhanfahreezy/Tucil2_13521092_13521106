from generateCoordinate import generateCoordinate, printCoordinate
from displayCoordinate import displayCoordinate 
from bruteForce import closestPair
from divideAndConquer import solveDivideAndConquer
from utilities import calculateDistance, pointToStr
from time import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Frame, Button, PhotoImage, Label


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
    clear_label(window)
    input_n = entry_1.get()
    input_R = entry_2.get()
    if(input_n=="0" or input_R=="0" or input_n=="" or input_R==""):
        show_error()
    else:
        n = int(input_n)
        R = int(input_R)
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
        show_results(Array[first], Array[second],distance,"Brute Force")

        if (R == 3):
            show_plot(Array, Array[first], Array[second])

def calculate_DnC():
    clear_label(window)
    input_n = entry_1.get()
    input_R = entry_2.get()
    if(input_n=="0" or input_R=="0" or input_n=="" or input_R==""):
        show_error()
    else:
        n = int(input_n)
        R = int(input_R)
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
        show_results(Array[first], Array[second],distance,"Divide \n& Conquer")

        if (R == 3):
            show_plot(Array, Array[first], Array[second])

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

def show_results(point1,point2,dist,algorithm):
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
    y=570.0,
    )
    result_algorithm = Label(window,
                     text = algorithm, 
                     font=("Arial Black",10),
                     justify="center",
                     bg="#2E2E48",
                     fg="#DCFFC1")
    result_algorithm.place(
    x=490.0,
    y=635.0,
    )

def show_plot(arrayCoordinate, c1, c2):
    # c1 dan c2 adalah 2 koordinat yang akan digaris
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Masukin semua koordinat ke diagram
    for i in range(len(arrayCoordinate)):
        x, y, z = arrayCoordinate[i]
        ax.scatter(x, y, z, c='g',s=1)

    # Buat garis diantara c1 dan c2
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    ax.scatter(x1, y1, z1, c='r',s=10)
    ax.scatter(x2, y2, z2, c='r',s=10)
    ax.plot([x1, x2], [y1, y2], [z1, z2], c='r')

    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')

    canvas_figure = FigureCanvasTkAgg(fig, master=canvas)
    canvas_figure.draw()
    canvas_figure.get_tk_widget().place(x=640, y=87, width=600, height=600)
    
    canvas.graph = canvas_figure

def show_error():
    errorMsg = Label(window,
                     text = "Input cannot be blank\nor zero", 
                     font=("Arial Black",10),
                     anchor="w",
                     justify="left",
                     bg="#393952",
                     fg="#FFC9C1")
    errorMsg.place(
    x=200.0,
    y=639.0,
)

def clear_label(window):
    for child in window.winfo_children():
        if isinstance(child, Label):
            child.destroy()

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
window.resizable(False, False)
window.mainloop()
