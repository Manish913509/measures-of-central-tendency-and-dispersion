from tkinter import *
from tkinter import ttk
import statistics
import math
       

# Function to calculate Arithmetic Mean
def calculate_arithmetic_mean():
    numbers = number_text.get("1.0", "end-1c").split()
    if numbers:
        numbers = [float(x) for x in numbers]
        result = statistics.mean(numbers)
        result_label.config(text=f"Arithmetic Mean: {result:.2f}")

# Function to calculate Geometric Mean
def calculate_geometric_mean():
    numbers = number_text.get("1.0", "end-1c").split()
    if numbers:
        numbers = [float(x) for x in numbers]
        result = statistics.geometric_mean(numbers)
        result_label.config(text=f"Geometric Mean: {result:.2f}")

# Function to calculate Harmonic Mean
def calculate_harmonic_mean():
    numbers = number_text.get("1.0", "end-1c").split()
    if numbers:
        numbers = [float(x) for x in numbers]
        result = statistics.harmonic_mean(numbers)
        result_label.config(text=f"Harmonic Mean: {result:.2f}")

# Function to calculate Mode
def calculate_mode():
    numbers = number_text.get("1.0", "end-1c").split()
    if numbers:
        numbers = [float(x) for x in numbers]
        result = statistics.mode(numbers)
        result_label.config(text=f"Mode: {result:.2f}")

# Function to calculate Median
def calculate_median():
    numbers = number_text.get("1.0", "end-1c").split()
    if numbers:
        numbers = [float(x) for x in numbers]
        result = statistics.median(numbers)
        result_label.config(text=f"Median: {result:.2f}")

# Function to be called when the "Calculate" button is clicked
def calculate_button_clicked():
    selected_option = var.get()
    if selected_option == 1:
        calculate_arithmetic_mean()
    elif selected_option == 2:
        calculate_harmonic_mean()
    elif selected_option == 3:
        calculate_geometric_mean()
    elif selected_option == 4:
        calculate_mode()
    elif selected_option == 5:
        calculate_median()

# Creating Main window
root = Tk()
root.title("Measure of Central Tendency and Dispersion")
root.geometry("450x600")

# Styling
root.configure(bg="lightgreen")  # Set a different background color

# Title
title_label = Label(
    text="Measure of Central Tendency and Dispersion",
    font=("Arial", 16),
    bg="yellow",  # Set background color
)
title_label.pack(pady=20)  # Add padding

# Author Details
author_label = Label(
    text="Developer: manish maurya", font=("Arial", 15), bg="#FFC0CB"
)
author_label.pack()




# List of Numbers
number_label = Label(
    text="Enter List of Numbers:", font=("Arial", 12), bg="#e6e6e6"
)
number_label.pack(pady=10)

number_text = Text(height=3, width=35)
number_text.pack(pady=5)

# Measure of Central Tendency
ctLabel = Label(
    text="Measure of Central Tendency", font=("Arial", 12), bg="light yellow"
)
ctLabel.pack(pady=10)

var = IntVar()

ct_options = [
    ("Arithmetic Mean", 1, "#FFD700"),  # Light Yellow
    ("Harmonic Mean", 2, "#98FB98"),  # Pale Green
    ("Geometric Mean", 3, "#ADD8E6"),  # Light Blue
    ("Mode", 4, "#FFA07A"),  # Light Salmon
    ("Median", 5, "#FFC0CB"),  # Pink
]

for text, value, color in ct_options:
    r_ct = Radiobutton(
        text=text, variable=var, value=value, font=("Arial", 10), bg=color,
        padx=10, pady=5, borderwidth=2, relief="ridge"
    )
    r_ct.pack(anchor=W, padx=25, pady=(0, 5))  # Adding a 5-pixel margin below each button

# Calculate Button
calculate_button = Button(
    text="Calculate",
    command=calculate_button_clicked,
    font=("Arial", 12),
    bg="green",
)
calculate_button.pack(pady=10)  # Reduce vertical padding to 10 pixels

result_label = Label(
    text="", font=("Arial", 12)
)
result_label.pack(pady=5)  # Reduce vertical padding to 5 pixels

quitButton = Button(
    text="Quit from System",
    command=root.destroy,
    font=("Arial", 12),
    bg="red",
)
quitButton.pack(pady=10)  # Reduce vertical padding to 10 pixels

root.mainloop()
