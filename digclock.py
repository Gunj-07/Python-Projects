from tkinter import * 
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    apm = time.strftime("%p")
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ampm.config(text=apm)
    lab_hr.after(200,date_time)


def dateday_monthyear():
    today = datetime.date.today()
    day = today.day
    month = today.strftime("%b")
    year = today.year
    day_name = today.strftime("%a")
    lab_dt.config(text=day)
    lab_mnth.config(text=month)
    lab_yr.config(text=year)
    lab_dy.config(text=day_name)


clock = Tk()
clock.title("DIGITAL_CLOCK")
clock.geometry("900x500")
clock.config(bg="yellow")

lab_hr = Label(clock,text="01",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_hr.place(x=100,y=80,height=100,width=100)

lab_min = Label(clock,text="02",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_min.place(x=300,y=80,height=100,width=100)

lab_sec = Label(clock,text="03",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_sec.place(x=500,y=80,height=100,width=100)

lab_ampm = Label(clock,text="04",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_ampm.place(x=700,y=80,height=100,width=100)



lab_hour = Label(clock,text="HOUR",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_hour.place(x=100,y=200,height=30,width=100)

lab_mint = Label(clock,text="MIN",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_mint.place(x=300,y=200,height=30,width=100)

lab_secd = Label(clock,text="SEC",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_secd.place(x=500,y=200,height=30,width=100)

lab_apm = Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_apm.place(x=700,y=200,height=30,width=100)



lab_dt = Label(clock,text="01",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_dt.place(x=100,y=250,height=100,width=100)

lab_mnth = Label(clock,text="02",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_mnth.place(x=300,y=250,height=100,width=100)

lab_yr = Label(clock,text="03",font=("Time New Roman",35,"bold"),bg="red",fg="white")
lab_yr.place(x=500,y=250,height=100,width=100)

lab_dy = Label(clock,text="04",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_dy.place(x=700,y=250,height=100,width=100)

 

lab_date = Label(clock,text="DATE",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_date.place(x=100,y=370,height=30,width=100)

lab_month = Label(clock,text="MONTH",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_month.place(x=300,y=370,height=30,width=100)

lab_year = Label(clock,text="YEAR",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_year.place(x=500,y=370,height=30,width=100)

lab_day = Label(clock,text="DAY",font=("Time New Roman",20,"bold"),bg="red",fg="white")
lab_day.place(x=700,y=370,height=30,width=100)

date_time()

dateday_monthyear()

clock.mainloop()