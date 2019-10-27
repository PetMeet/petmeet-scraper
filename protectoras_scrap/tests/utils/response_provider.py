import os
from scrapy.http import HtmlResponse, Request
import urllib.request

CODECS = ['utf8', 'iso-8859-1']


def force_decoding(byte_response):
    for i in CODECS:
        try:
            return byte_response.decode(i)
        except UnicodeDecodeError:
            pass


class ResponseProvider:

    @staticmethod
    def create_response_from_web(resourceUrl, meta={}):
        request = Request(resourceUrl, meta=meta)
        web_request = urllib.request.urlopen(resourceUrl)
        byte_response = web_request.read()
        response_content = force_decoding(byte_response)
        return HtmlResponse(url=resourceUrl, body=response_content, encoding='utf-8', request=request)

    @staticmethod
    def create_response_from_file(htmlSource, resourceUrl, meta={}):
        request = Request(resourceUrl, meta=meta)
        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '/'.join(test_dir.split('/')[0:3])
        html = open(test_dir + '/' + htmlSource, 'r', encoding='utf-8')
        file_content = html.read()
        html.close()
        return HtmlResponse(url=resourceUrl, body=file_content, encoding='utf-8', request=request)
