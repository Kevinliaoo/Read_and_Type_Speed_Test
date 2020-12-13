# Reading and typing speed test

This program is a reading and typing speed test written in python. For the typing test, the program will show some words the user has to type, once finished, results will show up (letters per minute typed), on the other hand, for the reading mode, the program will randomly scrape a Wikipedia summary for the user to read, and once finished the words per minute read will be displayed. 

## Instalation 

```bash
python -m venv venv 
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Running 

```bash
python run.py
```

## Instructions 
There is a file in ./texts called words.txt, in this file the user has to insert some words separated by a comma (,), these words will be the words displayed at the typing test, and for the reading test, will randomly scrape the summary from Wikipedia. 
<br>
<br>
### Reading mode
To enter the read mode, just click "R", then a text will be displayed for the user to read, once finished click "enter" and results will appear. 
### Typing mode 
To enter typing mode, click "T" and random words are going to start appearing for the user to type, one finished, click "enter" and the user's performance will be shown.

## Author

Kevin Liao - @kevinliaoo