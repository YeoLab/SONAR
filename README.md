# SONAR

SONAR is an algorithm to predict proteins' RNA-binding capability based on their protein-protein interaction neighborhood. This program will run SONAR with your PPI network edge list and RBP annotation list and give you a score table which contains the classification scores for all the proteins appearing in the PPI network. The immediate result (i.e. feature table involved in the classification) will also be presented. The program may run for several hours, please be patient.
## Install
> cd SONAR_directory

> python setup.py install #PS: Please use the version: python 2.7.*

## Usage:
1. Enter the SONAR software folder. 
2. sonar -e Edge_list_File -r RBP_annotation_list [-p num_processes] [--outfile_feature_table feature_table_filename] [-o score_table_filename] [-R num_repeats]
3. If the input files are not in the SONAR software folder, you have to
specify the paths of these files in front of the filenames. By default, the output files will be put in the SONAR software folder. If you wanna make them in other folders, please specify the path of the folder in front of the filenames.

## Example:
sonar -p 16 -r SONAR_directory/SONAR/Demo/RBP_merged_list.txt -e SONAR_directory/SONAR/Demo/BioPlex_interactionList_v4_edgelist.txt --outfile_feature_table=BioPlex_PPI_feature_table.xls -o SONAR_score_table_BioPlex_human.xls

## Alternative way for run the program (i.e. directly run python scripts):
### Prerequisite: 
        python2.7
        python packages: pandas, networkx, numpy, multiprocessing, argparse, sklearn. 
### Usage:
        1. Enter the SONAR software folder
        2. python SONAR_directory/SONAR/Demo/sonar.py -e Edge_list_File -r RBP_annotation_list [-p num_processes] [--outfile_feature_table filename] [-o outfile] [-R num_repeats]
        3. If the input files are not in the SONAR software folder, you have
to specify the paths of these files in front of the filenames. By default, the
output files will be put in the SONAR software folder. If you wanna make them
in other folders, please specify the path of the folder in front of the
filenames.


Please contact me if you have problems running this program.
Email address: wenhao.jin@u.nus.edu (Wenhao Jin)



Wenhao Jin

5 Sep, 2016
