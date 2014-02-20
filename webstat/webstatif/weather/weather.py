# -*- coding: utf-8 -*-
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from dateutil import parser
from matplotlib import dates


class Weather():
    def _init_(self):
        pass


    def defuse(self,data):
        data_len = len(data)
        if data_len < 60:
            defuser = 3
        elif data_len < 120:
            defuser = 6
        elif data_len < 180:
            defuser = 9
        else:
            defuser = 10
        return data[0::defuser]
    
    def make_plot(self,data,xasis,storepath):
        
        self.cpath = os.path.dirname(os.path.abspath(__file__))

        p = []
        for item in data:
            p.append(float(item.rstrip()))
        
        timeaxis=[]
        for items in xasis:
            timeaxis.append(parser.parse(items))

        y = np.array(p)


        font = {'family' : 'sans',
        'color'  : 'lightgreen',
        'weight' : 'normal',
        'size'   : 18,
        }

        min = p[0] - 1.5
        max = p[len(p)-1] + 1.5

        plt.clf()
        plt.cla()
        fig = plt.gcf()

        fig.patch.set_facecolor('black')
        fig.patch.set_visible(True)
        fig.set_size_inches(10,5)     
        fig.suptitle(u'Перепады давления за последние 3 часа', fontdict=font)
        
        plt.subplot(111,axisbg="black")
        plt.yticks(fontsize=18, color="lightgreen")
        plt.xticks(fontsize=18, color="lightgreen")
        
        plt.ylim([min,max])
        plt.xticks(rotation='vertical')

        plt.grid(b=True, which='both', color='gray',linestyle='--',linewidth=1)

        plt.subplots_adjust(bottom=.3)
        
        plt.plot(timeaxis, y, 'k-', color="lightgreen", linewidth=2)
        try:
            os.remove(storepath+"/3hp.png")
        except:
            pass
        plt.savefig(storepath+"/3hp.png",dpi=45,format="png",transparent=False,facecolor=fig.get_facecolor(),edgecolor='none')


    def normality(self,pdata):
        data=pdata[:-3]
        print data
        if int(data) in range(748,754):
            return u"<font color=#66ccff><b>нормальное</b></font>"        
        if int(data) <= 747:
            return u"<font color=#ffff99><b>низкое</b></font>"
        if int(data) >= 755:
            return u"<font color=#ff6666><b>высокое</b></font>"
        else:
            return "Error"

    def pres_tendense(self,data):
        first_half_list = data[0:60]
        last_half_lsit = data[61:120]
        self.up = u'\N{UPWARDS WHITE ARROW}' 
        self.dn = u'\N{DOWNWARDS WHITE ARROW}'
        self.nn = u'\N{ALMOST EQUAL TO}'
        a = 0
        for i in first_half_list:
            a = a + float(i)
        averfh = a / len(first_half_list)
        b = 0
        for i in last_half_lsit:
            b = b + float(i)
        averlh = b / len(last_half_lsit)
        print int(averlh), int(averfh)
        if int(averfh) >= int(averlh):
            return u"<font color=#FF57B0>"+self.up+"</font>"
        elif int(averfh) <= int(averlh):
            return u"<font color='yellow'>"+self.dn+"</font>"
        else:
            return u"<font color='lightblue'>"+self.nn+"</font>"



        
        



