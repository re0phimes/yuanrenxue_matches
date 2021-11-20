# -*- ecoding: utf-8 -*-
# @ModuleName: q1
# @Function: 
# @Author: ctx_phi
# @Craete Time: 2021/11/17 16:10


import requests
from loguru import logger
import time
import base64
import hashlib


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
    'cookie' : "sessionid=q9muqgtlaq43xxgf9c7y48slxs40bvm5"
}

url = 'https://www.python-spider.com/challenge/1'
preurl = 'http://www.python-spider.com/cityjson'
json_api = "https://www.python-spider.com/challenge/api/json?page={}&count=14"



def downloader():
    '''
    获取页面信息
    :return:
    '''
    # raw_data_list = []
    # s = requests.session()
    # # s.post('https://www.python-spider.com/challenge/login', )
    # cityinfo = s.post(preurl, data=False)
    # logger.info(cityinfo.text)
    # ts = int(time.time())
    # a = '9622'
    # m = (a + str(ts)).encode()
    # tmp_toekn = base64.b64encode(m)
    # logger.debug(tmp_toekn)
    # md5 = hashlib.md5()
    # md5.update(tmp_toekn)
    # tokens = md5.hexdigest()
    # logger.debug(tokens)
    # headers['timestamp'] = str(ts)
    # headers['safe'] = tokens
    # logger.info(headers)
    s = requests.session()
    raw_data_list = []
    for i in range(1,86):

        # s.post('https://www.python-spider.com/challenge/login', )
        cityinfo = s.post(preurl, data=False)
        logger.info(cityinfo.text)
        ts = int(time.time())
        a = '9622'
        m = (a + str(ts)).encode()
        tmp_toekn = base64.b64encode(m)
        logger.debug(tmp_toekn)
        md5 = hashlib.md5()
        md5.update(tmp_toekn)
        tokens = md5.hexdigest()
        logger.debug(tokens)
        headers['timestamp'] = str(ts)
        headers['safe'] = tokens
        logger.info(headers)
        r = s.get(json_api.format(i), headers=headers)
        if r.status_code != 500:
            logger.info(r.status_code)
            logger.debug(r.json())
            msg_list = [dict_info['message'] for dict_info in r.json()['infos']]
            raw_data_list += msg_list
            logger.info('current page:{}, data length: {}'.format(i, len(raw_data_list)))
        else:
            logger.warning('update header')
    return raw_data_list

# --------------------------------------------------------------------------------
count = 0
def parse_include(data_list):
    '''
    是否包含招字
    :param data_list:
    :return:
    '''
    global count
    for sentence in data_list:
        if '招' in sentence:
            count += 1
    logger.info('当前count为：{}'.format(count))




data_list = downloader()
parse_include(data_list)

