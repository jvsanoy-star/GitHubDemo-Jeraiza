def main():
	try:
		file = open("example.txt", "w")
		file.close()
		print("File created successfully.")
	except IOError:
		print("Failed to create the file.")

if __name__ == '__main__':
	main()