all: out/catcount.pdf out/datacount.pdf

out/catcount.pdf:
	python3 script/catcount.py

out/datacount.pdf:
	python3 script/datacount.py

clean:
	rm -rf out
