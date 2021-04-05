import os
import schedule
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE','capstone_project.settings')
import django
django.setup()
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from stock_app.models import Stock
requests.packages.urllib3.disable_warnings()

def stock_delete():
    deleter = Stock.objects.all().delete()
    
stock_delete()
