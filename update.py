import logging
import os

from ipaUtil import get_github_release
from sourceUtil import (AltSourceManager, AltSourceParser, GithubParser,
                        Unc0verParser)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# try:
#     g_token = os.environ["GITHUB_TOKEN"]
#     g_release = get_github_release(g_token, 321891219) # gets the github release by its API id
# except KeyError as err:
#     logging.error(f"Could not find GitHub Token.")
#     logging.error(f"{type(err).__name__}: {str(err)}")

sourcesData = [
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "quarksource.json"},
        "ids": ["com.libretro.RetroArchiOS11", "com.louisanslow.record", "org.scummvm.scummvm", "com.dry05.filzaescaped11-12", "com.virtualapplications.play"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://theodyssey.dev/altstore/odysseysource.json"},
        "ids": ["org.coolstar.odyssey"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "Odyssey-Team", "repo_name": "Taurine"},
        #"kwargs": {"filepath": "https://taurine.app/altstore/taurinestore.json"},
        "ids": ["org.coolstar.taurine"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "iNDS-Team", "repo_name": "iNDS"},
        "ids": ["net.nerd.iNDS"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "MAME4iOS"},
        "ids": ["com.example.mame4ios"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "brandonplank", "repo_name": "flappybird"},
        "ids": ["org.brandonplank.flappybird"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "nspire-emus", "repo_name": "firebird"},
        "ids": ["com.firebird.firebird-emu"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "Wh0ba", "repo_name": "XPatcher"},
        "ids": ["com.wh0ba.xpatcher"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "litchie", "repo_name": "dospad"},
        "ids": ["com.litchie.idosgames"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "QuarkSources", "repo_name": "ppsspp-builder"},
        "ids": ["org.ppsspp.ppsspp"]
    },
    {
        "parser": Unc0verParser,
        "kwargs": {"url": "https://unc0ver.dev/releases.json"},
        "ids": ["science.xnu.undecimus"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "ianclawson", "repo_name": "Delta-iPac-Edition"},
        "ids": ["com.ianclawson.DeltaPacEdition"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios"},
        ## This is the previous kwargs required when this application was distributed as a zipped .ipa file ##
        ## "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios", "asset_regex": r".*\.ipa\.zip", "extract_twice": True, "upload_ipa_repo": g_release},
        "ids": ["net.namedfork.minivmac"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "T-Pau", "repo_name": "Ready", "ver_parse": lambda x: x.replace("release-", "")},
        "ids": ["at.spiderlab.c64"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "activegs-ios"},
        "ids": ["com.yoshisuga.activeGS"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "zzanehip", "repo_name": "The-OldOS-Project"},
        "ids": ["com.zurac.OldOS"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://pokemmo.eu/altstore/"},
        "ids": ["eu.pokemmo.client"]
    }
]
alternateAppData = {
    "eu.pokemmo.client": {
        "beta": False
    },
    "org.ppsspp.ppsspp": {
        "tintColor": "#21486b",
        "subtitle": "PlayStation Portable games on iOS.",
        "screenshotURLs": [
            "https://i.imgur.com/CWl6GgH.png",
            "https://i.imgur.com/SxmN1M0.png",
            "https://i.imgur.com/sGWgR6z.png",
            "https://i.imgur.com/AFKTdmZ.png"
        ],
        "iconURL": "https://i.imgur.com/JP0Fncv.png"
    }
}

quantumsrc = AltSourceManager("sidecommunity.json", sourcesData, alternateAppData, prettify=True) # if prettify is true, output will have indents and newlines
try:
    quantumsrc.update()
except Exception as err:
    logging.error(f"Unable to update {quantumsrc.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
