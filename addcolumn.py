#add a column of data to the file so that it's the same size as the Ha file.
from astropy.io import fits

data, header = fits.getdata("r_night_2_shifted.fits", header=True)

extracolumn = np.zeros(2088)
extracolumn.fill(9611.68359375)
data2 = np.c_[data,extracolumn]
fits.writeto('r_night_2_reprojected_final.fits',data2,header)

