TEX=pdflatex
NOWEBOPTS=-latex -n
FILE=main

all: extract_code
	$(TEX) $(FILE)
	$(TEX) $(FILE)

extract_code: defs
	noweave $(NOWEBOPTS) -indexfrom $(FILE).defs nw/tmp.nw > tex/tmp.tex.in
	./filter-uses.py < tex/tmp.tex.in > tex/tmp.tex

defs:
	-rm $(FILE).defs $(FILE).tmp.defs
	nodefs nw/tmp.nw > $(FILE).tmp.defs
	sort -u $(FILE).tmp.defs | cpif $(FILE).defs