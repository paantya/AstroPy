#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import AstroPy as ap
import numpy as np

print(ap.elerToDecartXYZ(a=100000,e=0.1,i=1,omega=1,w=np.pi/2,t_obs=0,t_oe=0))