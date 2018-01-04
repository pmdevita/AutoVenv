# AutoVenv



AutoVenv is a library for automatically configuring and using a virtual environment. 

AutoVenv automatically stores in:

* Windows - Roaming Appdata
* Linux/Mac  - $HOME/.config

I'm definitely looking for feedback on this. Given that it is pretty simple and there doesn't seem to be another
similar implementation, I'm guessing there may be some reason to not do this.

##### Install:
    python setup.py install

##### Usage:
    import autovenv
    v = autovenv.Venv("venv name", ["package 1", "package 2"], path="path/to/parent/folder")


##### Example:

    import autovenv
    v = autovenv.Venv("int-flask", ["pillow", "numpy"])
    
To do:
* Path validation
* Control package versions
* Test cases