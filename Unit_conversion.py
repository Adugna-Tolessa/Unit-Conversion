import tkinter as tk
from ttkbootstrap import Style, ttk

length_factors = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Inch": 0.0254,
    "Foot": 0.3048,
    "Yard": 0.9144,
    "Mile": 1609.34,
}

def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        

        value_in_meters = value * length_factors[from_unit]
        converted_value = value_in_meters / length_factors[to_unit]
        
        result_var.set(f"{converted_value:.4f} {to_unit}")
    except ValueError:
        result_var.set("Invalid input")

# Main window
root = tk.Tk()
style = Style(theme="darkly")  

root.title("Unit Converter")
root.geometry("400x200")
root.resizable(False, False)

# Input field
ttk.Label(root, text="Value:").pack(pady=5)
entry_value = ttk.Entry(root)
entry_value.pack(pady=5)

# From unit
ttk.Label(root, text="From Unit:").pack(pady=5)
combo_from = ttk.Combobox(root, values=list(length_factors.keys()), state="readonly")
combo_from.pack(pady=5)
combo_from.set("Meter")

# To unit
ttk.Label(root, text="To Unit:").pack(pady=5)
combo_to = ttk.Combobox(root, values=list(length_factors.keys()), state="readonly")
combo_to.pack(pady=5)
combo_to.set("Kilometer")

# Convert button
ttk.Button(root, text="Convert", command=convert).pack(pady=10)

# Result
result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, font=("Helvetica", 14)).pack(pady=5)

root.mainloop()
