import argparse
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument('-v', '--variable', default=[], action='append')
