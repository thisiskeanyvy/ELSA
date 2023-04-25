import os

def clear():
   if os.name == 'nt':
       _ = os.system('cls')
   else:
       _ = os.system('clear')

def readContent():
	dataset_file_number = input("Numéro de la dataset : ")
	dataset_file = open(f'data/elsa_dataset_{dataset_file_number}_content.txt', "r")
	dataset_data_str = dataset_file.read()
	dataset_file.close()
	print(dataset_data_str)

if __name__ == "__main__":
	readContent()