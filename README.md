# Intro to webscraping with python

1. Make sure [Python](https://www.python.org/) is installed on your system.
2. Create folder web-scraping-with-python
3. Open with favorite text editor
4. Create `main.py` file
5. Create first Hello World program by adding the following code to the file.
    ```python
    print("Hello World!")
    ```
    Run program in terminal
    ```linux
    python main.py    
    ```
6. Install [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup) and [requests](https://pypi.org/project/requests/).
    ```linux
    pip install beautifulsoup4 requests
    ```

## Installing on Mac

In a Python 3 environment on a Mac, you may run into errors when trying to import beautifulsoup4 and requests.  Try this in your shell:

```bash
# from (my-env) *[main][/usr/local/projects/python/web-scraping-with-python]$
python3 -m venv my-env
source my-env/bin/activate
pip install beautifulsoup4 requests
python3 main.py
```

