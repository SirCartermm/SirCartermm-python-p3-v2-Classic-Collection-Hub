import argparse
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

def create_supercar():
    # ...

def get_supercars():
    # ...

def vote_supercar():
    # ...

def comment_supercar():
    # ...

def main():
    parser = argparse.ArgumentParser(description='Classic Collection Hub CLI')
    parser.add_argument('action', type=str, help='Action to perform (create_supercar, get_supercars, vote_supercar, comment_supercar)')
    args = parser.parse_args()

    if args.action == 'create_supercar':
        create_supercar()
    elif args.action == 'get_supercars':
        get_supercars()
    elif args.action == 'vote_supercar':
        vote_supercar()
    elif args.action == 'comment_supercar':
        comment_supercar()
    else:
        print('Invalid action')

if __name__ == '__main__':
    main()