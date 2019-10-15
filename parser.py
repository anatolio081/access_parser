import argparse
import os
import sys
import re
import json

arg_parser = argparse.ArgumentParser(description="access.log parser")
file_name_arg = arg_parser.add_argument('-f', '--file', dest="filename", help="enter path to file", metavar="FILE")
file_dir_arg = arg_parser.add_argument('-d', '--directory', dest="directory", help="enter path to files", metavar="DIR")
file_dir_arg = arg_parser.add_argument('-o', '--output', dest="output_name", help="enter name of output file",
                                       metavar="OUTP")

output = {}
raw = ""
raw_lines = ""
args = arg_parser.parse_args()
file_name = args.filename
file_dir = args.directory
output_name = args.output_name
# file_name = 'access.log'
# file_dir = 'acc_dir'
if not file_name == None:
    with open(file_name) as file:
        raw = file.read()
    with open(file_name) as file:
        raw_lines = file.readlines()
elif not file_dir == None:
    raw = ""
    files = os.listdir(file_dir)
    for name in files:
        with open(file_dir + "/" + name) as file:
            raw += file.read()
        with open(file_dir + "/" + name) as file:
            raw_lines += str(file.readlines())
else:
    print("Error!!! file/directory is not found")
    sys.exit()

if output_name == None:
    output_name = "output.txt"



cnt = 0
rs = {}
requests = re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", raw)
output["count_all_requests"] = requests.__len__()
rs = {
    "GET": requests.count("GET"),
    "POST": requests.count("POST"),
    "PUT": requests.count("PUT"),
    "DELETE": requests.count("DELETE"),
    "HEAD": requests.count("HEAD")
}

ip_count = {}
ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", raw)
for i in ip:
    if i in ip_count.keys():
        ip_count[i] += 1
    else:
        ip_count[i] = 0
list_d = list(ip_count.items())
list_d.sort(key=lambda i: i[1])
list_d.reverse()
top_ip = {}
for l in range(0, 10):
    top_ip[list_d[l][0]] = list_d[l][1]
output["top_request_by_ip"] = top_ip

db_dict = {}
id = []
method = []
url = []
ip = []
code_cl_error = []
for line in raw_lines:
    code = re.findall(r"\s4\d{2}\s", line)
    if not code == []:
        method.append(re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line))
        url.append(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line))
        ip.append(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))
        code_cl_error.append(code)
try:
    for i in range(0, 10):
        db_dict[i] = {
            "ip": ip[i][0],
            "url": url[i],
            "method": method[i][0],
            "code": code_cl_error[i][0]
        }
except IndexError:
    pass
output["client_error_top"] = db_dict

db_dict = {}
id = []
method = []
url = []
ip = []
code_cl_error = []
for line in raw_lines:
    code = re.findall(r"\s5\d{2}\s", line)
    if not code == []:
        method.append(re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line))
        url.append(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line))
        ip.append(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))
        code_cl_error.append(code)
try:
    for i in range(0, 10):
        db_dict[i] = {
            "ip": ip[i][0],
            "url": url[i],
            "method": method[i][0],
            "code": code_cl_error[i][0]
        }
except IndexError:
    pass
output["server_error_top"] = db_dict

with open(output_name, 'w') as outfile:
    json.dump(output, outfile)
