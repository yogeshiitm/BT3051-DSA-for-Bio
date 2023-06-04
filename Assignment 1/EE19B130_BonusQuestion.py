"""
	BT3051 Data Structures and Algorithms for Biology - 2022
	Name - Yogesh Agarwala
	Roll - EE19B130

	Assignment: 1
	Q6. Bonus Question
"""

def translate_to_protein(str):
	for i in range(len(str)):
		if(protein_map[str[i:i+3]]=="Met"):
			break

	result = ""
	i += 3
	while(protein_map[str[i:i+3]] != "Stop" and i+3<len(str)):
		result = result + protein_map[str[i:i+3]] + "-"
		i += 3

	if(result[-1]=="-"):
		return result[:-1]
	return result


protein_map = {
	"UUU":"Phe","UUC":"Phe","UUA":"Leu","UUG":"Leu","CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu","AUU":"Ile","AUC":"Ile","AUA":"Ile","AUG":"Met","GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val",
	"UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser","CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro","ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr","GCU":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala",
	"UAU":"Tyr","UAC":"Tyr","UAA":"Stop","UAG":"Stop","CAU":"His","CAC":"His","CAA":"Gln","CAG":"Gln","AAU":"Asn","AAC":"Asn","AAA":"Lys","AAG":"Lys","GAU":"Asp","GAC":"Asp","GAA":"Glu","GAG":"Glu",
	"UGU":"Cys","UGC":"Cys","UGA":"Stop","UGG":"Trp","CGU":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg","AGU":"Ser","AGC":"Ser","AGA":"Arg","AGG":"Arg","GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly"
}

str = "AUGGCAACAAGUCAUUGGAAUCGUUCCUUU"
print(translate_to_protein(str))