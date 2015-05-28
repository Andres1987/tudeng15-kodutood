#!/usr/bin/env python3

"Valgu koostise arvutaja"

__author__ = "Andres Maser"
__copyright__ = "Copyright 2015, Minufirma"
__credits__ = ["Maria Fomitsenko", "Andres Maser",]
__version__ = "0.001"
__email__ = "andresmaser@gmail.com"

from Bio import SeqIO
from Bio import Entrez
from Bio.SeqUtils import ProtParam
from Bio.Alphabet import IUPAC
Entrez.email = "A.N.Other@example.com"

"""See programmi osa otsib andmebaasist faili"""

def get(ID):
    return Entrez.efetch(db="protein", id=str(ID), rettype="fasta")
	
def read(fasta): # loeb etteantud FASTA faili
    for seq_record in SeqIO.parse(fasta, "fasta",IUPAC.protein):
        print("J2rjestus:",seq_record.seq)
    return(seq_record.seq)
    
"""See osa kirjutab l6pu ning on peamoodul"""	
	
def main(): #fasta sisend
    ID =input() #Anna valgu ID 
    fasta = get(ID) 
    sequence = read(fasta)
    from_fasta = ProtParam.ProteinAnalysis(str(sequence))
    
    #need print-laused annavad kohe vastuse konsooli
    print("\n","Valgu pikkus:",len(sequence))
    print("\n","Molekulaarmass:",from_fasta.molecular_weight())
    print("\n","Aminohappeid:",from_fasta.count_amino_acids())
          
    """Teksti faili output koosneb pikkusest, molekulaarmassist ja aminohapete loendist """
   
    text_file = open("Valgu_andmed.txt", "w")
    text_file.write("\n Length = ")
    text_file.write(str(len(sequence)))
    text_file.write("\n MW = ")
    text_file.write(str(from_fasta.molecular_weight()))
    text_file.write("\n aa = ")
    text_file.write(str(from_fasta.count_amino_acids()))
    text_file.write("\n aa% = ")
    text_file.write(str(from_fasta.get_amino_acids_percent()))
    text_file.close()

if __name__ == "__main__":
    main()
