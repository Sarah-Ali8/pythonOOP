##1 P1###################
import tkinter as tk
from tkinter import ttk
from tkinter import *

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Unit Converter')
        self.root.geometry('460x465')
        self.root.config(bg="lightblue")
        self.root.iconbitmap("c:/converter/exchange.ico")
        self.root.resizable(False ,False)
        self.root.grid_columnconfigure(0, weight=1)
## 2 ##################
        self.label = ttk.Label(text="__UNIT CONVERTER__", background='lightblue', font=('Times New Roman', 15, 'bold'), foreground='dimgray')
        self.label.grid(row=0, column=0, padx=40, pady=10)
        self.font_style = ttk.Style()
        self.font_style.configure('TButton',  font=('Times New Roman', 11, 'bold'), foreground= 'dimgray', background='lightblue')
        self.font_style.configure('TCombobox', font=('Times New Roman', 16))

        # Conversion factors by category
        self.conversion_factors = {
            'Length': {
            'meters': 1,
            'kilometers': 0.001,
            'centimeters': 100,
            'millimeters': 1000,
            'micrometers': 1e6,
            'nanometers': 1e9,
            'miles': 0.0006213712,
            'yards': 1.0936132983,
            'feet': 3.280839895,
            'inches': 39.37007874,
            'nautical miles': 0.0005396118,
            'astronomical units': 6.684587122E-12,
            'light years': 1.057000834E-16,
            'parsecs': 3.240779289E-17,
            'fathoms': 0.5468066492,
            'furlongs': 0.0049709695,
            'chains': 0.0497096954,
            'rods': 0.1988387815,
            'links': 4.9709695379,
            'nails': 17.497812773,
            'hands': 9.842519685,
            'mils': 39370.07874,
            'points': 2834.6456693,
            'arpents': 0.0170877078,
            'cubits': 2.1872265967,
            'fingers': 8.7489063867,
            'leagues': 0.0002071237,
            'microns': 1000000,
            'decimeters': 10,
            'football fields': 0.001,
            'angstroms': 10000000000,
            'rope': 0.1640419948,
            'stadia': 0.00634 ,
            'paces': 1.3123359580052,

            },
            'Mass': {
                'grams': 1,
                'kilograms': 0.001,
                'milligrams': 1000,
                'micrograms': 1000000,
                'metric tons': 0.000001,
                'pounds': 0.0022046226,
                'ounces': 0.0352739619,
                'stone (US)': 0.0001763698,
                'stone (UK)': 0.000157473,
            },
            'Temperature': {
                'celsius': lambda x: x,
                'fahrenheit': lambda x: (x - 32) * 5 / 9,
                'kelvin': lambda x: x - 273.15,
            },
            'Time': {
                'seconds': 1,
                'minutes': 1 / 60,
                'hours': 1 / 3600,
                'days': 1 / 86400,
                'weeks': 1 / 604800,
                'months': 1 / 2629746,
                'years': 1 / 31536000,
            },
            'Pressure': {
                'pascals': 1,
                'kilopascals': 0.001,
                'megapascals': 1e-6,
                'bars': 1e-5,
                'atmospheres': 9.8692e-6,
                'millimeters of mercury': 0.00750062,
                'inches of mercury': 0.0002953,
            },
            'Energy': {
                'joules': 1,
                'kilojoules': 0.001,
                'megajoules': 1e-6,
                'gigajoules': 1e-9,
                'calories': 0.000239006,
                'kilocalories': 2.39006e-7,
                'electronvolts': 6.242e+18,
                'british thermal units': 9.4782e-7,
            },
            'Frequency': {
                'hertz': 1,
                'kilohertz': 0.001,
                'megahertz': 1e-6,
                'gigahertz': 1e-9,
                'terahertz': 1e-12,
            },
            'Volume': {
                'cubic meters': 1,
                'cubic centimeters': 1e6,
                'cubic millimeters': 1e9,
                'liters': 1000,
                'milliliters': 1e6,
                'cubic inches': 61023.7,
                'cubic feet': 35.3147,
                'cubic yards': 1.30795,
                'gallons': 264.172,
                'quarts': 1056.69,
                'pints': 2113.38,
                'cups': 4166.67,
                'fluid ounces': 33814,
                'tablespoons': 67628,
                'teaspoons': 202884,
            },
            'Area': {
                'square meters': 1,
                'square kilometers': 1e-6,
                'square centimeters': 1e4,
                'square millimeters': 1e6,
                'hectares': 1e-4,
                'acres': 0.000247105,
                'square miles': 3.861e-7,
                'square yards': 1.19599,
                'square feet': 10.7639,
                'square inches': 1550.0031,
            },
            'Speed': {
                'meters per second': 1,
                'meters per hour':3600,
                'meters per minute': 60,
                'kilometers per second':0.001,
                'kilometers per minute': 0.06,
                'kilometers per hour': 3.6,
                'foot per second': 3.280839895,
                'foot per minuter': 196.8503937,
                'foot per hour': 11811.023622,
                'miles per second': 0.0006213712,
                'miles per minute': 0.0372822715,
                'miles per hour': 2.23694,
                'knots': 1.94384,
            },
        }
# 3 P1 #############################
        # Category selection combobox
        self.category_combobox = ttk.Combobox(root, values=[] + list(self.conversion_factors.keys()), style='TCombobox', state= 'readonly')
        self.category_combobox.set("Length")
        self.category_combobox.grid(row=1, column=0, padx=70, pady=15)

        # From unit selection combobox
        self.from_unit_combobox = ttk.Combobox(root, values=[], style='TCombobox', state= 'readonly')
        self.from_unit_combobox.grid(row=2, column=0, padx=70, pady=15)

        # To unit selection combobox
        self.to_unit_combobox = ttk.Combobox(root, values=[], style='TCombobox', state= 'readonly')
        self.to_unit_combobox.grid(row=3, column=0, padx=70, pady=15)

        # Entry widgets
        self.value_entry = tk.Entry(root, width=17, font=('Times New Roman', 11), borderwidth= "2")
        self.value_entry.grid(row=4, column=0, padx=70, pady=15)
        self.value_entry.insert(0, 'Enter a value')

        # Bind the event handler to the <FocusIn> event
        self.value_entry.bind("<FocusIn>", self.remove_placeholder)
#4 P1#############################
        # Convert button
        self.convert_button = ttk.Button(root, text="CONVERT", command=self.convert_units, style="TButton")
        self.convert_button.grid(row=5, column=0, padx=70, pady=10)
##6 P1########################      
        # Result text box
        self.result_text = tk.Text(root, height=2.5, width=40, font=('Times New Roman', 11), borderwidth= "2")
        self.result_text.grid(row=6, column=0, padx=70, pady=15)

        # Reset button
        self.reset_button = ttk.Button(root, text="RESET", command=self.reset_after_conversion, style='TButton')
        self.reset_button.grid(row=7, column=0, padx=70, pady=10)
## 5 #########################
        # Update unit comboboxes when category changes
        self.category_combobox.bind('<<ComboboxSelected>>', self.update_unit_comboboxes)

        # Initialize unit comboboxes with the first category
        self.update_unit_comboboxes(None)

        
        # Update "from" unit combobox based on selected category
    def update_unit_comboboxes(self, event):
        selected_category = self.category_combobox.get()
        from_units = list(self.conversion_factors[selected_category].keys())
        self.from_unit_combobox['values'] = from_units
        self.from_unit_combobox.set('From')

        # Update "to" unit combobox based on selected category
        to_units = list(self.conversion_factors[selected_category].keys())
        self.to_unit_combobox['values'] = to_units
        self.to_unit_combobox.set('To')
## 4 P2 #############################
    def convert_units(self):
        try:
            value = float(self.value_entry.get())
            category = self.category_combobox.get()
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()


            # Perform the conversion
            from_conversion_function = self.conversion_factors[category][from_unit]
            to_conversion_function = self.conversion_factors[category][to_unit]

            if callable(from_conversion_function):
                from_value = from_conversion_function(value)
            else:
                from_value = value / from_conversion_function

            if callable(to_conversion_function):
                result = to_conversion_function(from_value)
            else:
                result = from_value * to_conversion_function

            result_str = f"{value} {from_unit} = {result} {to_unit}."
## 6 P2 #######################
            # Display the result in the text box
            self.result_text.delete(1.0, tk.END)
            if value:
                self.result_text.insert(tk.END, result_str)

        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a valid numeric value.")

        # Reset category selection and clear all fields and result text
    def reset_after_conversion(self):
        self.category_combobox.set('Select a category')
        self.from_unit_combobox.set('From')
        self.to_unit_combobox.set('To')
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, 'Enter a value')
        self.result_text.delete(1.0, tk.END)

## 3 P2 #################
    def remove_placeholder(self, event):
        # Event handler to clear the placeholder text when entry gains focus
        if self.value_entry.get() == 'Enter a value':
            self.value_entry.delete(0, tk.END)
## 1 P2 ##################

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()