from btrfs_snapshots import make_snapshot
from fonts import install_fonts
import sys

snapshot = make_snapshot()

if not snapshot:
    sys.exit(1)

fonts = install_fonts()

if not fonts:
    sys.exit(1)

