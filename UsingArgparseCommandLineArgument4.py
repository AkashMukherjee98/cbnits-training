import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, help="first")
parser.add_argument("--num2", type=int, help="second")

args = parser.parse_args()

n1=int(args.num)
n2=int(args.num2)
result = None
result=n1+n2
print("Result:",result)