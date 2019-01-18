import sys, os, argparse
#sys.path.insert(0, r'../post_processing/')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from evaluation import evaluate, get_evaluation_parser
from post_processing.utils import generate_heads

def wrapper(args):
    heads = generate_heads(int(args.heads))
    for i in range(int(args.layers)):
        for head in heads:
            file_name = "layer" + str(i+1) + "_" + head + "_" + args.suffix
            args.segmentation = file_name
            args.output = file_name.replace(args.suffix, "eval")
            evaluate(args)



if __name__ == "__main__":
    parser = get_evaluation_parser(argparse.ArgumentParser())
    parser.add_argument('--suffix', type=str, nargs='?', help='suffix of the segmentation')
    parser.add_argument('--heads', type=str, nargs='?', help='number of heads')
    parser.add_argument('--layers', type=str, nargs='?', help='number of layers')
    args = parser.parse_args()
    if not (args.heads and args.layers):
        parser.print_help()
        sys.exit(1)
    wrapper(args)