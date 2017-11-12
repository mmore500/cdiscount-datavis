all: out/catcount.pdf out/datacount.pdf out/img-0-0.pdf

out/catcount.pdf:
	python3 script/catcount.py

out/datacount.pdf:
	python3 script/datacount.py

out/img-0-0.pdf:
	python3 script/imgvis.py

clean:
	rm -rf out
