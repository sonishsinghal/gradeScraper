# GradeScraper

First install the libraries
```sh
$ pip install -r requirements.txt
```
Run the server
```sh
$ python app.py
```

If you want to host the server online for production, then before deploying update this
```py
if(__name__ == "__main__"):
    app.run(debug=True)
```
to
```py
if(__name__ == "__main__"):
    app.run()
```
