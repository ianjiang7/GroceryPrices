# PuzzleAsker
This scraper scrapes Geeks for Geeks' top 20 most commonly asked brainteasers/puzzles in SDE interviews. This project is intended to help interviewees practice these brainteasers in a flashcard-like style

## The Website
This was the website used:
```https://www.geeksforgeeks.org/top-20-puzzles-commonly-asked-during-sde-interviews/?ref=outind```
I chose this website because it allowed webscraping and the html was simple. This simple html means it would be straightforward to webscrape.

## Usage
1. Run this command in the terminal:

  ```git clone https://github.com/ianjiang7/PuzzleAsker.git```

2. cd in the directory and set up a virtual environment:

  ```python -m venv .venv```
  
3a. Activate venv on Windows:

  ```.venv\Scripts\activate```

3b. Activate on macOS and Linux:

  ```source .venv/bin/activate```

4. Install requirements:
  ```pip install -r requirements.txt```

5. Run main.py:

   ```python main.py```
