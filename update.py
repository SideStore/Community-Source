import logging

from altparse import AltSourceManager, Parser, altsource_from_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

sourcesData = [
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://apps.altstore.io"},
        "ids": ["com.rileytestut.Delta", "com.rileytestut.Clip"],
        "getAllNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://alpha.altstore.io"},
        "ids": ["com.rileytestut.Delta.Alpha", "com.rileytestut.Clip.Beta"],
        "getAllNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://quarksources.github.io/quarksource.json"},
        "ids": ["com.libretro.RetroArchiOS11", "com.louisanslow.record", "org.scummvm.scummvm", "com.dry05.filzaescaped11-12", "com.virtualapplications.play"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://theodyssey.dev/altstore/odysseysource.json"},
        "ids": ["org.coolstar.odyssey"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "Odyssey-Team", "repo_name": "Taurine"},
        #"kwargs": {"filepath": "https://taurine.app/altstore/taurinestore.json"},
        "ids": ["org.coolstar.taurine"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "iNDS-Team", "repo_name": "iNDS"},
        "ids": ["net.nerd.iNDS"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "MAME4iOS"},
        "ids": ["com.example.mame4ios"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "nspire-emus", "repo_name": "firebird"},
        "ids": ["com.firebird.firebird-emu"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "Wh0ba", "repo_name": "XPatcher"},
        "ids": ["com.wh0ba.xpatcher"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "litchie", "repo_name": "dospad"},
        "ids": ["com.litchie.idosgames"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "QuarkSources", "repo_name": "ppsspp-builder"},
        "ids": ["org.ppsspp.ppsspp"]
    },
    {
        "parser": Parser.UNC0VER,
        "kwargs": {"url": "https://unc0ver.dev/releases.json"},
        "ids": ["science.xnu.undecimus"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "ianclawson", "repo_name": "Delta-iPac-Edition"},
        "ids": ["com.ianclawson.DeltaPacEdition"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios"},
        ## This is the previous kwargs required when this application was distributed as a zipped .ipa file ##
        ## "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios", "asset_regex": r".*\.ipa\.zip", "extract_twice": True, "upload_ipa_repo": g_release},
        "ids": ["net.namedfork.minivmac"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "T-Pau", "repo_name": "Ready", "ver_parse": lambda x: x.replace("release-", "")},
        "ids": ["at.spiderlab.c64"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "activegs-ios"},
        "ids": ["com.yoshisuga.activeGS"]
    },
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "zzanehip", "repo_name": "The-OldOS-Project"},
        "ids": ["com.zurac.OldOS"]
    }
]
alternateAppData = {
    #"eu.pokemmo.client": {
    #    "beta": False
    }
}

def header_remover(filename: str, header: str):
    with open(filename, 'r+') as f: 
        content = f.readlines()
        f.seek(0)
        f.writelines(content[header.count('\n')+1:])
        f.truncate()
        
def header_prepender(filename: str, header: str):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(header.rstrip('\r\n') + '\n' + content)
        f.truncate()

filename="sidecommunity.json"
header="""---
title: JSON Source
permalink: /
---"""

header_remover(filename,header)

src = altsource_from_file(filename)
mgr = AltSourceManager(src, sourcesData)
try:
    mgr.update()
    mgr.alter_app_info(alternateAppData)
    mgr.save(prettify=True)
    #mgr.save("sidecommunity.min.json",prettify=False) # use to save an additional copy of the json except minified
except Exception as err:
    logging.error(f"Unable to update {mgr.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
        
header_prepender(filename, header)
