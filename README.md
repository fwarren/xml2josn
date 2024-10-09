Create a pyinstaller executable for converting xml to json
Based on https://gist.github.com/WazeHell/68b27f254208f873863fa67db0dceefe

## Installation
```
git clone https://github.com/fwarren/xml2json.git
cd xml2json
python -m venv venv

source venv/bin/activate   # Linux
venv/bin/activate           # Windows

pip install -r requirements.txt
pyinstaller xml2json.spec
```
## Usage
Input from file
```
xml2json [-f/--format] [-o/--output <output-filename.json>] <input-filname.xml> 
```
