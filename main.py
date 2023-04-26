import os, json, base64

def clear():
   if os.name == 'nt':
       _ = os.system('cls')
   else:
       _ = os.system('clear')

def banner():
	print("""\033[1;35;49m
	E.L.S.A (Electronic Learning and Scrapping Algorithm)
	\033[1;37;49m""")
	print("""
   - Commandes :
   /help (Obtenir la liste des commandes)
   /quit (Quitter le programme)
	""")

def offlineLookup():
	param = input("\033[1;32;49m- Rechercher : \033[1;37;49m")
	if param == "/quit":
		exit()
	elif param == "/help":
		print("""
\033[1;33;49m--- E.L.S.A v1.0 ---\033[1;37;49m
 *Utilisation : python3 main.py
 -RECHERCHE :
     La recherche fonctionne sans avoir besoin d'une connexion Internet
 -DATASET :
     Le dossier contenant les datasets utilisées pour la recherche est 'data/'
     Ex: elsa_dataset_1.txt, elsa_dataset_2.txt (encodage en base64)
		""")
	elif param == "":
		print("""\033[1;33;49m
  Ce champ permet d'interagir avec E.L.S.A pour rechercher une information...
		\033[1;37;49m""")
	param_encoded = base64.b64encode(bytes(param, 'utf-8'))
	param_encoded = param_encoded.decode("utf-8")
	if os.path.isdir("data") == False:
		print("""\033[1;33;49m
  Le dossier contenant les datasets ('data/') est introuvable...
		\033[1;37;49m""")
	data_files = os.listdir('data/')
	data_files_datasets = []
	for d in range(len(data_files)):
		if "content" not in data_files[d]:
			data_files_datasets.append(data_files[d])
	result_found = 0
	for f in range(len(data_files_datasets)):
		if data_files_datasets[f] == f"elsa_dataset_{f+1}.txt":
			dataset_files = data_files_datasets[f]
			dataset_file = open(f'data/{dataset_files}', "r")
			dataset_data_str = dataset_file.read()
			dataset_file.close()
			dataset_data = json.loads(dataset_data_str)
			for i in range(len(dataset_data["n"])):
				name_encoded = dataset_data["n"][i]
				category_encoded = dataset_data["c"][i]
				summary_encoded = dataset_data["s"][i]
				name = base64.b64decode(bytes(name_encoded, 'utf-8'))
				name = name.decode("utf-8")
				category = base64.b64decode(bytes(category_encoded, 'utf-8'))
				category = category.decode("utf-8")
				summary = base64.b64decode(bytes(summary_encoded, 'utf-8'))
				summary = summary.decode("utf-8")
				if param_encoded == name_encoded:
					result_found = 1
					print(f"""
\033[1;33;49mCategorie :\033[1;37;49m {category}
\033[1;33;49mRésumé :\033[1;37;49m {summary}
					""")
					break
	if result_found == 0 and param != "/help" and param != "":
		print(f"""
\033[1;33;49mCategorie : \033[1;31;49m!\033[1;37;49mAucune donnée
\033[1;33;49mRésumé : \033[1;31;49m!\033[1;37;49mAucune donnée
		""")

if __name__ == "__main__":
	clear()
	banner()
	while True:
		try:
			offlineLookup()
		except:
			print("\n\n \033[1;31;49m*\033[1;37;49mFermeture du programme...\n")
			break