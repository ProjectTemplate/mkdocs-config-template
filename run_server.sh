#!/usr/bin/bash

# 绑定的 IP
host="127.0.0.1"
# 绑定的端口
port=34251
# 校验key
auth_key="72e0013883cbc8333575c250bc0d14cd"

nohup python ./server.py ${host} ${port} > rebuild.log &