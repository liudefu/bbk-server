# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~

    Config file for the spider module.

    :copyright: (c) 2017-18 by Wendell Hu.
    :license: MIT, see LICENSE for more details.
"""

#: Start points for spiders
#: Also in `IgnoreDuplicatedRequestMiddleware` scrapy would check if the
#: current request is in this list. if true, it wouldn't ignore it cuz we
#: cannot jump over the homepages!
START_POINTS = {
    'sina': 'http://sina.com.cn/',
    'chinadaily': 'http://cn.chinadaily.com.cn/',
    'people': 'http://www.people.com.cn/',
    'ifeng': 'http://www.ifeng.com/',
    'cctv': 'http://www.cctv.com/',
}

PREVENTS = START_POINTS.values()

#: Database
SPIDER_DATABASE_URI = 'mysql://root:sige1995@localhost:3306/bbk-spider'
SPIDER_REDIS_CONFIG = {
    'host': 'localhost',
    'port': 6379,
}
