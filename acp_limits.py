import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging

import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times


class brevet_calculator():
    """Stores the functions and tables required for calculating openings and closings."""
    def __init__(self):
        self.maxSpd = [34,32,30,28,28,26]
        self.minSpd = [15,15,15,11.428,11.48,13.333] #repeat the values for 600-1000 to cover the whole range
        self.interval = 200
        self.endings = { 200:[5,53,13,30], 300:[9,0,20,0], 400:[12,8,27,0], 600:[18,48,40,0], 1000:[33,5,75,0]}
        #For use when the controle is at or past the assigned length.
        #endings[key][0] represents opening hour, [1] represents opening minute.
        # [2] represents closing hour, [3] represents closing minute.
    def controle_times(self, brevet_length, controle):
        """returns an integer list of form[op-hr,op-mi,ed-hr,ed-mi]"""
        if(brevet_length<=controle<=1.1*brevet_length):
            return self.endings[brevet_length]
        elif(controle==0):
            return [0,0,1,0]
        elif(controle>1.1*brevet_length):
            return [-1,-1,-1,-1] #negatives are normally impossible so this will serve as an error code of sorts
        else:
           tm = [0,0,0,0]
           fas = 0.0
           slo = 0.0
           ct = controle
           las = len(self.maxSpd)
           for i in range(las):
               seg=min(ct,200)*1.0
               ct -=seg
               fas+=seg/self.maxSpd[i]
               slo+=seg/self.minSpd[i]
           tm[0]=fas//1
           fmin = round(60*(fas%1),0)
           tm[1]=int(fmin)
           tm[2]=slo//1
           smin = round(60*(slo%1),0)
           tm[3]=int(smin)
           return tm
    def message(self, brevet_length, controle,date_time):
          """Produces the message to be displayed by the webpage."""
          c_times = self.controle_times(brevet_length,controle)
          print(c_times)
          if(c_times[0]==-1):
              return "Error: Exceeded Maximum Brevet Length!"
          else:
              t = arrow.get(date_time, 'YYYY-MM-DD HH:mm')
              opn = t.replace(hours=c_times[0],minute=c_times[1])
              cls = t.replace(hours=c_times[2],minute=c_times[3])
              begin = opn.format('YYYY-MM-DD HH:mm')
              end = cls.format('YYYY-MM-DD HH:mm')
              mess = "Open: "+begin+"\nClose: "+end
              return mess
              