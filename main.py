import argparse
import os

DOCUPATH = '/Docu/'
def parse_args():
    parser=argparse.ArgumentParser(description="a script to do stuff")
    parser.add_argument("--source", type=str, required=True)
    args=parser.parse_args()
    return args


def main():
    print("this is the main function")
    args = parse_args()
    cwd = os.getcwd() 
    print(args.source)
    print(cwd)
    print(f'{os.getcwd()}'.join(DOCUPATH))
    pass

if __name__ == "__main__":
    main()
