from btrfs_snapshots import make_snapshot
import sys

snapshot = make_snapshot()

if not snapshot:
    sys.exit(1);



