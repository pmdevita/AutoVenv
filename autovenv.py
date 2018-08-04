import os
import sys
from subprocess import Popen, PIPE


class Venv:
    def __init__(self, name, packages, folder=None):
        if folder is not None:  # Folder manually set
            self.venv_home = folder
        elif os.name == "nt":  # Default Windows
            self.venv_home = os.path.join(os.environ["APPDATA"], "VirtualEnvs")
        elif os.name == "posix":  # Default Linux/Mac/other Posix
            self.venv_home = os.path.join(os.environ["HOME"], ".venvs")
        else:
            raise Exception("Unsupported operating system")

        self.venv_path = os.path.join(self.venv_home, name)

        # Check if the virtualenv is already created/initialized and if not, initialize it
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

    def get_installed(self):
        # Get packages from pip
        p = Popen([os.path.join(self.scripts_path, "pip"), "list", "--format=columns"], stdout=PIPE)
        # Parse output lines
        output = p.communicate()[0].decode()
        pkg_lines = output.split('\r\n')[2:-1]
        # Split off whitespace
        pkgs = {}
        for i in pkg_lines:
            pkg = i.split()
            pkgs[pkg[0].lower()] = pkg[1]
        return pkgs

    def update(self, packages):
        # Get a list of the current environment's packages
        current_packages = self.get_installed()
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
    v = Venv("test1", ["requests", "pillow", "numpy"])
    print(v.get_installed())

