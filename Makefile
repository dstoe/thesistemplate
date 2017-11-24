# Always run latexmk
.PHONY: all plots clean

# "all" target
all: doc.pdf

# CUSTOM BUILD RULES
#
#%.tex: %.raw
#        ./raw2tex $< > $@

# MAIN LATEXMK RULE

# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -pdflatex="" tells latexmk to call a specific backend with specific options.
# -use-make tells latexmk to call make for generating missing files.
# -interactive=nonstopmode keeps the pdflatex backend from stopping at a
#  missing file reference and interactively asking you for an alternative.

doc.pdf: plots doc.tex
	latexmk -jobname=build/doc -pdf -pdflatex="pdflatex -interaction=nonstopmode -file-line-error" -use-make doc.tex

clean:
	latexmk -CA

plots:
	make -C plots
