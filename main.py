
#
# A Python script to get language statistics about a specific code project.
# Copyright. Raúl Gutiérrez Beltrán 2024
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.
#
# Author of this code: Raúl Gutiérrez Beltrán AKA "Gato" <raulgbeltran23@proton.me>
# See CONTRIBUTORS to read all contributors who contributed to this program.
#

import os
import sys

programmingExtensions = {
	"asm": "Assembly",
	"bat": "Batch",
	"c,h": "C",
	"cpp": "C++",
	"cs": "C#",
	"java": "Java",
	"js": "JavaScript",
	"kt": "Kotlin",
	"lua": "Lua",
	"pl": "Perl",
	"php": "PHP",
	"py": "Python",
	"rb": "Ruby",
	"rs": "Rust",
	"sh": "Shell",
	"nut": "Squirrel"
}
markupExtensions = {
	"css": "CSS",
	"html": "HTML + CSS/JS/PHP",
	"json": "JSON",
	"xml": "XML"
}

acceptedExtensions = {}
fileQuantityPerLang = {}
charQuantityPerFile = {}
totalChars = 0

def getFileChars(name: str) -> int:
	file = open(name, "rb")
	print(f"Analyzing {file.name} ...")
	size = len(str(file.read()).replace(" ","").replace("\n","").replace("\t",""))
	return size

def getExtension(bits: str) -> str:
	for exts in acceptedExtensions:
		if bits[len(bits)-1] in exts.split(","):
			return exts
	return ""

def validFile(name:str) -> bool:
	split = name.split(".")
	return split[0]!=""

def processFiles():

	# Iterating over the list
	global totalChars
	for a in filenamesList:
		filenameSplit = a.split(".")
		ext = getExtension(filenameSplit)
		if ext != "":
			try:
				chars = getFileChars(a)
				totalChars += chars
				if ext in charQuantityPerFile:
					fileQuantityPerLang[ext] += 1
					charQuantityPerFile[ext] += chars
				else:
					fileQuantityPerLang[ext] = 1
					charQuantityPerFile[ext] = chars
			except FileNotFoundError:
				print(f"ERROR: File not found ({a}). Might have been deleted?")

# Returns the size of bytes into readable format.
# By "whereisalext" in https://stackoverflow.com/a/31631711 [CC BY-SA 4.0]
def size(bytes):

	bytes = float(bytes)
	KB = float(1024)
	MB = float(KB ** 2)
	GB = float(KB ** 3)
	TB = float(KB ** 4)

	if bytes < KB:
		return '{0} {1}'.format(bytes,'Bytes' if 0 == bytes > 1 else 'Byte')
	elif KB <= bytes < MB:
		return '{0:.2f} KB'.format(bytes / KB)
	elif MB <= bytes < GB:
		return '{0:.2f} MB'.format(bytes / MB)
	elif GB <= bytes < TB:
		return '{0:.2f} GB'.format(bytes / GB)
	elif TB <= bytes:
		return '{0:.2f} TB'.format(bytes / TB)


if __name__ == "__main__":

	dir = ""
	try:
		if sys.argv[1] in ["-P","-M"]:

			if sys.argv[1] == "-P":
				acceptedExtensions = programmingExtensions
				if sys.argv[2] != "":
					dir = sys.argv[2]
				else:
					dir = "."
			else:
				acceptedExtensions = markupExtensions

				if sys.argv[2] != "":
					dir = sys.argv[2]
				else:
					dir = "."

		elif sys.argv[1] != "":
			dir = sys.argv[1]
			acceptedExtensions.update(programmingExtensions)
			acceptedExtensions.update(markupExtensions)
		else:
			print("Wrong argument")
			exit()
	except IndexError:
		dir = "."
		acceptedExtensions.update(programmingExtensions)
		acceptedExtensions.update(markupExtensions)

	# Saves recognized files into the list
	print(f"Discovering files in {dir} ...")
	filenamesList = []
	for root, dirs, files in os.walk(dir):
		for a in files:
			filenamesList.append(str(os.path.join(root, a)))

	# Non recognized files are removed
	filenamesList += list(filter(validFile, filenamesList))
	print("Analyzing files...\n")
	processFiles()

	# Sorting by char quantity
	charQuantityPerFile = dict(sorted(charQuantityPerFile.items(), key=lambda e: e[1], reverse=True))

	i = 1
	print("Summary of all written code:")
	for e,c in charQuantityPerFile.items():
		print(f"\t{i}# ·{acceptedExtensions[e]} ({fileQuantityPerLang[e]} files) -> {round((c/totalChars)*100, 2)}% ({c})")
		i += 1

	print(f"Chars of code written: {totalChars}\n")
	print(f"Size of all code analyzed: {size(totalChars)}")
