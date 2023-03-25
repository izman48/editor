# Editor.py
Python script to trim video. 

## Build
Build using:

```
python -m build
```

## Add to path

```
pip install dist/editor-0.1.0-py3-none-any.whl
```

## Usage
```
Usage: editor [OPTIONS] NAME
--start                           INTEGER  [default: None]
--end                             INTEGER  [default: None] 
--result-name                     TEXT     [default: output.mp4]  
--fps                             INTEGER  [default: 25]    
--compress       --no-compress             [default: compress]  
--help                                     Show this message and exit. 
```