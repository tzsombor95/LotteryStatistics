from django.db import models

# makemigrations → To update and see the history or transaction happened in our table
# (We have to run this command every time when something changes in models.py e.g. adding a new table, changing a field name, etc
# python manage.py makemigrations
#
# migrate → The last step to submit or sent out our table into the database server
# python manage.py migrate

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
