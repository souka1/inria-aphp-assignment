# inria-aphp-assignment
Ce travail est une partie de inria-aphp-assignment, L'objectif général de cette mise en situation est de comprendre les problèmes de qualités de données. La mise   en évidence des doublons dans la base patients et l'estimation du nombre de patients positifs au Covid19 (par tranche d'age, par localisation géographique etc.).

## Technologies

* Python
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scipy
* Pytest
* Jupyter

## Démarche

- Inria_assignment.ipynb
- Inria_assignment.
     - \__init\__.py
     - detect_duplicates.py
     - tests
         - test_duplicates.py
         - test_data.csv
- data.db  

### Inria_assignment.ipynb
C'est le notebook principal qui contient la partie cleaning et preprocessing des données et la partie visualisation.
### Inria_assignment
C'est un package qui contient le module detect_duplicates.py, ce module est importé dans le notebook principal Inria_assignment.ipynb. 
#### -  detect_duplicates.py  
C'est un module qui contient la fonction detect-duplicates qui a pour role detecter et supprimer les doublons.
#### -  \__init\__.py
Ce fichier est appelé à chaque fois on importe le module detect_duplicates.py du package Inria_assignment,
#### -  tests
C'est un dossier qui contient un fichier test_duplicates.py pour tester la fonction detect_duplicates, et un fichier test_data.csv qui represente les données de test.

Pour le test on a utilisé la librairie Pytest qui lance les tests de tous les fichiers qui commencent par  test\_  ou qui finissent par  \_test.
### data.db
C'est un fichier qui représente une base de données sqlite contenant 2 tables. Une table de patients et une table de tests PCR (test utlisé pour le diagnostic du Covid19).
