# AutoVenv

<a target='_blank' rel='nofollow' href='https://app.codesponsor.io/link/mAAoQtNM9wiSavibTmZvvG8g/pmdevita/AutoVenv'>
  <img alt='Sponsor' width='888' height='68' src='https://app.codesponsor.io/embed/mAAoQtNM9wiSavibTmZvvG8g/pmdevita/AutoVenv.svg' />
</a>

AutoVenv is a library for automatically configuring and using a virtual environment. 

AutoVenv automatically stores in

* Windows - Roaming Appdata
* Linux/Mac  - $HOME/.config

I'm definitely looking for feedback on this. Given that it is pretty simple and there doesn't seem to be another
similar implementation, I'm guessing there may be some reason to not do this.

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