.ONESHELL:
SHELL = /bin/bash

env:
	source /srv/conda/etc/profile.d/conda.sh
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name ligo_environment --display-name "IPython - ligo_environment"
    
.PHONY: html
html:
	jupyter-book build .
    
.PHONY: clean
clean:
	rm -rf figures/*
	rm -rf audio/*
	rm -rf _build/*