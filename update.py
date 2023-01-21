import logging

from altparse import AltSourceManager, Parser, altsource_from_file

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

sourcesData = [
    {
        "parser": Parser.GITHUB,
        "kwargs": {"repo_author": "lonkelle", "repo_name": "Deltroid"},
        "ids": ["com.rileytestut.Deltroid"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://apps.altstore.io"},
        "ids": ["com.rileytestut.Delta"],
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
        "ids": ["com.louisanslow.record", "org.scummvm.scummvm"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://raw.githubusercontent.com/SideStore/Community-Source/main/staticApps/play.json"},
        "ids": ["com.virtualapplications.play"]
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://raw.githubusercontent.com/SideStore/Community-Source/main/staticApps/Retroarch.json"},
        "ids": ["com.libretro.RetroArchiOS11"]
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
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://gitlab.com/blurt/openblurt/blurt-mobile-app/-/raw/main/ios/app.json"},
        "ids": ["blog.blurt.blurt"],
        "getAllNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://github.com/spknetwork/Android-App/raw/development/ios/app.json"},
        "ids": ["com.example.acela"],
        "getAllNews": True
    },
    {
        "parser": Parser.ALTSOURCE,
        "kwargs": {"filepath": "https://raw.githubusercontent.com/vcmi/vcmi-updates/master/altstore/altstore.json"},
        "ids": ["com.vcmi.VCMI"],
        "getAllNews": True
    }    
]
alternateAppData = {

"com.firebird.firebird-emu": {
    "screenshotURLs": [
        "https://user-images.githubusercontent.com/64176728/211237020-f12974b6-5836-4bf1-a927-002f9e48a00f.png",
        "https://user-images.githubusercontent.com/64176728/211237030-6c613bae-3a5e-4826-9fd6-20dfa628bd4a.png",
        "https://user-images.githubusercontent.com/64176728/211237032-e8a72501-9c94-4d5f-b50c-ea65ef84c361.png"
    ]
},
"net.namedfork.minivmac": {
    "screenshotURLs": [
        "https://user-images.githubusercontent.com/64176728/211237407-e79d6562-c6c2-4a69-b8ea-4414e6b97be0.png",
        "https://user-images.githubusercontent.com/64176728/211237433-ca07c970-747e-4fd1-a206-be07384183cb.png",
        "https://user-images.githubusercontent.com/64176728/211237435-27c3a84c-7213-4a55-b4d9-b7a9362ffb36.png"
        ]
}

    #"eu.pokemmo.client": {
    #    "beta": False
    #}

    #"com.virtualapplications.play": {
    #    "screenshotURLs": [
    #         "https://user-images.githubusercontent.com/64176728/209461585-74b856e0-ae30-41be-91ce-d3eb262be260.png",
    #         "https://user-images.githubusercontent.com/64176728/209461763-c122f9f6-5103-4c59-b730-0e5b34b5937b.png",
    #         "https://user-images.githubusercontent.com/64176728/209461593-f771a49d-a44d-4d9c-8bb7-dfab48c5dd25.png"
    #    ]
    #}
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

src = altsource_from_file("sidecommunity.json")
mgr = AltSourceManager(src, sourcesData)
try:
    mgr.update()
    mgr.alter_app_info(alternateAppData)
    mgr.save(prettify=True)
    #mgr.save("sidecommunity.min.json",prettify=False) # use to save an additional copy of the json except minified
except Exception as err:
    logging.error(f"Unable to update {mgr.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
        
