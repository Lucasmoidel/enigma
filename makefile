all: build run
build:
	g++ main.cpp enigma.cpp -o enigma
run:
	./enigma
