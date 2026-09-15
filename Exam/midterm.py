#class name, scores
#
import pandas as pd
import numpy as np

Student = str("name")
name = ["Amara", "Leo", "Priya", "Sam", "Amara", "Jade"]
scores = ["92,85,78", "88, 91, 73", "65,72,150","70,not_a_number,60", "95,90,88","81,77,84,90"]

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]
print(student[0]["grade"])
student[0]["grade"] = 95
student.append({"name": "Priya", "grade": 78})