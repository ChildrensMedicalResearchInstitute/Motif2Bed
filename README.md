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
## History

First release September 2021

## Credits

Author: Pablo Galaviz              
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