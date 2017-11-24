.PHONY: all data

BUILD_DIR=../build/fig
DATA_DIR=~/data/dls
# All the plots' names go here
NAMES=parabola

FIGURES=$(NAMES:%=$(BUILD_DIR)/%.pgf)
DATA=$(NAMES:%=$(BUILD_DIR)/%.npz)

all: directories $(DATA) $(FIGURES)

data: directories $(DATA)

directories:
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/%.pgf: plot_%.py $(BUILD_DIR)/%.npz matplotlibrc
	python3 $< $(word 2,$^) --save $@

$(BUILD_DIR)/%.npz: make_%.py
	python3 $< --save $@
