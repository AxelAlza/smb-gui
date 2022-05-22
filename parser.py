import configparser
import os


class Parser:
    path = 'C:\\Users\\Axel Alza\\Desktop\\parser\\smb.conf'
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

    def GetShares(self):
        shares = filter(lambda s: s not in ['global', 'homes', 'printers'], self.config.sections())
        sharesinfo = {}
        for share in list(shares):
            sharesinfo[share] = self.config[share]['path']

        return sharesinfo
