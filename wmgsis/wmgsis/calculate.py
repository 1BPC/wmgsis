from .models import Graduate
import sqlite3
from collections import defaultdict

class Calculate_Grad:
    """ A class which gets gets data from the database, and prepares it in such a 
    way to be able to add it to a dictionary."""

    def getDegreeClassData(self):
        """ Gets data on degree classification
        Returns a dictionary of the grade and the number of people with that grade
        for example {'First':3} """

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
        """ Gets salary data from the
        Creates a database connection, calls a cursor object, then 
        executes custom SQL directly, returning the results to the row variable.
        Loop through the list creating a dictionary of city: salary """

        conn = sqlite3.connect(database="db.sqlite3")
        cursor = conn.cursor()

        cursor.execute ("SELECT salary, city from wmgsis_graduate")
        rows = cursor.fetchall()

        salary_dict = {}
        for row in rows:
            salary_dict[row[1]] = row[0]
        return salary_dict
    

    def getGradActivity(self):
        """ Gets graduate activity data from the database

        Creates a database connection, calls a cursor object, then 
        executes custom SQL directly, returning the results to the row variable.
        Loop through the list creating a dictionary of city: salary

        # Returns dictionary, Example {'Employed':3} """

        conn = sqlite3.connect(database="db.sqlite3")
        cursor = conn.cursor()

        cursor.execute ("SELECT cohort, activity from wmgsis_graduate")
        rows = cursor.fetchall()

        my_dict = {}

        for index, value in enumerate(rows):
            my_dict[value[1]] = index
           
        return my_dict


       
  
    
        

    
    



    



