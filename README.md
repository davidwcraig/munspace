# munspace

## Utility for using rgb colors that approximate the Munsell color space in Python.

Note that these will only be approximations, and will depend on the 
color temperature of your display, etc.

<figure>

![10 sine waves in Munsell colors](munsell-color-demo.png)

<figcaption>Sine waves in Munsell primary and secondary colors, medium chroma
and value.</figcaption>
</figure>

I was led to the RGB values used by Andrew Werth's very nice
[Virtual Munsell Color Wheel](https://www.andrewwerth.com/aboutmunsell/) and the
Javascript there.

This uses the **Munsell Renotation Data** from:
<https://www.rit.edu/cos/colorscience/rc_munsell_renotation.php>

I have downloaded the files from there: `all.dat` `real.dat` and 
associated `.xlsx` files. I include the text from there in a description file.
