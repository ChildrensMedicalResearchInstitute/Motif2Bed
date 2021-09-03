from setuptools import setup

setup(
    name='motif2bed',
    version='0.0.1',
    packages=['pycmri'],
    url='https://github.com/ChildrensMedicalResearchInstitute/Motif2Bed',
    license='GNU V3',
    author='Pablo Galaviz',
    author_email='pgalaviz@cmri.org.au',
    description='Finds motifs in a fasta file and generates a bed file with the motifs location.',
    requires = [
        "pandas"
        ,"biopython"
        ,"numpy"
    ],
    scripts=['bin/motif2bed.py']

)
