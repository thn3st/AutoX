import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if getattr(sys, 'frozen', False):
    ROOT_DIR = os.path.dirname(sys.executable)
elif __file__:
    ROOT_DIR = os.path.dirname(__file__)
