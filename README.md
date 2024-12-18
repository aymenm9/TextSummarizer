# Automatic Summary Generator

## Description

" Développez une application qui résume automatiquement un texte en
utilisant des techniques d'extraction."

### Features

- Load a long text
- Generate a concise summary
- Options to adjust the summary length

### File Structure

Here’s the file structure of the application:

    ```bash
    .
    ├── README.md
    └── project
        ├── __init__.py
        ├── app_argv.py
        ├── choice_algo.py
        ├── file_io.py
        ├── lsa.py
        ├── luhn.py
        ├── main.py
        ├── max.py
        ├── text1.txt
        ├── text1o.txt
        └── text_rank.py
    ```
- *README.md*: This file you're reading.
- *project/*: The folder containing the main scripts of the application.
    - *`__init__.py`*: Initialization of the package.
    - *app_argv.py*: Defines the arguments and options for the program's CLI.
    - *choice_algo.py*: Contains logic to select the summarization algorithm.
    - *file_io.p*: Handles reading from and writing to files.
    - *lsa.py*: Implements Latent Semantic Analysis for text summarization.
    - *luhn.py*: Implements Luhn's summarization algorithm.
    - *main.py*: The main script that processes input, selects algorithms, and outputs the summary.
    - *max.py*: Handles sentence-level summarization using specific limits.
    - *text1.txt*: Input file used for testing summarization.
    - *text1o.txt*: Output file containing the summarized text.
    - *text_rank.py*: Implements the TextRank algorithm for text summarization.

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
    cd project
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
