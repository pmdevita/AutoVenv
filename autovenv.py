import os
import sys
from importlib.util import find_spec
from subprocess import Popen


class Venv:
    def __init__(self, name, packages, folder=None):
        if folder is not None:  # Folder manually set
            self.venv_home = folder
        elif os.name == "nt":  # Default Windows
            self.venv_home = os.path.join(os.environ["APPDATA"], "VirtualEnvs")
        elif os.name == "posix":  # Default Linux/Mac/other Posix
            self.venv_home = os.path.join(os.environ["HOME"], ".venvs")

        self.venv_path = os.path.join(self.venv_home, name)

        # Check if the virtualenv is already initialized and if not, initialize it
        if not os.path.isdir(self.venv_path):
            p = Popen([sys.executable, "-m", "virtualenv", self.venv_path])
            p.wait()

        # Windows stores the Python binary differently
        if os.name == "nt":
            activate_this = os.path.join(self.venv_path, "Scripts/activate_this.py")
            # print(activate_this)
        else:
            activate_this = os.path.join(self.venv_path, "bin/activate_this.py")

        # Switch the interpreter to the virtualenv
        exec(open(activate_this).read(), dict(__file__=activate_this))

        # Update the environment's packages
        self.update(packages)

    def update(self, packages):
        import pip

        # Get a list of the current environment's packages
        current_packages = {x.key: x.version for x in pip.get_installed_distributions()}
        packages_to_install = []

        # Check if each of requested packages is already installed
        for i in packages:
            if type(i) == list:
                if not i[0] in current_packages.keys():
                    packages_to_install.append(i[0])
            else:
                if i not in current_packages.keys():
                    packages_to_install.append(i)

        # Install the missing packages
        print(packages_to_install)
        if packages_to_install:
            pip.main(["install"] + packages_to_install)


if __name__ == "__main__":
    # Testcases (Make more)
    print("Running testcases")
    Venv("test", ["pillow"])
