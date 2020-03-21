# munspace

## Utility for using rgb colors that approximate the Munsell color space in Python.

To use these:

1.  Clone the repository or copy the files (at minimum) `munspace.py` and 
    `munsell_chips.csv` to your working directory.
2.  In your Python file include `import munspace` or `from munspace import hvc`
3.  `munspace.hvc` has the following signature:

        hvc(h, v = 5, c = 'middle'):
        """
        returns rbg hex string of 'high', 'middle' or 'low' chroma=c for munsell
        h=hue, v=value.

        defaults to 'middle' chroma.
        """
    Hues available will be in the list `hues`, values run from 1 to 9,
    and simple chroma ranges are from `['low', 'middle', 'high']`

    Hues available are (see also the list variable `hues`)
    
        2.5R 5R 7.5R 10R 2.5YR 5YR 7.5YR 10YR 
        2.5Y 5Y 7.5Y 10Y 2.5GY 5GY 7.5GY 10GY 
        2.5G 5G 7.5G 10G 2.5BG 5BG 7.5BG 10BG 
        2.5B 5B 7.5B 10B 2.5PB 5PB 7.5PB 10PB 
        2.5P 5P 7.5P 10P 2.5RP 5RP 7.5RP 10RP
    
Note that these will only be approximations, and will depend on the 
color temperature of your display, etc.

See `use-munspace.ipynb` for the example below:

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
