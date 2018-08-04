# AutoVenv

AutoVenv is a library for automatically setting up and configuring a virtual environment from within an application. 

AutoVenv automatically stores in:

* Windows - Roaming Appdata
* Linux/Mac  - $HOME/.config

I wrote this because I didn't know about pipenv. It's much simpler than pipenv though so I think it still might 
be useful.

##### Install:
    python setup.py install

##### Usage:
    import autovenv
    v = autovenv.Venv("venv name", ["package 1", "package 2"], path="path/to/parent/folder")


##### Example:

    import autovenv
    v = autovenv.Venv("my_venv", ["pillow", "numpy"])
    
To do:
* Path validation
* Control package versions
* Test cases