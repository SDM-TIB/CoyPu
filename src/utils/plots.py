import sys

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from io import StringIO
from jupyter_plotly_dash import JupyterDash
from SPARQLWrapper import SPARQLWrapper, CSV, SELECT, POST, POSTDIRECTLY
from urllib.parse import quote_plus
import base64
import json
import pandas as pd
import numpy as np
import plotly.express as px
import requests

print (sys.version)
