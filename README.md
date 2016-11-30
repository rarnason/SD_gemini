# SD_gemini
Source extractor (sextractor) detection/photometry files for the Gemini GMOS imaging data of the Sculptor Dwarf Galaxy 

Files:

***Sextractor***
default.sex
default.param
default.conv

test2.cat - output catalog created by sextractor

***Region files***
*.reg - region files created from 8 sources common to both r- and Ha-band images

***Scripts***
shift.py - Calculates shift between the r- and Ha-band images
header_edit.py - Modifies the header of the r-band image to have the same WCS mapping as the Ha-band image
