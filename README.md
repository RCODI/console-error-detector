# console-error-detector
Python script to detect console that shows up in firebug

##Description
A set of scripts which takes a CSV file as input corresponding to Ironhack participants project links and outputs a file corresponding to the console error thrown by each of these projects

##Initial Setup
Python3 is required to run this script. It can be downloaded [here](https://www.continuum.io/downloads)


Change chromeLoc variable in `config.py` to point to location of Chrome executable


Change logLoc variable in `config.py` to point to location of chrome-debug.log. It is the file where your chrome debug log output goes by default. More details [here](http://stackoverflow.com/questions/7627113/save-the-console-log-in-chrome-to-a-file)


Change inputFileLoc variable in `config.py` to point to location of the input CSV file.
Format of input CSV file is
```javascript
Id, Name, Web url, Irrelevant column1, Irrelevant column2
```

Output CSV file would have format
```
Id, Name, Web url, Errors seperated by '|'
```


##Usage
1. Open a console with admin access

2. Execute the command:
```sh
python3 error_detector.py
```


```