# Template for a Thesis

This template requires `latexmk` for the build and the `texlive-fonts-extra` package for the fonts:
```bash
sudo apt install latexmk texlive-fonts-extra
```

## Build the Template

Run
```bash
make
```
from within the base folder. The final document is then located in the `build` folder at `build/doc.pdf`.

## How the Plotting Works

The `Makefile` in the `plots` configures which plots should be build with the `NAMES` variable. All the plots' names should go there, separated by spaces, for example:
```Makefile
NAMES=parabola sine
```
This will generate the plots with the names `parabola` and `sine`. These plots can be included in the document as shown for the parabola in the template. From these names, the `make`-rule tries first to generate the necessary data for the plot with
```bash
python3 make_paraboly.py --save ../build/fig/parabola.npz
```
The plotting is then done with
```bash
python3 plot_paraboly.py ../build/fig/parabola.npz --save ../build/fig/parabola.pgf
```
Therefore, all data files and plots are located in the `build/fig` folder. If the plots should be generated with the `python` interpreter, instead of `python3` the according rule can be changed in `plots/Makefile`. The`make`-based workflow should take care that plots are only regenerated if the data-script, plotting-script or the `matplotlibrc` is changed. The generation of data and the plotting is separated such that the plotting is still fast, even if generating the data takes a long time.

The appearance of all plots can be changed with the `plots/matplotlibrc` file. Currently it is configured for example to not show the upper left spines.
