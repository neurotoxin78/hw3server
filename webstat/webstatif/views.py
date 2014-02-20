# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django import template
from django.template.defaultfilters import stringfilter
from django.template import *
register = template.Library()
from django.template import RequestContext
import datetime
from webstat import settings
from db.mtsql import sql
from weather.weather import Weather
import os
import SOAPpy



s = sql()
###


cpath = os.path.dirname(os.path.abspath(__file__))
spath = cpath[:-9]+"statics/images/"
s=sql()
w=Weather()

#@login_required
def hello(request): 
    last3h = s.get_last_3h()

    last3hour = []
    pres = []
    time = []
    
    for items in last3h:
        last3hour.append(items[10].rstrip())
        time.append(items[4]+":"+items[5]+":"+items[6])
    
    
    norm = w.normality(last3hour[0])
    ten = w.pres_tendense(last3hour)

    intro = u'<center><div class="bank_summary_head_main" ><h2><b>Сейчас: '+str(last3hour[0])+'</b><sup>mmHg<sup></h2><br>'+norm+ten+'</div></center>'
    w.make_plot(last3hour,time,spath)        
    
    return render_to_response('newlook.html', {'content': intro,'title': "uForecaster",'url' : "/statics/images/3hp.png" })


def login_redirect(request):
    pass
    return redirect('/login/')

def render_nav(request):
    menu="<html><body><a href='/loguot/'></a></body></html>"
    return menu
