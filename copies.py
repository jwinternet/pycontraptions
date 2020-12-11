#!/usr/bin/env python3
"""Password Generator"""

__author__ = "Jared Winter"
__started__ = "12/2/2020"
__revision__ = "v0.1.0"

import subprocess
import readline


class Copies:

	def __init__(self, name, extension, amount):
		self.name = name
		self.extension = extension
		self.amount = int(amount) + 1

	def create_copies(self):
		for number in range(1, self.amount):
			file_number = str(number) + self.extension
			subprocess.call(["cp", self.name, file_number], stdout=subprocess.DEVNULL)


if __name__ == "__main__":
	file_name = input(" Original file: ")
	file_extension = input("File extension: ")
	amount_of_copies = input(" Amount of copies: ")
	my_order = Copies(file_name, file_extension, amount_of_copies)
	my_order.create_copies()
