

import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1000, height=1000)
        self.title("The Daily Grind")

        # Create a label
        label1 = tk.Label(self, text="Coffee Mobile Ordering!")
        label1.pack()
        
        # Create a button that opens a secondary window
        button1 = tk.Button(self, text="Start Order for In-Store Pickup", command=self.open_secondary_window)
        button1.pack()
        
        # Create a button that opens a secondary window
        button2 = tk.Button(self, text="Start Order for Drive-Thru Window Pickup", command=self.open_secondary_window)
        button2.pack()

        # Create a button that exits the application
        button3 = tk.Button(self, text="Exit", command=self.quit)
        button3.pack()

        #Create Canvas
        canvas= Canvas(self, width=143, height=113)
        canvas.pack()
        
        # Create a photoimage object of the image in the path
        image1 = Image.open("cupp.png")
        image1 = image1.resize((100,100))
        self.ph = ImageTk.PhotoImage(image1)
        
        
        #Add image to the Canvas Items
        canvas.create_image(100,100,image=self.ph)

        #Create Canvas
        canvas= Canvas(self, width=143, height=113)
        canvas.pack()
        
        # Create a photoimage object of the image in the path
        image2 = Image.open("thanku.png")
        image2 = image2.resize((100,100))
        self.ph2 = ImageTk.PhotoImage(image2)
       
        
        #Add image to the Canvas Items
        canvas.create_image(100,100,image=self.ph2)

    def open_secondary_window(self):
        # Create secondary (or popup) window.
        newWindow = tk.Toplevel()
        newWindow.title("Menu")
        newWindow.config(width=10, height=10)

        # Create input labels and entry boxes
        self.caramel_iced_latte_lbl = tk.Label(newWindow, text="Caramel Iced Latte ($5.00)")
        self.caramel_iced_latte_ent = tk.Entry(newWindow)
        self.vanilla_iced_latte_lbl = tk.Label(newWindow, text="Vanilla Iced Latte ($5.00)")
        self.vanilla_iced_latte_ent = tk.Entry(newWindow)
        self.black_brewed_coffee_lbl = tk.Label(newWindow, text="Black Brewed Coffee ($5.00)")
        self.black_brewed_coffee_ent = tk.Entry(newWindow)
        self.frozen_vanilla_coffee_lbl = tk.Label(newWindow, text="Frozen Vanilla Coffee($7.00)")
        self.frozen_vanilla_coffee_ent = tk.Entry(newWindow)
        self.halzenut_latte_lbl = tk.Label(newWindow, text="Halzenut Latte ($7.00)")
        self.halzenut_latte_ent = tk.Entry(newWindow)
        self.mocha_latte_lbl = tk.Label(newWindow, text="Mocha Latte ($7.00)")
        self.mocha_latte_ent = tk.Entry(newWindow)

        # Create order button
        self.order_btn = tk.Button(newWindow, text="Place Order", command=self.calculate_total)

        # Create exit button
        self.exit_btn = tk.Button(newWindow, text="Exit", command=self.quit)

        # Pack labels, entry boxes and buttons to the form
        self.caramel_iced_latte_lbl.pack()
        self.caramel_iced_latte_ent.pack()
        self.vanilla_iced_latte_lbl.pack()
        self.vanilla_iced_latte_ent.pack()
        self.black_brewed_coffee_lbl.pack()
        self.black_brewed_coffee_ent.pack()
        self.frozen_vanilla_coffee_lbl.pack()
        self.frozen_vanilla_coffee_ent.pack()
        self.halzenut_latte_lbl.pack()
        self.halzenut_latte_ent.pack()
        self.mocha_latte_lbl.pack()
        self.mocha_latte_ent.pack()
        self.order_btn.pack()
        self.exit_btn.pack()
    
    def calculate_total(self):
        try:
            # Get input values and calculate total price
            caramel_iced_latte = int(self.caramel_iced_latte_ent.get())
            vanilla_iced_latte = int(self.vanilla_iced_latte_ent.get())
            black_brewed_coffee = int(self.black_brewed_coffee_ent.get())
            frozen_vanilla_coffee = int(self.frozen_vanilla_coffee_ent.get())
            halzenut_latte = int(self.halzenut_latte_ent.get())
            mocha_latte = int(self.mocha_latte_ent.get())

            total_price = (caramel_iced_latte + vanilla_iced_latte + black_brewed_coffee) * 5.00 + \
                          (frozen_vanilla_coffee + halzenut_latte + mocha_latte) * 7.00
            total_price *= 1.07 # Add 7% sales tax

            # Display total price in a message box
            messagebox.showinfo("Total Price", f"Thank you for ordering, your total is ${total_price:.2f}")
        except ValueError:
            # Display error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid integer for each item.")

root = MainWindow()

# Run main loop
root.mainloop()