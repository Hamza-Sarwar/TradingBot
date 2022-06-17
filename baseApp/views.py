from django.shortcuts import render
from websocket import create_connection
import json, time
import pandas as pd
# Create your views here.

def index(request):
    
    return render(request, 'index.html', {})