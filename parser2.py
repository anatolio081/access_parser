import argparse
import re
import json

arg_parser = argparse.ArgumentParser(description="access.log parser")
file_name = arg_parser.add_argument('-f', '--file', dest="filename", help="enter path to file", metavar="FILE")
args = arg_parser.parse_args()
file_path = args.filename
dict_ip = {}

with open(file_path) as file:
    for index, line in enumerate(file.readlines()):
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
        method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
        if dict_ip.get(ip, None) is None:
            dict_ip[ip] = {
                "GET": 0,
                "POST": 0,
                "PUT": 0,
                "DELETE": 0,
                "HEAD": 0,
            }
        dict_ip[ip][method] += 1
print(json.dumps(dict_ip, indent=4))
with open('output.txt','w') as f:
    json.dump(dict_ip, f)
