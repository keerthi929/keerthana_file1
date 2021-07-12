#1)

from tkinter import *  
from PIL import ImageTk,Image
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("ball.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop() 


# 2 explicit function to get 
# weather details 

def getweather(city): 

    result = requests.get(url.format(city, api_key)) 
    if result: 
        json = result.json() 
        city = json['name'] 
        country = json['sys'] 

        temp_kelvin = json['main']['temp'] 
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main'] 
        final = [city, country, temp_kelvin,  
                 temp_celsius, weather1] 
        return final 
    else: 
        print("NO Content Found") 
        
        

#3
import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()