"""
This module implements some interesting algorithmic challenges on strings
"""


def remove_duplicates(s):
	"""
	Given a string, remove duplicate characters, retaining only the first time for each unique character.
	Example: helloh -> helo
	"""
	unique_chars = set()
	new_string = ""
	for char in s:
		if char not in unique_chars:
			new_string += char
			unique_chars.add(char)
	return new_string


def main():
	s = "Hello, my friend liam"
	print(remove_duplicates(s))


if __name__ == "__main__":
	main()
