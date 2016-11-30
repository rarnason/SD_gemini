from astropy.io import fits

data, header = fits.getdata("r_night_2_shifted.fits", header=True)

header['CRVAL1'] = 14.9913082325231 + 1.25E-5
header['CRVAL2'] = -33.7331611203648 - 6.9625E-5

fits.writeto('r_night_2_test_alt.fits', data, header, clobber=True)
