# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:46:44 2022

@author: Bernardo
"""
from datetime import datetime
import tkinter as tk
## Class implementation not actually needed for this case, abandoned
# class ExerciseLog():
#     """ Simple data structure to hold exercise info as a list of tuples
#     to export/import to text."""
#     def __init__(self):
#         self.entries = []
        
#     def add_entry(self, exercise, weight, sets, reps):
#         time = datetime.now()
#         self.entries.append((time, exercise, weight, sets, reps))
        
        
#     def export_data(self, filename):
#         with open(filename, "a") as f:
#             print(self.entries, file=f, sep="")
        
    
#     def import_data(self):
#         pass
    
    
class ExerciseLogGUI():
    """GUI for entering exercise info and exporting record to file."""
    def __init__(self, root):
        root.title("Exercise Log")
        
        #Set up GUI frame
        mainframe = tk.Frame(root)
        mainframe.grid(column=0, row=0, columnspan=4, rowspan=2)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        #Set up dropdown for selecting exercise, and entry fields for weight in
        #lbs, # of sets, and # of reps
        self.exercise = tk.StringVar()
        self.exercise.set("-")
        options = ["Chest Press", "Shoulder Press", "Vertical Row", 
                   "Lat Pulldown", "Dumbbell", "Leg Press", 
                   "Leg Extension", "Leg Curl"]
        self.exercise_options = tk.OptionMenu(mainframe, self.exercise, *options)
        self.exercise_options.grid(column=0, row=0, sticky = "W")                                     
        tk.Label(mainframe, text="Exercise").grid(column=0, row=1, sticky = 'N')
        
        self.weight = tk.StringVar()
        self.weight_entry = tk.Entry(mainframe, width=15, textvariable=self.weight)
        self.weight_entry.grid(column=1, row=0)
        tk.Label(mainframe, text="Weight (Lbs)").grid(column=1, row=1)
        
        
        self.sets = tk.StringVar()
        self.sets_entry = tk.Entry(mainframe, width=7, textvariable = self.sets)
        self.sets_entry.grid(column=2, row=0)
        tk.Label(mainframe, text="Sets").grid(column = 2, row=1)
        
        self.reps = tk.StringVar()
        self.reps_entry = tk.Entry(mainframe, width=7, textvariable = self.reps)
        self.reps_entry.grid(column=3, row=0)
        tk.Label(mainframe, text="Reps").grid(column=3, row=1)
        
        
        #Button to save record
        self.save_record_button = tk.Button(mainframe, text="Save record",
                                            command=self.save_record)
        self.save_record_button.grid(column=4, row=0)
       
    def save_record(self):
        """Save exercise log tuple (datetime, str exercise, int weight,
        int sets, int reps) to file"""
        record = (datetime.now(), self.exercise.get(), self.weight.get(), 
                  self.sets.get(), self.reps.get())
        with open("ExerciseLog.txt", "a") as f:
            print(record, file=f, sep="")

       
        
        
root = tk.Tk()
ExerciseLogGUI(root)
root.mainloop()