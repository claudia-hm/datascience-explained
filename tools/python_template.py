" Basic python template"

#imports
import argparse, warnings, os, multiprocessing

def parse_arguments():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('data', help="Data file")
    parser.add_argument('-mp', "--multiproc", action='store_true', help='Compute something in parallel')

    args = parser.parse_args()
    return args

def main():
   print("Alohomora!\U0001F4AB")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    args = parse_arguments()
    main()
