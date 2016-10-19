import cos, sin from numpy

def elerToDecartXYZ(a, e, i, om, w, m):
	u = w
	E = m
	r = a * (1 - e * cos(E))
	x_or = r * cos(u)
	y_or = r * sin(u)
	z = y_or * sin(i)
	x = x_or * cos(om) - y_or * cos(i) * sin(om)
	y = x_or * sin(om) + y_or * cos(i) * cos(om)
	return [x,y,z]