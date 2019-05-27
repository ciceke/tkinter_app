
# tkinter_app
# created by E.Cicek, May 2019

import random
import tkinter as tk
import time
import datetime

cur_time=datetime.datetime.now()

n_question=1
n_try=1
    
def time_elapsed():
    global cur_time
    t2=datetime.datetime.now()
    diff=t2-cur_time
    return int(diff.seconds)


class App():
    
    def __init__(self):
        
        #initial numbers
        x=random.randint(2,9)
        y=random.randint(x,9)
        
        #main window
        self.root=tk.Tk()
        self.root.title("Multiplication Table Questions for 2nd Graders")
        self.root.geometry("480x300")
        
        #other widgets
        self.labelt=tk.Label(text="", font=("Arial",11), fg="blue", height="2")
        self.labelt.grid(row=0, column=2, columnspan=4, sticky="W")
        self.clock()
        
        self.labelsoru=tk.Label(text="Question-%i" %n_question, font=("Arial",11), height="2")
        self.labelsoru.grid(row=1, column=1, sticky="W")

        self.label0=tk.Label(text="Press OK after entering your Answer !",font=("Arial",11))
        self.label0.grid(row=4, column=1, columnspan=6)

        self.label1=tk.Label(text=x, font=(None,15))
        self.label1.grid(row=1, column=2)

        self.label2=tk.Label(text="X", font=(None,15))
        self.label2.grid(row=1, column=3)       

        self.label3=tk.Label(text=y, font=(None,15))
        self.label3.grid(row=1, column=4)

        self.label4=tk.Label(text="=", font=(None,15))
        self.label4.grid(row=1, column=5)

        self.e=tk.Entry(font=(None,15), width=5)
        self.e.grid(row=1, column=6)
        self.e.focus()

        self.label5=tk.Label(text="", font=("Calibri",12), height=2)
        self.label5.grid(row=5, column=1, columnspan=7)
        
        self.r = tk.Button(text="OK", fg="red",command=self.check_mult)
        self.r.grid(row=3,column=6,sticky="S")
        
        #keep window open
        self.root.mainloop()

    def clock(self):
        t=time.strftime("%-d-%B-%Y %H:%M:%S",time.localtime())
        if t!="":
            self.labelt.config(text=t)
        self.root.after(100,self.clock)
        
    def correct_answer(self):
        global n_question, t_elapsed, n_try
        n_question+=1
        if n_question<11:
            a=str(self.label1["text"])
            b=str(self.label3["text"])
            dt=time.strftime("%-d-%B %H:%M:%S",time.localtime())
            cur_result=dt+" Question: "+a+"x"+b+" in "+str(t_elapsed)+"seconds "+str(n_try)+" after tries\n"
            f=open("result.txt","a")
            f.write(cur_result)
            f.close()
            self.e.delete(0,"end")
            self.e.focus()
            n_try=1
            #create new numbers and show them on window
            x=random.randint(2,9)
            y=random.randint(2,9)
            self.label1.config(text=x)
            self.label3.config(text=y)
            self.labelsoru.config(text="Question-%i" %n_question)
        else:
            self.label0.config(text="",fg="red")
            self.label5.config(text="****** FINISHED QUESTIONS *****",fg="red")

    def check_mult(self):
        global cur_time, t_elapsed, n_try
        if self.e.get()=="":
            self.label5.config(text="You pressed OK before entering your Answer !", fg="red", bg="white")
            self.e.focus()
        else:
            try:
                z=int(self.e.get()),
                x=int(str(self.label1["text"]))
                y=int(str(self.label3["text"]))
                z=int(self.e.get())
                if x*y==int(z):
                    t_elapsed=time_elapsed()
                    cur_time=datetime.datetime.now()
                    self.label5.configure(text="Congrats. Correct answer in %i seconds)" %t_elapsed,fg="green",bg="white")
                    self.correct_answer()
                else:
                    self.label5.configure(text="Think again. Correct Answer in not %i :(" %z,fg="white",bg="red")
                    n_try+=1
                    self.e.delete(0,"end")
                    self.e.focus()
            except ValueError:
                self.label5.configure(text="Hey ! You need to enter a number !!",fg="yellow",bg="purple")
                self.e.delete(0,"end")
                self.e.focus()    


if __name__=="__main__":
    app=App()
