from django import template
from time import strftime,time,mktime
from datetime import datetime

register = template.Library()

def st(timeobj):

    return timeobj.strftime("%Y-%h-%d,%H:%M:%S")



register.filter("time" , st)
