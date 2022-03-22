# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 23:19:40 2022

@author: Bernardo
"""
from datetime import datetime
import ui

class ExerciseLogGUI():
    """GUI for entering exercise info and exporting record to file."""
    def __init__(self):
        
        #Set up GUI frame
        view = ui.View()
        view.name="Exercise Log"
        view.background_color = "White"
        
        self.exercise = ""
        self.weight = ""
        self.sets = ""
        self.reps = ""
        
        def exercise_tapped(sender):
            self.exercise = self.exercise_textfield.text

        self.exercise_textfield = ui.TextField(placeholder="Insert exercise", frame=(150,100,200,40))
        self.exercise_textfield.action = exercise_tapped
        view.add_subview(self.exercise_textfield)
        
        def weight_tapped(sender):
            self.weight = self.weight_textfield.text
            
        self.weight_textfield = ui.TextField(placeholder="Insert weight (lbs)", frame=(150, 180, 200, 40))
        self.weight_textfield.action = weight_tapped
        view.add_subview(self.weight_textfield)
        
        def sets_tapped(sender):
            self.sets = self.sets_textfield.text
        self.sets_textfield = ui.TextField(placeholder="Insert # of Sets", frame=(150, 260, 200, 40))
        self.sets_textfield.action = sets_tapped
        view.add_subview(self.sets_textfield)

        def reps_tapped(sender):
            self.reps = self.reps_textfield.text
        self.reps_textfield = ui.TextField(placeholder="Insert # of Reps", frame=(150, 340, 200, 40))
        self.reps_textfield.action = reps_tapped
        view.add_subview(self.reps_textfield)           
    
        def save_record(sender):
            """Save exercise log tuple (datetime, str exercise, int weight,
            int sets, int reps) to file"""
            record = (datetime.now().strftime("%d-%b-%y (%H:%M:%S)"), self.exercise, self.weight, 
                  self.sets, self.reps)
            with open("ExerciseLog.txt", "a") as f:
                print(record, file=f, sep="")

        
        #Button to save record
        self.save_record_button = ui.Button(title="Save", frame=(150, 450, 40, 40))
        self.save_record_button.action = save_record
        view.add_subview(self.save_record_button)
       

        

        self.last_record_label = ui.Label(text=logged_records_string, frame=(0, 500, 400, 40), text_color='white')
        view.add_subview(self.last_record_label)

        view.present("fullscreen")


def load_records():
            """Loads exercise log tuple from file and returns a list of records.
            Uses string manipulation methods to split between datetime portion and
            other attributes portion because both datetime and tuple 
            objects delimited by comma. """
            with open("ExerciseLog.txt", "r") as f:
                records = []
                for line in f:
                    datetime_index = line.find(")")
                    record = []
                    record.append(line[:datetime_index+1])
                    tuple_remainder = line[datetime_index+3:len(line)-1]
                    for item in tuple_remainder.split(", "):
                        cleaned_item = item.replace("'", "")
                        record.append(cleaned_item)
                    records.append(record)
                return records

logged_records = load_records()
logged_records_string = ", ".join(logged_records[len(logged_records)-1])
        
ExerciseLogGUI()
   