# import tkinter as tk

# root = tk.Tk()
# root.title("my first canvas")

# canvas = tk.Canvas(root,width=500,
#                    height=350, bg="white")

# canvas.pack()


# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(280, 50, 440, 190, fill="lightblue")
# canvas.create_line(50, 250, 500, 250, width=4)
# canvas.create_text(275, 310, text="Hello canvas",font=("Arial",20))

# root.mainloop()

import tkinter as tk

# -----------------------------
# WINDOW
# -----------------------------
root = tk.Tk()
root.title("Beautiful House")
root.geometry("900x650")
root.resizable(False, False)

canvas = tk.Canvas(root, width=900, height=650)
canvas.pack()

# -----------------------------
# SKY
# -----------------------------
canvas.create_rectangle(
    0, 0, 900, 650,
    fill="#BDEBFF",
    outline=""
)

# -----------------------------
# GRASS
# -----------------------------
canvas.create_rectangle(
    0, 470, 900, 650,
    fill="#8FD694",
    outline=""
)

# -----------------------------
# SUN
# -----------------------------
canvas.create_oval(
    720, 60, 810, 150,
    fill="#FFD966",
    outline="#F4B942",
    width=3
)

# Sun rays
for x1, y1, x2, y2 in [
    (765, 45, 765, 20),
    (765, 165, 765, 190),
    (705, 105, 680, 105),
    (825, 105, 850, 105),
    (720, 60, 700, 40),
    (810, 60, 830, 40),
    (720, 150, 700, 170),
    (810, 150, 830, 170)
]:
    canvas.create_line(
        x1, y1, x2, y2,
        fill="#F4B942",
        width=4
    )

# -----------------------------
# CLOUDS
# -----------------------------
def cloud(x, y):
    canvas.create_oval(
        x, y + 20, x + 70, y + 60,
        fill="white", outline=""
    )
    canvas.create_oval(
        x + 30, y, x + 100, y + 60,
        fill="white", outline=""
    )
    canvas.create_oval(
        x + 65, y + 20, x + 130, y + 60,
        fill="white", outline=""
    )

cloud(80, 80)
cloud(500, 70)

# -----------------------------
# HOUSE BODY
# -----------------------------
canvas.create_rectangle(
    250, 280, 650, 500,
    fill="#F4A6A6",
    outline="#703838",
    width=5
)

# -----------------------------
# ROOF
# -----------------------------
canvas.create_polygon(
    200, 280,
    450, 90,
    700, 280,
    fill="#3979B7",
    outline="#244E78",
    width=6
)

# Small roof border
canvas.create_line(
    200, 280,
    700, 280,
    fill="#244E78",
    width=8
)

# -----------------------------
# LEFT WINDOW
# -----------------------------
canvas.create_rectangle(
    295, 325, 395, 410,
    fill="#EAF8FF",
    outline="#5C6670",
    width=5
)

# Window frame
canvas.create_line(
    345, 325, 345, 410,
    fill="#5C6670",
    width=4
)

canvas.create_line(
    295, 367, 395, 367,
    fill="#5C6670",
    width=4
)

# -----------------------------
# RIGHT WINDOW
# -----------------------------
canvas.create_rectangle(
    505, 325, 605, 410,
    fill="#EAF8FF",
    outline="#5C6670",
    width=5
)

canvas.create_line(
    555, 325, 555, 410,
    fill="#5C6670",
    width=4
)

canvas.create_line(
    505, 367, 605, 367,
    fill="#5C6670",
    width=4
)

# -----------------------------
# DOOR
# -----------------------------
canvas.create_rectangle(
    405, 370, 495, 500,
    fill="#8B5A3C",
    outline="#59351F",
    width=5
)

# Door panels
canvas.create_rectangle(
    420, 385, 480, 430,
    outline="#70452F",
    width=2
)

canvas.create_rectangle(
    420, 445, 480, 485,
    outline="#70452F",
    width=2
)

# Door handle
canvas.create_oval(
    470, 435, 480, 445,
    fill="#FFD966",
    outline="#9A751A",
    width=2
)

# -----------------------------
# PATH
# -----------------------------
canvas.create_polygon(
    405, 500,
    495, 500,
    580, 650,
    320, 650,
    fill="#D8C3A5",
    outline=""
)

# -----------------------------
# LEFT TREE
# -----------------------------
canvas.create_rectangle(
    95, 350, 135, 500,
    fill="#795548",
    outline=""
)

canvas.create_oval(
    40, 270, 160, 390,
    fill="#4CAF50",
    outline=""
)

canvas.create_oval(
    90, 230, 210, 370,
    fill="#43A047",
    outline=""
)

canvas.create_oval(
    70, 310, 180, 420,
    fill="#388E3C",
    outline=""
)

# -----------------------------
# RIGHT TREE
# -----------------------------
canvas.create_rectangle(
    765, 365, 805, 500,
    fill="#795548",
    outline=""
)

canvas.create_oval(
    700, 285, 820, 400,
    fill="#4CAF50",
    outline=""
)

canvas.create_oval(
    750, 240, 870, 380,
    fill="#43A047",
    outline=""
)

canvas.create_oval(
    720, 320, 840, 430,
    fill="#388E3C",
    outline=""
)

# -----------------------------
# FLOWERS
# -----------------------------
def flower(x, y, petal_color):
    # stem
    canvas.create_line(
        x, y, x, y + 35,
        fill="#3D8B40",
        width=3
    )

    # petals
    canvas.create_oval(
        x - 12, y - 10, x, y + 2,
        fill=petal_color,
        outline=""
    )

    canvas.create_oval(
        x, y - 10, x + 12, y + 2,
        fill=petal_color,
        outline=""
    )

    canvas.create_oval(
        x - 6, y - 18, x + 6, y - 5,
        fill=petal_color,
        outline=""
    )

    canvas.create_oval(
        x - 6, y - 3, x + 6, y + 10,
        fill=petal_color,
        outline=""
    )

    # center
    canvas.create_oval(
        x - 4, y - 5, x + 4, y + 3,
        fill="#FFD966",
        outline=""
    )


flower(180, 530, "#FF7AA2")
flower(220, 570, "#9B7EDE")
flower(690, 540, "#FF7AA2")
flower(730, 580, "#FFD166")
flower(150, 590, "#9B7EDE")
flower(770, 530, "#FF7AA2")

# -----------------------------
# SMALL BUSHES
# -----------------------------
for x in [20, 250, 620, 850]:
    canvas.create_oval(
        x, 440, x + 80, 510,
        fill="#4CAF50",
        outline=""
    )

# -----------------------------
# BIRDS
# -----------------------------
canvas.create_arc(
    300, 100, 330, 120,
    start=0, extent=180,
    style=tk.ARC,
    width=3
)

canvas.create_arc(
    330, 100, 360, 120,
    start=0, extent=180,
    style=tk.ARC,
    width=3
)

# -----------------------------
# DOG HOUSE
# -----------------------------

# Dog house body
canvas.create_rectangle(
    690, 400, 850, 520,
    fill="#D99A6C",
    outline="#70452F",
    width=4
)

# Dog house roof
canvas.create_polygon(
    675, 400,
    770, 320,
    865, 400,
    fill="#B94E48",
    outline="#6E2925",
    width=4
)

# Dog house entrance
canvas.create_oval(
    735, 430, 805, 510,
    fill="#4A3025",
    outline="#3A241C",
    width=3
)

# Small step
canvas.create_rectangle(
    730, 505, 810, 520,
    fill="#8B5A3C",
    outline="#5C3825",
    width=3
)

# -----------------------------
# SMALL DOG HOUSE
# -----------------------------

# Dog house body
canvas.create_rectangle(
    720, 430, 830, 515,
    fill="#D99A6C",
    outline="#70452F",
    width=3
)

# Dog house roof
canvas.create_polygon(
    705, 430,
    775, 370,
    845, 430,
    fill="#B94E48",
    outline="#6E2925",
    width=3
)

# Entrance
canvas.create_oval(
    750, 455, 800, 515,
    fill="#4A3025",
    outline="#3A241C",
    width=2
)

# Small step
canvas.create_rectangle(
    745, 510, 805, 520,
    fill="#8B5A3C",
    outline=""
)


# -----------------------------
# SMALL CUTE DOG
# -----------------------------

# Body
canvas.create_oval(
    585, 540, 655, 580,
    fill="#C68642",
    outline="#6B4226",
    width=2
)

# Head
canvas.create_oval(
    625, 505, 680, 550,
    fill="#C68642",
    outline="#6B4226",
    width=2
)

# Ears
canvas.create_oval(
    620, 505, 640, 535,
    fill="#8B5A2B",
    outline=""
)

canvas.create_oval(
    665, 505, 685, 535,
    fill="#8B5A2B",
    outline=""
)

# Eyes
canvas.create_oval(
    638, 520, 645, 527,
    fill="black",
    outline=""
)

canvas.create_oval(
    660, 520, 667, 527,
    fill="black",
    outline=""
)

# Nose
canvas.create_oval(
    648, 535, 658, 543,
    fill="black",
    outline=""
)

# Tongue
canvas.create_oval(
    649, 542, 657, 553,
    fill="#F08080",
    outline=""
)

# Front legs
canvas.create_rectangle(
    600, 570, 612, 600,
    fill="#C68642",
    outline="#6B4226",
    width=1
)

canvas.create_rectangle(
    630, 570, 642, 600,
    fill="#C68642",
    outline="#6B4226",
    width=1
)

# Paws
canvas.create_oval(
    596, 592, 614, 602,
    fill="#8B5A2B",
    outline=""
)

canvas.create_oval(
    626, 592, 644, 602,
    fill="#8B5A2B",
    outline=""
)

# Tail
canvas.create_arc(
    565, 530, 605, 565,
    start=60,
    extent=220,
    style=tk.ARC,
    width=5
)

# -----------------------------
# START
# -----------------------------
root.mainloop()