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

from acp_limits import brevet_calculator

def test_over_err():
    x=brevet_calculator()
    assert (x.message(1000,1300,"2001-01-01 00:00")=="Error: Exceeded Maximum Brevet Length!")

def test_fixed():
    x=brevet_calculator()
    y=x.controle_times(200,200)
    assert(y[0]==5 and y[1]==53 and y[2]==13 and y[3]==30)

def test_variable():
    x=brevet_calculator()
    y=x.controle_times(600,500)
    assert(y[0]==15 and y[1]==28 and y[2]==33 and y[3]==20)