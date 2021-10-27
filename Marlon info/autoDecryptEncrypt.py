"""
Na pasta packages do sublime:
Packages/autoDecryptEncrypt/autoDecryptEncrypt.py

salve esse arquivo
"""

import sublime, sublime_plugin

class EventListener( sublime_plugin.EventListener ):

    def on_load ( self, view ):

        fileExtension = view.window().extract_variables() [ "file_extension" ]
        if(fileExtension.find('__crypt')==-1):#Esse trecho é para encryptar somente os arquivos que contém CRYPT
            return
        encodingSets = \
            {
                "log"  : "Hexadecimal",
                "dump" : "Hexadecimal",
            }

        if fileExtension in encodingSets:
            encoding = encodingSets[ fileExtension ]
            view.run_command ( "reopen", { "encoding" : encoding } )