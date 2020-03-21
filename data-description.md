# Description of color data files.

**Original at** <https://www.rit.edu/cos/colorscience/rc_munsell_renotation.php>


all.dat: real and unreal

File download: all.dat

These are all the Munsell data, including the extrapolated colors. Note that
extrapolated colors are in some cases unreal. That is, some lie outsize the
Macadam limits.

This file should be used for those performing multidimensional interpolation
to/from Munsell data. You will need the unreal colors in order to completely
encompass the real colors, which is required to do the interpolation when near
the Macadam limits.

real.dat: by the book

File download: real.dat

These are real colors only, "real" being those lying inside the Macadam limits.
Specifically, these are those colors listed the original 1943 renotation article
(Newhall, Judd, and Nickerson, JOSA, 1943).

This file should be used for a complete mapping between the Munsell system and
its CIE equivalents. Note, however, that many of these colors were not used in
the original scaling experiments, and are therefore extrapolated or at best
interpolated from the test colors used.

Flash! Here are sRGB values and CIELAB for most of the colors in the real.dat
file. There are some important notes regarding these data in the spreadsheet.
1929.dat: back to the source

File download: 1929.dat

These are only those colors physically appearing in the 1929 Munsell Book of
Color. These data might be of useful for those interested in the input colors
used for the scaling experiments leading to the 1943 renotation. Remember
though, these are renotation colors of those original patches, not necessarily
the colors of the input data used in the visual experiment.
