#!/usr/bin/python3
def uppercase(str):
	for i in str:
		print("{}".format(chr(ord(i) - 32) if 122 >= ord(i) >= 97 else "{}".format(i)), end="")
	print()
