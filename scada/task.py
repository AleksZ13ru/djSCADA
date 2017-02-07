# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


# для запуска
# C:\Python\env\twoenv\Scripts\activate
# D:
# cd D:\IdeaProjects\prj\djSCADA
# # C:\Python\env\twoenv\Scripts\celery -A skabel beat -l info -S django
# C:\Python\env\twoenv\Scripts\celery -A djSCADA worker -l info

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
