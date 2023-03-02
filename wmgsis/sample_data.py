import os
import django

class Data():

    def MakeData(self):
        Graduate.objects.all().delete()

        Brandon = Graduate(graduate_name="Brandon", cohort="2023", salary=30000, city="Warwick", activity="Employed", degree_classifcation="First")
        Mansi = Graduate(graduate_name="Mansi", cohort="2023", salary=20000, city="London", activity="Employed", degree_classifcation="Second")
        Josh = Graduate(graduate_name="Josh", cohort="2023", salary=24000, city="Manchester", activity="Employed", degree_classifcation="Upper Second")
        Fas = Graduate(graduate_name="Fas", cohort="2023", salary=28000, city="Bath", activity="Employed", degree_classifcation="First")
        Giorgio = Graduate(graduate_name="Giorgio", cohort="2023", salary=18000, city="Liverpool", activity="Unemployed", degree_classifcation="Third")
        Tia = Graduate(graduate_name="Tia", cohort="2021", salary=40000, city="Crawley", activity="Other", degree_classifcation="First")
        Shelly = Graduate(graduate_name="Shelly", cohort="2021", salary=280000, city="Crawley", activity="Employed", degree_classifcation="First")

        Graduates = [Brandon, Mansi, Josh, Fas, Giorgio]

        for Grad in Graduates:
            Grad.save()



if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "wmgsis.settings")

    django.setup()

    from wmgsis.models import Graduate

    graduate_class = Data()
    graduate_class.MakeData()

