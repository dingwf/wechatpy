from __future__ import absolute_import, unicode_literals

import logging

from wechatx.client import WeChatClient  # NOQA
from wechatx.component import ComponentOAuth, WeChatComponent  # NOQA
from wechatx.exceptions import WeChatClientException, WeChatException, WeChatOAuthException, WeChatPayException  # NOQA
from wechatx.oauth import WeChatOAuth  # NOQA
from wechatx.parser import parse_message  # NOQA
from wechatx.pay import WeChatPay  # NOQA
from wechatx.replies import create_reply  # NOQA

__version__ = '1.8.3'
__author__ = 'messense'

# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
