import configparser
import subprocess


class Parser:
    path = '/etc/samba/smb.conf'
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read(self.path)

    def ConfigShare(self, nombre, ruta, writable, browseable):
        if not self.config.has_section(nombre): self.config.add_section(nombre)
        bools = {True: "yes", False: 'no'}
        self.config.set(nombre, 'path', ruta)
        self.config.set(nombre, 'public', 'yes')
        self.config.set(nombre, 'writable', bools[writable])
        self.config.set(nombre, 'browseable', bools[browseable])
        with open(self.path, 'w') as file:
            self.config.write(file)

    def EliminarShare(self, nombre):
        self.config.remove_section(nombre)
        with open(self.path, 'w') as file:
            self.config.write(file)

    def GetUsers(self):
        users = []
        result = subprocess.check_output("pdbedit -L | awk -F: 'NF>=3'", shell=True)
        output = result.decode("utf-8")
        for i in output.splitlines():
            users.append(i.split(':')[0])
        return users

    def GetShares(self):
        filtro = ['global', 'homes', 'printers', 'netlogon', 'profiles', 'pdf-documents', 'pdf-printer']
        shares = filter(lambda s: s not in filtro, self.config.sections())
        sharesinfo = {}
        for share in list(shares):
            sharesinfo[share] = self.config[share]['path']

        return sharesinfo
