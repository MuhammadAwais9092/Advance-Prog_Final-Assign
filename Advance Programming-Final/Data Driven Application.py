# Advance Programming
# ASSESSMENT 2: Data Driven Application
# The Meal Database


# Import necessary modules
import requests  # For making HTTP requests
import json  # For working with JSON data
import tkinter as tk  # For creating a GUI
from PIL import Image, ImageTk  # For working with images
from io import BytesIO  # For handling binary data
import tkinter.messagebox  # For displaying message boxes

# Function to fetch a random meal from the API
def lookup_random_meal():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    if response.status_code == 200:
        meal = response.json()["meals"][0]
        return meal
    else:
        return None

# Function to clear the text in all labels
def clear_labels():
    for label in [meal_label, image_label, ingredients_label, measurements_label, area_label, category_label]:
        label.config(text="")

# Function to display information about a meal
def show_meal(meal_name):
    global meal_label, image_label, ingredients_label, measurements_label, area_label, category_label
    clear_labels()

    # Fetch meal data from the API
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meal = data["meals"][0]

        # Display meal name and image
        meal_label = tk.Label(root, text=meal["strMeal"], font=("Helvetica", 16))
        meal_label.place(x=350, y=250)

        image_url = meal["strMealThumb"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image = image.resize((352, 204), resample=Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            image_label = tk.Label(root, image=image)
            image_label.image = image
            image_label.place(x=592, y=250)

            # Display ingredients, measurements, area, and category
            ingredients = [meal[f"strIngredient{i}"] for i in range(1, 21) if meal[f"strIngredient{i}"]]
            measurements = [meal[f"strMeasure{i}"] for i in range(1, 21) if meal[f"strMeasure{i}"]]

            ingredients_label = tk.Label(root, text="Ingredient: " + ", ".join(ingredients), font=("Helvetica", 12), wraplength=800)
            ingredients_label.place(x=350, y=550)

            measurements_label = tk.Label(root, text="Measurement: " + ", ".join(measurements), font=("Helvetica", 12), wraplength=800)
            measurements_label.place(x=350, y=670)

            area_label = tk.Label(root, text="Area: " + meal["strArea"], font=("Helvetica", 16))
            area_label.place(x=350, y=777)

            category_label = tk.Label(root, text="Category: " + meal["strCategory"], font=("Helvetica", 16))
            category_label.place(x=350, y=807)

        else:
            meal_label = tk.Label(root, text="No meal found")
            meal_label.pack()
    else:
        meal_label = tk.Label(root, text="No meal found")
        meal_label.pack()

# create a GUI with tkinter
root = tk.Tk()  # Initialize the main tkinter window
root.geometry("1500x1000+200+0")  # Set the initial size and position of the window
root.maxsize(1500, 1000)  # Set the maximum size of the window
root.minsize(1500, 1000)  # Set the minimum size of the window

# Load the image file
bg_image = ImageTk.PhotoImage(Image.open("frame bg.png"))  # Load the background image
background_label = tk.Label(root, image=bg_image)  # Create a label to display the background image
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the background label, covering the entire window

# Get the width and height of the window
window_width = root.winfo_width()  # Get the width of the window
window_height = root.winfo_height()  # Get the height of the window

# define variables in the global scope
meal_label = tk.Label(root, text="")  # Initialize a label for displaying meal information
image_label = tk.Label(root, text="")  # Initialize a label for displaying images
ingredients_label = tk.Label(root, text="")  # Initialize a label for displaying ingredients
measurements_label = tk.Label(root, text="")  # Initialize a label for displaying measurements
area_label = tk.Label(root, text="")  # Initialize a label for displaying the meal area
category_label = tk.Label(root, text="")  # Initialize a label for displaying the meal category

def show_random_meal():
    clear_labels()  # Clear the existing labels
    meal = lookup_random_meal()  # Get a random meal from the API

    if meal:
        show_meal(meal["strMeal"])  # Display the details of the random meal
    else:
        meal_label = tk.Label(root, text="No meal found")  # Display a message if no meal is found
        meal_label.pack()

def show_info():
    tkinter.messagebox.showinfo(
        "Information",
        "Welcome to the Meal API! Explore random and top-rated culinary delights. Click the buttons to view recipes."
    )  # Show an information dialog

RandomButton = tk.Button(
    root,
    text="Random Meal",
    command=show_random_meal,
    fg="white",
    font=("Italiana", 18),
)  # Create a button for displaying a random meal
RandomButton.place(x=1180, y=80, relwidth=0.1, relheight=0.05)  # Place the random meal button

RandomButton.config(
    borderwidth=5,
    relief="flat",
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
    padx=0,
)  # Configure the appearance of the random meal button

InstructionButton = tk.Button(
    root,
    text="Instruction",
    command=show_info,
    fg="white",
    font=("Italiana", 24),
)  # Create a button for displaying instructions
InstructionButton.place(x=140, y=90, relwidth=0.1, relheight=0.05)  # Place the instruction button

InstructionButton.config(
    borderwidth=5,
    relief="flat",
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
    padx=0,
)  # Configure the appearance of the instruction button

tamiyaButton = tk.Button(
    root,
    text="Tamiya",
    command=lambda: show_meal("tamiya"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Tamiya
tamiyaButton.place(x=300, y=185, relwidth=0.1, relheight=0.05)  # Place the Tamiya button

tamiyaButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  # Configure the appearance of the Tamiya button

bistekButton = tk.Button(
    root,
    text="Bistek",
    command=lambda: show_meal("bistek"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Bistek
bistekButton.place(x=520, y=185, relwidth=0.1, relheight=0.05)  # Place the Bistek button

bistekButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  # Configure the appearance of the Bistek button

burekButton = tk.Button(
    root,
    text="Burek",
    command=lambda: show_meal("burek"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Burek
burekButton.place(x=740, y=185, relwidth=0.1, relheight=0.05)  # Place the Burek button

burekButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  # Configure the appearance of the Burek button

kaftejiButton = tk.Button(
    root,
    text="Kafteji",
    command=lambda: show_meal("kafteji"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Kafteji
kaftejiButton.place(x=960, y=185, relwidth=0.1, relheight=0.05)  # Place the Kafteji button

kaftejiButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  # Configure the appearance of the Kafteji button

root.mainloop()  # Start the tkinter event loop