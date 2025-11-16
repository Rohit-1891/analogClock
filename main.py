import tkinter as tk
import math
from datetime import datetime

def stylish_clock():
    root = tk.Tk()
    root.title("Modern Analog Clock")

    canvas = tk.Canvas(root, width=420, height=420, bg="#f3f3f3", highlightthickness=0)
    canvas.pack()

    def update_clock():
        canvas.delete("all")

        cx, cy = 210, 210
        radius = 180

        # Outer Circle (Modern thin border)
        canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius,
                           outline="#444", width=3)

        # Hour Marks
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x_start = cx + 150 * math.cos(angle)
            y_start = cy + 150 * math.sin(angle)
            x_end = cx + 170 * math.cos(angle)
            y_end = cy + 170 * math.sin(angle)
            canvas.create_line(x_start, y_start, x_end, y_end, fill="#222", width=3)

        # Minute Marks
        for i in range(60):
            if i % 5 != 0:
                angle = math.radians(i * 6 - 90)
                x_start = cx + 165 * math.cos(angle)
                y_start = cy + 165 * math.sin(angle)
                x_end = cx + 175 * math.cos(angle)
                y_end = cy + 175 * math.sin(angle)
                canvas.create_line(x_start, y_start, x_end, y_end, fill="#777", width=1)

        now = datetime.now()
        sec = now.second
        minute = now.minute
        hour = now.hour % 12

        sec_angle = sec * 6
        min_angle = minute * 6 + sec * 0.1
        hour_angle = hour * 30 + minute * 0.5

        def draw_hand(angle, length, width, color):
            rad = math.radians(angle - 90)
            x = cx + length * math.cos(rad)
            y = cy + length * math.sin(rad)
            canvas.create_line(cx, cy, x, y, fill=color, width=width, capstyle=tk.ROUND)

        draw_hand(hour_angle, 95, 6, "#000")
        draw_hand(min_angle, 140, 4, "#111")
        draw_hand(sec_angle, 160, 2, "#d90429")

        canvas.create_oval(cx - 8, cy - 8, cx + 8, cy + 8, fill="#222")

        root.after(1000, update_clock)

    update_clock()
    root.mainloop()

stylish_clock()
