# twintScrapper

# Projet Walletexplorer : 


* Projet réalisé dans le cadre de l'UE POM pour l'extraction des informations relatives aux bitcoins sur les réseaux sociaux 


## Authors 


* POITEVIN Louis & AMINI Khaled

* Encadrant : CAZABET Remy


## Required 


* python : <code>sudo apt-get install python3</code>

* twint : <code>sudo pip3 install twint</code>


## Objectif


* Associer les adresses bitcoins a des utilisateurs sur twitter


## How to 


* <code>git clone https://forge.univ-lyon1.fr/p1410541/twintscrapper</code>

* <code>cd twintscrapper</code>

* <code>python3 main.py </code>

## Optionnal Arguments parse

optional arguments:
  * -h, --help  show this help message and exit
  * -n [N]      number of threads. 10 by default
  * -s [S]      search value. 'search bictoin address' by default

exemple : 

* <code> python3 main.py -n 100 -s 'bitcoin adresses" </code>



