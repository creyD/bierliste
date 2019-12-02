# Bierliste/ Beerlist

# Content

1. Installation (DE)
1. Installation (EN)
2. Mitwirkende/ Contributors
3. Fehler/ Bugs

# Installation (DE)

## Vorraussetzungen

Python 3 und PiP sollten installiert sein.

## Testumgebung installieren

- Repository klonen
- Kommandozeile der Wahl im geklonten Ordner öffnen
- Module installieren mit pip: `pip install -r requirements.txt`
- Datenstruktur auf lokale Datenbank anwenden: `python src/manage.py migrate`
- (optional) Verwaltungsnutzer erstellen mit `python src/manage.py createsuperuser`


- Server starten `python src/manage.py runserver`


# Installation (EN)

## Prequisites

Python 3 with pip should be installed.

## Install testing environment

- Clone repo
- Open shell in cloned folder
- Install modules with pip: `pip install -r requirements.txt` (<a href="https://virtualenv.pypa.io/en/latest/">Please consider using virtual environments!</a>)
- Migrate data structure: `python src/manage.py migrate`
- (optional) Create super user: `python src/manage.py createsuperuser`


- Start test server `python src/manage.py runserver`


# Mitwirkende/ Contributors

You may add yourself here.

# Fehler/ Bugs

Bitte fehler <a href="https://github.com/creyD/bierliste/issues">hier melden</a>. Please report bugs <a href="https://github.com/creyD/bierliste/issues">here.</a>
