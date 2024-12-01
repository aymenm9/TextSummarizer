# Générateur de Résumés Automatiq

## Description : 

Créez une application pour gérer une collection de musique, où chaque
morceau est stocké dans une table de hachage selon le titre ou l'artis

### Fonctionnalités

    - Chargement d'un texte long
    - Génération d'un résumé concis
    - Options pour ajuster la longueur du résumé

#### how to use it
##### recomended 

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
##### dependnses

    ```bash
    pip install sumy nltk numpy
    ```
##### run the program

    ```bash
    python3 main.py -i text1.txt -o text1o.txt -a TextRank -l 6 -sl 3 -lang english
    ```
    usage: main.py [-h] [-i INPUT] [-o OUTPUT] [-a {TextRank,Luhn,LSA}] [-l LIMIT] [-sl SENTENCE_LIMIT] [-lang LANGUAGE]

    options:
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                            the input text file name
    -o OUTPUT, --output OUTPUT
                            the output text file name
    -a {TextRank,Luhn,LSA}, --algorithm {TextRank,Luhn,LSA}
                            'TextRank' for TextRank Algorithm. 'Luhn' for Luhn's Algorithm. 'LSA' for Latent Semantic Analysis.
    -l LIMIT, --limit LIMIT
                            The max number of sentences to include in the summary.
    -sl SENTENCE_LIMIT, --sentence_limit SENTENCE_LIMIT
                            The max number of sub-sentences or words to include in the summary.
    -lang LANGUAGE, --language LANGUAGE
                            The language of the text. Supported languages: english, french, spanish, german, italian, portuguese, russian, dutch, czech, slovak.