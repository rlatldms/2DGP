#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by: python.exe -m py2exe mygame.py -O -W setup.py


import platform
import os
from distutils.core import setup
import py2exe

class Target(object):
    '''Target is the baseclass for all executables that are created.
    It defines properties that are shared by all of them.
    '''
    def __init__(self, **kw):
        self.__dict__.update(kw)

        # the VersionInfo resource, uncomment and fill in those items
        # that make sense:
        
        # The 'version' attribute MUST be defined, otherwise no versioninfo will be built:
        # self.version = "1.0"
        
        # self.company_name = "Company Name"
        # self.copyright = "Copyright Company Name © 2013"
        # self.legal_copyright = "Copyright Company Name © 2013"
        # self.legal_trademark = ""
        # self.product_version = "1.0.0.0"
        # self.product_name = "Product Name"

        # self.private_build = "foo"
        # self.special_build = "bar"

    def copy(self):
        return Target(**self.__dict__)

    def __setitem__(self, name, value):
        self.__dict__[name] = value

RT_BITMAP = 2
RT_MANIFEST = 24

# A manifest which specifies the executionlevel
# and windows common-controls library version 6

manifest_template = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="*"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="%(level)s"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
'''



mygame = Target(
    script = "Clicker_Wars.py",
    dest_base = "ClickerWars",
    icon_resources = [(1, r"pico2d.ico")],
    other_resources = [(RT_MANIFEST, 1, (manifest_template % dict(prog="mygame", level="asInvoker")).encode("utf-8"))]
    )

py2exe_options = dict(
    packages = [],
    optimize=1,
    compressed=True, # uncompressed may or may not have a faster startup
    bundle_files=2,
    dist_dir='dist',
    )


resources = "location/location_1.jpg \
            location/location_2.jpg \
            location/location_3.jpg \
            location/location_4.jpg \
            location/location_5.jpg \
            location/location_6.jpg \
            location/location_7.jpg \
            location/location_8.jpg \
            location/location_9.jpg \
            location/location_10.jpg \
            title&menu/end.png \
            monsters/monsters1.png \
            monsters/monsters3.png \
            monsters/monsters5.png \
            monsters/monsters7.png \
            monsters/monsters9.png \
            monsters/monsters11.png \
            monsters/monsters13.png \
            monsters/monsters15.png \
            monsters/monsters17.png \
            monsters/monsters19.png \
            monsters/monsters49.png \
            title&menu/main6.png \
            sound&font/my_font.ttf \
            sound&font/new_level.mp3 \
            sound&font/monster_die_01.mp3 \
            sound&font/hit_monster_2.mp3 \
            sound&font/upgrade_hero.mp3 \
            sound&font/take_coin.mp3 \
            sound&font/Coin_down.mp3".split()

if platform.architecture()[0] == '32bit':
    sdl_folder = './SDL2/x86/'
else:
    sdl_folder = './SDL2/x64/'

sdl_dlls = [sdl_folder + file_name for file_name in os.listdir(sdl_folder)]


setup(name="name",
      windows=[mygame],
      data_files=[('.', resources), (sdl_folder, sdl_dlls)], # copy resource to '.' folder
      zipfile=None,
      options={"py2exe": py2exe_options},
      )

