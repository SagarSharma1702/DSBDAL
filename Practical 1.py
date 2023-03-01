import pandas as sn
import tkinter as tk
from tkinter import ttk
from tkinter  import filedialog
def load_csv():
    # Show file dialog to select CSV file
    file_path = filedialog.askopenfilename()
    # Read the CSV file
    df = sn.read_csv(file_path)
    print(df)

    root=tk.Tk()
    root.title('CSV Data read')
    # Create a Tkinter table
    table = ttk.Treeview(root)

    # Define the columns
    table['columns'] = tuple(df.columns)

    # Add the columns to the table
    for column in table['columns']:
        table.heading(column, text=column)

    # Add the data to the table
    for i, row in df.iterrows():
        table.insert('', 'end', iid=i, values=tuple(row))
# Create a Tkinter window for the file dialog
    #root.withdraw()
# Pack the table into the window
    table.pack(expand=True, fill='both')
   # Run the Tkinter event loop
    root.mainloop()
# Load the CSV file

load_csv()
