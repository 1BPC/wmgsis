from .models import Graduate
import sqlite3
from collections import defaultdict

class Calculate_Grad:

    def getDegreeClassData(self):

        first = Graduate.objects.filter(degree_classifcation="First")
        upper_second = Graduate.objects.filter(degree_classifcation="Upper Second")
        second = Graduate.objects.filter(degree_classifcation="Second")
        third = Graduate.objects.filter(degree_classifcation="Third") 

        degree_class_dict = {"First":((len(first)/5)*100), 
                             "Upper Second":((len(upper_second)/5)*100), 
                             "Second":((len(second)/5)*100), 
                             "Third":((len(third)/5)*100)}
        
        return degree_class_dict  
    

    def getSalaryData(self):
        conn = sqlite3.connect(database="db.sqlite3")
        cursor = conn.cursor()

        cursor.execute ("SELECT salary, city from wmgsis_graduate")
        rows = cursor.fetchall()

        salary_dict = {}
        for row in rows:
            salary_dict[row[1]] = row[0]
        return salary_dict
    

    def getGradActivity(self):
        conn = sqlite3.connect(database="db.sqlite3")
        cursor = conn.cursor()

        cursor.execute ("SELECT cohort, activity from wmgsis_graduate")
        rows = cursor.fetchall()

        my_dict = {}

        cohort_years = []

        for index, value in enumerate(rows):
            
            # Example {'Employed':3}
            my_dict[value[1]] = index
           
           # print(value[0], value[1], index) 

        print(my_dict)

        return my_dict
         


       
  
    
        

    
    



    



