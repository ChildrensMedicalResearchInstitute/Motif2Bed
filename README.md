# Motif2Bed
Finds motifs in a fasta file and generates a bed file with the motifs location.

## Getting Started

git clone repository 
```
git clone https://github.com/ChildrensMedicalResearchInstitute/Motif2Bed.git
cd Motif2Bed
```

### Prerequisites

This script needs Python 3, pandas and biopython.

```
sudo pip3 install biopython pandas
```

## Installation
Installation can be done with the following command:
```
sudo python3 ./setup.py install 
```

## Usage

This script generates a bed file with motifs extracted from a fasta file.
It requires an input file in fasta format, output file name and list of motifs.

Example:
```
motif2bed.py -i input.fa -o motifs.bed -m TTAGGG TCAGGG TTTTTAAAGGGGCC
```
To see the full set of options run the script with -h flag:
```
motif2bed.py -h
usage: motif2bed.py [-h] [-s] [-d] -i INPUT -o OUTPUT -m MOTIFS [MOTIFS ...]

Generates a bed file with motifs extracted from a fasta file.

optional arguments:
  -h, --help            show this help message and exit
  -s, --silent          Starts in silent mode, no message will be output.
  -d, --debug           Shows debug info
  -i INPUT, --input INPUT
                        Input fasta file
  -o OUTPUT, --output OUTPUT
                        Output bed file
  -m MOTIFS [MOTIFS ...], --motifs MOTIFS [MOTIFS ...]
                        List of motifs

Children's Medical Research Institute - Bioinformatics team 
```

## Usage Example

In this example, we want to find the Foxd1 motif (binding site = GTAAACA) over mouse genome (mm10). Then, we will find out if the motif overlaps with any gene, promoter or gene+promoter region across the genome. At the end, we use R to extract the statistics and visulaization (if needed).
You will need to install the following packages:
* bedtools; https://bedtools.readthedocs.io/en/latest/content/installation.html
* gtf2bed (bedops); https://bedops.readthedocs.io/en/latest/content/installation.html#installation

1- Defining variables and finding the motif across the mm10 genome:
```
genome=mm10
fasta=PATH_TO_mm10/genome.fa
gtf=PATH_TO_mm10/genes.gtf
fastaIndex=PATH_TO_mm10/genome.fa.fai
promoterLength=2000
GeneMotif=Foxd1_motifs

motif2bed.py  -i $fasta -o ${GeneMotif}.bed -m GTAAACA -r
```

2- Converting the gtf file to bed file and only keeping `gene` in the bed file. 
```
cat $gtf  | sed '/#/d' > ${genome}.gtf
awk '{ if ($0 ~ "transcript_id") print $0; else print $0" transcript_id \"\";"; }' ${genome}.gtf | gtf2bed - > ${genome}.sorted.bed
grep -P "HAVANA\tgene" ${genome}.sorted.bed > ${genome}_genes.bed
```

3- Extracting promoter and promoter+gene coordinates:
In this example, we use 2 kb upstream as promoter. 
```
bedtools flank -i ${genome}_genes.bed -g $fastaIndex -l $promoterLength -r 0 -s  > ${genome}_promoters.bed
bedtools slop -i ${genome}_genes.bed -g $fastaIndex -l $promoterLength -r 0 -s  > ${genome}_PromoterPlusGenes.bed
```
4- Extracting the genes/promoters with motif
```
bedtools intersect -wa -wb -a ${genome}_genes.bed -b ${GeneMotif}.bed > ${genome}_genes-${GeneMotif}s.bed
bedtools intersect -wa -wb -a ${genome}_promoters.bed -b ${GeneMotif}.bed > ${genome}_promoters-${GeneMotif}.bed
bedtools intersect -wa -wb -a ${genome}_PromoterPlusGenes.bed -b ${GeneMotif}.bed > ${genome}_PromoterPlusGenes-${GeneMotif}.bed
```
5- Extracting the list of the interestd genes which has motif. For example, if you have a list of differentially expressed genes (DEGs) and want to see if these genes are affected by this motif, you may run the script below in R.

```
library(tidyverse)
library(dplyr)

baseDir <- getwd()
beds <- list.files(path = baseDir, pattern = "_motif.bed")
motif <- lapply(beds, function(x){
    read.delim(paste0(baseDir, x), header = FALSE)
})
names(motif) <- c("promoter", "gene", "promoter.gene")

# Number of promoter/genes in mm10 genome with motif (GTAAACA)

lapply(motif, function(x){
    x$geneID %>% sort() %>% unique() %>% length()
})

# List of differentially expressed genes (DEGs)
DEGs <- c("Gem", "Zic1", "Zic2", "Twist1", "Foxa2", 
           "Lhx1", "Otx2", "Hesx1","Sox9")

# Keep only motifs overlapping with DEGs
motif.DEGs <- lapply(motif, function(x){
    x[x$geneID %in% DEGs, ]
})

# Number of motifs for each DEGs
lapply(motif.DEGs, function(x){
    table(x$geneID)
})
```

## History

First release September 2021

## Credits

Author(s): Pablo Galaviz and Nader Aryamanesh        
Email:  pgalaviz@cmri.org.au 


**Children’s Medical Research Institute, finding cures for childhood genetic diseases**  

## License

Edit license statement or refer to file. 

Motif2Bed is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

Motif2Bed is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Motif2Bed.  

If not, see <http://www.gnu.org/licenses/>.
