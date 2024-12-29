import requests
import tkinter as tk
from tkinter import ttk, messagebox
import time

def featch_prayar_time(city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return None
    except Exception as e:
        return f"Unexpected error occurred: {e}"

def gui_featch_prayar_time():
    try:
        city = city_entry.get()
        country = country_entry.get()
        if city and country:
            # Check for valid input
            if not city.isalpha() or not country.isalpha():
                messagebox.showerror("ERROR", "Please enter valid city and country names.")
                return
            prayar_timings = featch_prayar_time(city, country)
            if prayar_timings:
                result.delete(0, tk.END)
                for name, time in prayar_timings.items():
                    result.insert(tk.END, f"{name}: {time}")
                current_time = time.strftime('%H:%M:%S')
                result.insert(tk.END, f"Current Time: {current_time}")
            else:
                messagebox.showerror("ERROR", "Unable to fetch prayer times. Please try again.")
        else:
            messagebox.showerror("ERROR", "Please enter both city and country names.")
    except AttributeError:
        messagebox.showerror("ERROR", "Unable to fetch prayer times. Please try again.")

def update_prayer_times():
    gui_featch_prayar_time()

app = tk.Tk()
app.title("Prayer Time Fetcher")
frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=5)
city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=5)

country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=5)
country_entry = ttk.Entry(frame, width=20)
country_entry.grid(row=1, column=1, pady=5)

fetch_button = ttk.Button(frame, text="Get Prayer Times", command=gui_featch_prayar_time)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

update_button = ttk.Button(frame, text="Update Prayer Times", command=update_prayer_times)
update_button.grid(row=3, column=0, columnspan=2, pady=5)

result = tk.Listbox(frame, height=11, width=50)
result.grid(row=4, column=0, columnspan=2, pady=5)

app.mainloop()
