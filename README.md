# Práctica 1: Web scraping

## Descripció

Aquesta és la primera pràctica de l'assignatura _Tipologia i cicle de vida de les dades_ del Màster en Ciència de Dades de la Universitat Oberta de Catalunya. L'objectiu d'aquesta pràctica és a aprendre a identificar les dades rellevants per un projecte analític i usar les eines d'extracció de dades. Per això s'utilitzaran tècniques de Web Scrapping per tal de poder obtenir i analitzar la informació.

## Membres del grup

La pràctica ha sigut realitzada en grup format per  **Marc Ramos Bruach** i **Marc Ferrer Margarit**

## Fitxers i estructura

* **Covid19_WebScrapping.ipynb**: Respostes a les preguntes realitzades en l'enunciat.
* **src/coronavirus.py**: conté la implementació de la classe que s'encarrega de generar el conjunt de dades partint de la base de dades [COVID-19 situation update worldwide](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases).
* **src/requirements.txt**: conté les llibreries necessàries per a crear l'entorn i poder executar el codi.
* **csv/covid_notification_world_cases_dataset.csv**: fitxer que conté les dades exportes obtingudes de la pàgina web.

## Configuració de l'entorn

### Creació de l'entorn, activació i instal·lació de llibreries
```
python -m venv env

Windows: /env/Scripts/activate.bat
Mac Os/Linux: source /enve/bin/activate

pip install -r src/requirements.txt
```

### Execució del codi

```
python .\src\coronavirus.py
```

## Asignacions tasques
Marc R:
 - 1, 6, 7, 8


Marc F:
 - 2, 3 ,4, 5
