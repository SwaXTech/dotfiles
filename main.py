from btrfs_snapshots import make_snapshot
from fonts import install_fonts
from fish import install_fish, install_fisher, install_fish_plugins
import sys

snapshot = make_snapshot()

if not snapshot:
    sys.exit(1)

fonts = install_fonts()

if not fonts:
    sys.exit(1)


fish = install_fish()

if not fish:
    sys.exit(1)

fisher = install_fisher()

if not fisher:
    sys.exit(1)

fish_plugins = install_fish_plugins()

if not fish_plugins:
    sys.exit(1)


