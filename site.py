import requests
import os
import subprocess
from selenium import webdriver
import time, random
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
import html
from datetime import datetime, timedelta
import random
import threading
import feedparser
import requests
import xml.etree.ElementTree as ET
import threading



def read_sitemap(url, checker="sitemap"):
    response = requests.get(url)
    with open("new_sitemap.xml", "w",encoding="utf-8") as d:
        d.write(response.text)

    


read_sitemap("https://www.newsquik.online/sitemap.xml","url")