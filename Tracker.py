import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expense_df = pd.DataFrame(columns=["Date", "Category", "Amount"])

        # Styling
        self.root.style = ttk.Style()
        self.root.style.theme_use("clam")
        self.root.style.configure("TButton", padding=10, font=("Arial", 10))
        self.root.style.configure("TLabel", font=("Arial", 10))
        self.root.style.configure("TEntry", font=("Arial", 10))

        self.date_label = ttk.Label(root, text="Date:")
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = ttk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        self.category_label = ttk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.category_entry = ttk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = ttk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        self.view_button = ttk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        if not date or not category or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        self.expense_df = self.expense_df.append({"Date": date, "Category": category, "Amount": amount}, ignore_index=True)
        messagebox.showinfo("Success", "Expense added successfully.")

    def view_expenses(self):
        if self.expense_df.empty:
            messagebox.showinfo("Info", "No expenses to display.")
            return

        category_summary = self.expense_df.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        category_summary.plot(kind="bar", ax=ax)
        ax.set_xlabel("Category")
        ax.set_ylabel("Total Amount")
        ax.set_title("Expense Summary by Category")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, padx=10, pady=5)

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
