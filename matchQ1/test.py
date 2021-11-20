# -*- ecoding: utf-8 -*-
# @ModuleName: test
# @Function: 
# @Author: ctx_phi
# @Craete Time: 2021/11/18 17:42


import requests
from loguru import logger

url = 'https://match.yuanrenxue.com/api/match/1?m=7d492fc0c9cf269f86383764490cf0e3%E4%B8%A81637329132'


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
    'cookie' : "sessionid=3yx145n2fv89nfwk4wend7w5j5uyvf9x"
}


s = requests.session()

r = s.get(url, headers=headers)
logger.info(r.text)