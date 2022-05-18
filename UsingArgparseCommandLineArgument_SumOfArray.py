import argparse  
parser = argparse.ArgumentParser()

parser.add_argument("--elements",type=int ,nargs=3, help="Enter The Elements: ")
args = parser.parse_args()
sum=0

print(args.elements)
for i in range(0,3):
    a=args.elements
sum=0
for i in range(0,3):
    sum=sum+a[i]
print("Summations Of An Array Elements: ",sum)