import numpy as np

def toZiroTwoPi(fi_):
    while (fi_ < 0) or (fi_ > 2 * np.pi):
        if fi_ < 0:
            fi_ += 2 * np.pi
        if fi_ > 2 * np.pi:
            fi_ -= 2 * np.pi
    return fi_

def elerToDecartXYZ(a, e, i, omega, w, t_obs, t_oe, eps = 1e-12,c = 299792458, M_kg = 5.97236255464e+24,M_g = 5.97236255464e+27, grav_kg = 6.674083131313131e-11,grav_g = 6.674083131313131e-8,mu = 3.986004418e+14):

	if M_kg != 5.97236255464e+24 or grav_kg !=6.674083131313131e-11:
		mu = M_kg * grav_kg
	elif M_g != 5.97236255464e+27 or grav_g !=6.674083131313131e-8:
		mu = M_g * grav_g

	n_0 = np.sqrt(mu / np.power(a,3))
	t_em = t_obs
	t = t_em - t_oe
	
	if t > 302400:
		t = t - 604800
	elif t < - 302400:
		t = t + 604800

	n = n_0

	M = M_0 + n * t
	M = toZiroTwoPi(M)

	E = M
	E_ = M + 1
	while (np.abs(E - E_) > eps):
		E_ = E
		v = 2 * np.arctan(np.sqrt((1+n)/(1-n)) * np.tan(E/2))
		E = M + e * np.sin(E)

	E = toZiroTwoPi(E)

	X_orb  = a*(np.cos(E) - e)
	Y_orb = a * np.qwrt(1 - np.power(e,2)) * np.cos(E)
	
	u = w
	X_ = X_orb * np.cos(u)
	Y_ = Y_orb * np.sin(u)

	x = X_ * np.cos(omega) - Y_ * np.cos(i)* np.sin(omega)
	y = Y_ * np.sin(omega) - Y_ * np.cos(i)* np.cos(omega)
	z = Y_ * np.sin(i)
	
	return [x,y,z]