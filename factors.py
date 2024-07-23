import tkinter as tk 
from tkinter import messagebox 

def main():
    try:
        num = int(entry.get())
        result = factorize(num)
        messagebox.showinfo("Result", f"The factors of {num} are {result}")
    except ValueError:
        messagebox.showinfo("Error", "enter a valid integer")


def factorize(n):
    factors=[]
    for i in range(n+1):
          if i !=0:
               if n%i==0:
                    factors.append(i)
    return factors


root = tk.Tk()
root.title("Finding Factors")

label = tk.Label(root,text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Find", command=main)
button.pack(pady=10)

root.mainloop()