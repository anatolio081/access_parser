import argparse
import os
import sys
import re
import json

arg_parser = argparse.ArgumentParser(description="access.log parser")
file_name_arg = arg_parser.add_argument('-f', '--file', dest="filename", help="enter path to file", metavar="FILE")
file_dir_arg = arg_parser.add_argument('-d', '--directory', dest="directory", help="enter path to files", metavar="DIR")
output={}

args = arg_parser.parse_args()
file_name = args.filename
#file_dir = args.directory
file_dir = "acc_dir"
if not file_name == None:
    file_path = file_name
elif not file_dir == None:
    pass
else:
    print("Error!!! file/directory is not found")
    sys.exit()


files = os.listdir(file_dir)
for name in files:
    print(name)

# with open(file_path) as file:
#     a = 0
#     for line in file:
#         print(str(a))
#         a += 1




# with open(file_path) as file:
#     requests = re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", file.read())
#     output["count_all_requests"] = requests.__len__()
#     output["count_requests_by_method"] = {
#         "GET": requests.count("GET"),
#         "POST": requests.count("POST"),
#         "PUT": requests.count("PUT"),
#         "DELETE": requests.count("DELETE"),
#         "HEAD": requests.count("HEAD")
#     }

#
# with open(file_path) as file:
#     ip_count = {}
#     ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file.read())
#     for i in ip:
#         if i in ip_count.keys():
#             ip_count[i] += 1
#         else:
#             ip_count[i] = 0
#     list_d = list(ip_count.items())
#     list_d.sort(key=lambda i: i[1])
#     list_d.reverse()
#     top_ip={}
#     for l in range(0, 10):
#          top_ip[list_d[l][0]] = list_d[l][1]
#     output["top_request_by_ip"] = top_ip
#
#
#
#
# db_dict = {}
# id = []
# method = []
# url = []
# ip = []
# code_cl_error = []
# with open(file_path) as file:
#     for line in file:
#         code = re.findall(r"\s4\d{2}\s", line)
#         if not code == []:
#             method.append(re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line))
#             url.append(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line))
#             ip.append(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))
#             code_cl_error.append(code)
# try:
#     for i in range(0, 10):
#         db_dict[i] = {
#             "ip": ip[i][0],
#             "url": url[i],
#             "method": method[i][0],
#             "code": code_cl_error[i][0]
#         }
# except IndexError:
#     pass
# output["client_error_top"] = db_dict
#
#
#
# db_dict = {}
# id = []
# method = []
# url = []
# ip = []
# code_cl_error = []
# with open(file_path) as file:
#     for line in file:
#         code = re.findall(r"\s5\d{2}\s", line)
#         if not code == []:
#             method.append(re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line))
#             url.append(re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", line))
#             ip.append(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))
#             code_cl_error.append(code)
# try:
#     for i in range(0, 10):
#         db_dict[i] = {
#             "ip": ip[i][0],
#             "url": url[i],
#             "method": method[i][0],
#             "code": code_cl_error[i][0]
#         }
# except IndexError:
#     pass
# output["server_error_top"] = db_dict
#
# with open('output.txt', 'w') as outfile:
#     json.dump(output, outfile)