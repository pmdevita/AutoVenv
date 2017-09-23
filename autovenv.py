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
            self.scripts_path = os.path.join(self.venv_path, "Scripts")
            # print(activate_this)
        else:
            self.scripts_path = os.path.join(self.venv_path, "bin")

        # Switch the interpreter to the virtualenv
        try:
            exec(open(os.path.join(self.scripts_path, "activate_this.py")).read(), dict(__file__=os.path.join(self.scripts_path, "activate_this.py")))
        except FileNotFoundError:
            # There is some problem with the virtualenv. Let's rebuild it
            print("Virtualenv broken. Recreating...")
            import shutil
            shutil.rmtree(self.venv_path)
            p = Popen([sys.executable, "-m", "virtualenv", self.venv_path])
            p.wait()

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
                if not i[0].lower() in current_packages.keys():
                    packages_to_install.append(i[0])
            else:
                if i.lower() not in current_packages.keys():
                    packages_to_install.append(i)

        # Install the missing packages
        if packages_to_install:
            p = Popen([os.path.join(self.scripts_path, "pip"), "install"] + packages_to_install)
            p.wait()


if __name__ == "__main__":
    # Testcases (Make more)
    print("Running testcases")
    Venv("test", ["pillow"])
