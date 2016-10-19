import numpy as np

def elerToDecartXYZ(a, e, i, om, w, m):
	u = w
	E = m
	r = a * (1 - e * np.cos(E))
	x_or = r * np.cos(u)
	y_or = r * np.sin(u)
	z = y_or * np.sin(i)
	x = x_or * np.cos(om) - y_or * np.cos(i) * np.sin(om)
	y = x_or * np.sin(om) + y_or * np.cos(i) * np.cos(om)
	return [x,y,z]