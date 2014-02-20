# -*- coding: utf-8 -*-
import urllib
from lxml.html import fromstring

class yandex():
    def __init__(self):
        pass
    def get_now(self):
        self.rawxml = urllib.urlopen("http://export.yandex.ru/weather-ng/forecasts/33347.xml").read();
        self.xstring = fromstring(self.rawxml)

        ds = u'\N{DEGREE SIGN}'
        
        w = {}
        now = self.xstring.findall("fact")
        for item in now:
            temp = item.findall("temperature")
            wtype = item.findall("weather_type")
            wind_direction = item.findall("wind_direction")
            wind_speed = item.findall("wind_speed")
            humidity = item.findall("humidity")
            pressure = item.findall("pressure")
            observation_time = item.findall("observation_time")
            image = item.findall("image")
        try:
            w["temperature"] = temp[0].text
            w["weather_type"] = wtype[0].text
            w["wind_direction"] = wind_direction[0].text
            w["wind_speed"] = wind_speed[0].text
            w["humidity"] = humidity[0].text
            w["pressure"] = pressure[0].text
            w["observation_time"] = observation_time[0].text
            w["image"] = image[0].text
            w["status"] = 0
        except:
            w["status"] = 1
        return w

    def wind(self,w):
        if w["status"] == 0:
                 
            if w["wind_direction"] == "s":
                wd = u"Ветер: <b>Южный</b>"
            elif w["wind_direction"] == "se":
                wd = u"Ветер: <b>Юго-восточный</b>"
            elif w["wind_direction"] == "sw":
                wd = u"Ветер: <b>Юго-западный</b>"
            elif w["wind_direction"] == "n":
                wd = u"Ветер: <b>Северный</b>"
            elif w["wind_direction"] == "ne":
                wd = u"Ветер: <b>Северо-восточный</b>"
            elif w["wind_direction"] == "nw":
                wd = u"Ветер: <b>Северо-западный</b>"
            elif w["wind_direction"] == "w":
                wd = u"Ветер: <b>Западный</b>"
            elif w["wind_direction"] == "e":
                wd = u"Ветер: <b>Восточный</b>"
            else:
                wd = ""
#            #wheader = u"<center><b><small>Яндекс погода <sup>(сейчас)</sup></small></b></center><br>" 
#            wt = u"<font color='lightblue'> <center><b>На улице сейчас<hr>"+w["weather_type"].upper()+"</b></center></font><br>"
#            ws = u" <b> "+w["wind_speed"]+" m/c</b><br>" 
#            wh = u"Влажность: <b><font size=5 color='#0079E3'> "+w["humidity"]+"<sup>%</sup></font></b><br>"
#            wp = u"Атмосферное давление: <b><font size=5 color='lightblue'> "+w["pressure"]+"<sup>mmHg</sup></font></b><hr>" 
#            wtmp = u"Температура воздуха: <font size=5 color='#E39000'><b>"+w["temperature"]+ds+"<sub>C</sub></b></font><hr>"
#            wo = u"<center><font size=2 color='#D2FF8A'>"+w["observation_time"]+"</font><center>"
#            data = wt+wd+ws+wh+wp+wtmp+wo
        
        else:
            wd = "Нет данных"
        return wd


