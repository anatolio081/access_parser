import argparse
import re
import json

# arg_parser = argparse.ArgumentParser(description="access.log parser")
# file_name = arg_parser.add_argument('-f', '--file', dest="filename", help="enter path to file", metavar="FILE")
# args = arg_parser.parse_args()
# file_path = args.filename
# dict_ip = {}
output = {}
file_path = "access.log"

with open(file_path) as file:
    requests = re.findall(r"\] \"(POST|GET|PUT|DELETE|HEAD)", file.read())
    output["count_all_requests"] = requests.__len__()
    output["count_requests_by_method"] = {
        "GET": requests.count("GET"),
        "POST": requests.count("POST"),
        "PUT": requests.count("PUT"),
        "DELETE": requests.count("DELETE"),
        "HEAD": requests.count("HEAD")
    }

with open(file_path) as file:
    ip_count = {}
    ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", file.read())
    for i in ip:
        if i in ip_count.keys():
            ip_count[i] += 1
        else:
            ip_count[i] = 0
    list_d = list(ip_count.items())
    list_d.sort(key=lambda i: i[1])
    list_d.reverse()
    top_ip={}
    for l in range(0, 10):
         top_ip[list_d[l][0]] = list_d[l][1]
    output["top_request_by_ip"] = top_ip

print(json.dumps(output))

# print(req)
# print("POST=" + str(POST_ct))
# print("GET=" + str(GET_ct))
# print("PUT=" + str(PUT_ct))
# print("DELETE=" + str(DELETE_ct))
# print("HEAD=" + str(HEAD_ct))

# with open(file_path) as file:
#     for index, line in enumerate(file.readlines()):
#         ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
#         method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()
#         ip_req[index] = {ip: method}
#     for i in range(0, ct_reqests):
#         print(ip_req[i])
# for index, line in enumerate(file.readlines()):
#     ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group()
#     method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
#     if dict_ip.get(ip, None) is None:
#         dict_ip[ip] = {
#             "GET": 0,
#             "POST": 0,
#             "PUT": 0,
#             "DELETE": 0,
#             "HEAD": 0,
#         }
#     dict_ip[ip][method] += 1
# print(json.dumps(dict_ip, indent=4))
# with open('output.txt','w') as f:
#     json.dump(dict_ip, f)
