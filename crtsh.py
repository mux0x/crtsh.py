import requests
import argparse
import sys
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", help="domain to get it's subs")
parser.add_argument("-o","--output",help="output file location")
args = parser.parse_args()

if isinstance(args.domain, str):
    domain = args.domain
else:
    print("you must provide a domain to recon on => python3 crtsh.py -d example.com")
    sys.exit(0)

if isinstance(args.output, str):
    outFile = args.output
else:
    print("you must provide a file name/path to print the results to => python3 crtsh.py -d example.com -o output.txt")

f = open(outFile, "a")
try:
    response = requests.get('https://crt.sh/?q=' + domain + '.com&output=json')
except Exception as e:
    print("ERROR OCCURED DURING REQUESTING " + e)
json = response.json()
subs = []
for show in json:
    lol = show['name_value'].split('\n')
    for x in lol:
        x = x.replace('*.','')
        if x not in subs:
            print("Found: " + x)
            subs.append(x)
            f.write(x + '\n')
f.close()
