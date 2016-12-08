
from astropy.io import fits
import numpy as np

data, header = fits.getdata("Ha_night_2.fits", header=True)

j=0
for i in np.nditer(data,op_flags=['readwrite']):
	#print i
	if i < 0:
		i[...]=0 


fits.writeto('Ha_night_2_corrected.fits',data,header,clobber=True)

	
