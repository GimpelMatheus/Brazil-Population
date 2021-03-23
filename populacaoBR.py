#Crescimento da pop BR

import matplotlib.pyplot as plt

def population():
	dados = open("original.csv").readlines()

	anos = []
	populacao = []

	for i in range(len(dados)):

		if i != 0:
			linha = dados[i].split(";")
			anos.append(int(linha[0]))
			populacao.append(int(linha[1]))


	plt.title("Crescimento da População Brasileira 1980 - 2016")
	plt.xlabel("Ano")
	plt.ylabel("População x 10^8")


	plt.bar(anos, populacao, color = "red")
	plt.plot(anos, populacao, color = "k", linestyle = "--")

	plt.savefig("PopulaçãoBR.png", dpi = 300)

if __name__ == "__main__":
	population()