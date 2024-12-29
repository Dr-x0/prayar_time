import requests
import tkinter as tk
from tkinter import ttk , messagebox
def featch_prayar_time (city, country):
    url= f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
   
    try :
        respons = requests.get(url) 
        info = respons.json()
        if "data" in info :
           timings = info["data"]["timings"]
           return timings  
        else :
            return None
    except Exception as  e :
        return f"unxepcted error occurod{e}"  
def gui_featch_prayar_time():
  try:  
    city= city_entry.get()
    country= country_entry.get()
    if city and country :
       prayar_timings = featch_prayar_time(city , country)
    #print(prayar_timings) 
       for name , time in prayar_timings.items():
          result.insert(tk.END, f"{name}:{time}")
    else:
        messagebox.showerror("ERROR","unable to featch prayer time,please enter corrct city and country names ")
  except AttributeError:
     messagebox.showerror("ERROR","unable to featch prayer time,please enter corrct city and country names")              
app= tk.Tk()   
app.title("prayar_time") 
frame=ttk.Frame(app,padding="20")
frame.grid(row=0,column=0)

city_labble=ttk.Label(frame,text= "City : " )
city_labble.grid(row=0,column=0,pady=5)
city_entry=ttk.Entry(frame,width=20)
city_entry.grid(row=0,column=1,pady=5)

country_labble=ttk.Label(frame,text= "country : " )
country_labble.grid(row=1,column=0,pady=5)
country_entry=ttk.Entry(frame,width=20)
country_entry.grid(row=1,column=1,pady=5)
featch_button=ttk.Button(frame,text="get prayer times",command=gui_featch_prayar_time)
featch_button.grid(row=2,column=0,columnspan=2,pady=10)
result=tk.Listbox(frame,height=11 ,width=30)
result.grid(row=3,column=0,columnspan=2,pady=5)
app.mainloop()
