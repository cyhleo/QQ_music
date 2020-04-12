# -*- coding: utf-8 -*-

from fake_useragent import UserAgent
import logging

logger = logging.getLogger(__name__)

class RandomUserAgentDownloaderMiddleware(object):
    def process_request(self, request, spider):
        agent = UserAgent()
        agent_random = agent.random
        request.headers['User-Agent'] = agent_random
        logger.debug('正在使用的User-Agent：{}'.format(agent_random))
        return None


