# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 23:19:40 2022

@author: Bernardo
"""
from datetime import datetime
import ui
import dialogs

class ExerciseLogGUI():
    """GUI for entering exercise info and exporting record to file."""
    def __init__(self):
        
        #Set up GUI frame
        view = ui.View()
        view.name="Exercise Log"
        view.background_color = "White"
        
        #Set up dropdown for selecting exercise, and entry fields for weight in
        #lbs, # of sets, and # of reps
        options = ["Chest Press", "Shoulder Press", "Vertical Row", 
                   "Lat Pulldown", "Dumbbell", "Leg Press", 
                   "Leg Extension", "Leg Curl"]
        self.exercise = ""
        self.weight = ""
        self.sets = ""
        self.reps = ""
        
        def exercise_tapped(sender):
            self.exercise = dialogs.list_dialog(title="Exercise Options", 
                                                items=options)
        self.exercise_button = ui.Button(title="Exercise", frame=(0,0,50,16))
        self.exercise_button.action = exercise_tapped
        self.exercise_button.flex = "WH"
        view.add_subview(self.exercise_button)
        
        def weight_tapped(sender):
            self.weight = dialogs.text_dialog(title="Insert weight (lbs)")
            
        self.weight_button = ui.Button(title="Weight", frame=(60, 0, 25, 16))
        self.weight_button.action = weight_tapped
        self.weight_button.flex = "WH"
        view.add_subview(self.weight_button)
        
        def sets_tapped(sender):
            self.sets = dialogs.text_dialog(title="Insert # of sets")
        self.sets_button = ui.Button(title="Sets", frame=(90, 0, 25, 16))
        self.sets_button.action = sets_tapped
        self.sets_button.flex = "WH"
        view.add_subview(self.sets_button)

        def reps_tapped(sender):
            self.reps = dialogs.text_dialog(title="Insert # of reps")
        self.reps_button = ui.Button(title="Reps", frame=(120, 0, 25, 16))
        self.reps_button.action = reps_tapped
        self.reps_button.flex = "WH"
        view.add_subview(self.reps_button)           
    
        def save_record(self, sender):
            """Save exercise log tuple (datetime, str exercise, int weight,
            int sets, int reps) to file"""
            record = (datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"), self.exercise.get(), self.weight.get(), 
                  self.sets.get(), self.reps.get())
        with open("ExerciseLog.txt", "a") as f:
            print(record, file=f, sep="")

        
        #Button to save record
        self.save_record_button = ui.Button(title="Save", frame=(150, 0, 25, 16))
        self.save_record_button.action = save_record
        self.save_record_button.flex = "WH"
        view.present("fullscreen")
        
        
   