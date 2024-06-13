import argparse
import sys
import os

# Add the parent directory of cli to the Python path
sys.path.insert(0, os.path.dirname(__file__))

from .cli import create_supercar, get_supercars, vote_supercar, comment_supercar

def main():
    parser = argparse.ArgumentParser(description='Classic Collection Hub CLI')
    parser.add_argument('action', type=str, help='Action to perform (create_supercar, get_supercars, vote_supercar, comment_supercar)')
    args = parser.parse_args()

    if args.action == 'create_supercar':
        parser.add_argument('--name', type=str, help='Supercar name')
        parser.add_argument('--description', type=str, help='Supercar description')
        args = parser.parse_args()
        create_supercar(args.name, args.description)
    elif args.action == 'get_supercars':
        get_supercars()
    elif args.action == 'vote_supercar':
        parser.add_argument('--supercar_id', type=int, help='Supercar ID')
        parser.add_argument('--vote_type', type=str, help='Vote type (like/dislike)')
        args = parser.parse_args()
        vote_supercar(args.supercar_id, args.vote_type)
    elif args.action == 'comment_supercar':
        parser.add_argument('--supercar_id', type=int, help='Supercar ID')
        parser.add_argument('--comment_text', type=str, help='Comment text')
        args = parser.parse_args()
        comment_supercar(args.supercar_id, args.comment_text)
    else:
        print("Invalid action")

if __name__ == '__main__':
    main()