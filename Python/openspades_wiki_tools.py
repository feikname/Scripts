#
# openspades_wiki_tools.py - v0.0.0 (not a release!)
# MIT License
#

from __future__ import print_function

import os
import platform
import sys

"""
This function gathers all settings present in the OpenSpades user resource
directory configuration file (SPConfig.cfg) and generates a markdown string to
be used in the wiki.

If cfg_file=None, it searches automatically for the file.

See also: https://github.com/yvt/openspades/wiki/User-Resource-Directory
"""
def cfg_file_to_markdown(cfg_file=None):
    # List for storing the list of configurations
    cfg_list = []

    # List of config variables that should have an link added to them
    cfg_link_list = ["cg_Minimap_Player_Color"]

    # No configuration file given, use platform-specific default one
    if cfg_file == None:
        cfg_file = get_spconfig_path()

    # Open SPConfig.cfg in read-only mode
    sp_cfg = open(cfg_file, "r")

    # Parse each line
    for line in sp_cfg:
        _line = line.lstrip()
        if (_line.startswith("#")) or (_line.rstrip() == ""):
            continue

        key = _line.split(":", 1)[0] # Everything before the ":' character

        cfg_list.append(key)

    # Close the file
    sp_cfg.close()

    # Output the markdown list
    for cfg in cfg_list:
        cfg_md = ""

        if cfg in cfg_link_list:
            link = "#" + cfg.lower()
            cfg_md = " * [{0}]({1})".format(cfg, link)
        else:
            cfg_md = " * {0}".format(cfg)

        print(cfg_md)

def get_spconfig_path():
    # Windows Location: %APPDATA%\OpenSpades\Resources
    # Linux Location: $XDG_DATA_HOME/openspades/Resources
    # Darwin Location: ~/Library/Application Support/OpenSpades/Resources

    if platform.system() == "Windows":
        raise NotImplementedError("Windows not implemented yet")

        appdata = os.environ.get("APPDATA")
        if appdata == None:
            raise RuntimeError("%APPDATA% not defined! (wtf?)")

        cfg_file = os.path.join(appdata, "OpenSpades", "Resources",
                                "SPConfig.cfg")

        return cfg_file

    elif platform.system() == "Linux":
        xdg = os.environ.get("XDG_DATA_HOME")

        if xdg == None:
            # Default to $HOME/.local/share, as defined by the specs
            home = os.path.expanduser('~')
            xdg = os.path.join(home, ".local", "share")

        cfg_file = os.path.join(xdg, "openspades", "Resources",
                                "SPConfig.cfg")

        return cfg_file

    elif platform.system() == "Darwin":
        home = os.path.expanduser('~')

        cfg_file = os.path.join(home, "Library", "Application Support",
                                "OpenSpades", "Resources")

        return cfg_file

    else:
        return None;

# TODO: Colors
def display_help():
    help_text="""openspades_wiki_tool.py - v0.0.0 (not a release!)

Usage: python openspades_wiki_tools.py [action] [action_arguments]

Available actions:
  config_to_markdown [FILE]: Output the markdown index list of an SPConfig.cfg
      note: The [FILE] argument is optional.

It's recommended to redirect the output to a file (e.g. tools.py > output.md)
"""

    print(help_text)

NO_ARGUMENTS = (len(sys.argv) == 1) # First argument is the filename
INVALID_ACTION = True

try:
    INVALID_ACTION = (sys.argv[1] not in ["config_to_markdown"])
except IndexError:
    pass

if NO_ARGUMENTS:
    display_help()

elif INVALID_ACTION:
    print("Invalid action selected! Run this script with no arguments to see"\
          " the help text")

else:
    if sys.argv[1] == "config_to_markdown":
        if len(sys.argv) == 3:
            cfg_file_to_markdown(sys.argv[2])
        elif len(sys.argv) > 3:
            raise RuntimeError("Your provided more than 2 arguments to the"\
                               " config_to_markdown action!")
        else:
            cfg_file_to_markdown()
