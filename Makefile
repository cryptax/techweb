MARKDOWN_FILES = $(wildcard *.md)
HTML_FILES = $(patsubst %.md,%.html,$(MARKDOWN_FILES))

all : $(HTML_FILES)

%.html : %.md
	pandoc $< --self-contained -s --toc -c pandoc.css -o $@

clean:
	rm -f $(HTML_FILES)
