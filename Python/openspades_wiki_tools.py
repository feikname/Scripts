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
    # no configuration file given, use platform-specific default one
    if cfg_file == None:
        cfg_file = get_spconfig_path()

    print(("Parsing %s " % cfg_file))

def get_spconfig_path():
    # Windows Location: %APPDATA%\OpenSpades\Resources
    # Linux Location: $XDG_DATA_HOME/openspades/Resources
    # Darwin Location: ~/Library/Application Support/OpenSpades/Resources

    if platform.system() == "Windows":
        raise NotImplementedError("Windows not implemented yet")

        appdata = os.environ.get("APPDATA")
        if appdata == None:
            raise RuntimeError("%APPDATA% not defined! (wtf?)")

        cfg_file = os.path.join([appdata, "OpenSpades", "Resources",
                                 "SPConfig.cfg"])

        return cfg_file

    elif platform.system() == "Linux":
        xdg = os.environ.get("XDG_DATA_HOME")

        if xdg == None:
            # Default to $HOME/.local/share, as defined by the specs
            home = os.path.expanduser('~')
            xdg = os.path.join([home, ".local", "share"])

        cfg_file = os.path.join([xdg, "openspades", "Resources",
                                 "SPConfig.cfg"])

        return cfg_file

    elif platform.system() == "Darwin":
        raise NotImplementedError("Darwin not implemented yet")

    else:
        return None;

# TODO: Colors
def display_help():
    help_text="""openspades_wiki_tool.py - v0.0.0 (not a release!)

Usage: python openspades_wiki_tools.py [action] [action_arguments]

Available actions:
  config_to_markdown [FILE]: Output the markdown index list of an SPConfig.cfg
      note: The [FILE] argument is optional.


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
        else:
            cfg_file_to_markdown()
