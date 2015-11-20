#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Al-Ramaa Lahan <lahangit@gmail.com>.
# NO LICENCE.
"""Open a Python shell with flask and the project imported."""

import os
import readline
from pprint import pprint

os.environ['APP_CONFIG'] = "project.config.DevelopmentConfig"
os.environ['PYTHONINSPECT'] = "True"

from flask import *
from project import *
