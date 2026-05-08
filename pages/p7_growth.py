import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _production_pages import show_growth

def show():
    show_growth()
