import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dry-run', action='store_true')

args = parser.parse_args()

if args.dry_run:
    print("Dry run mode enabled")
else:
    print("Dry run mode disabled")
