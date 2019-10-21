import os
from scrapy.http import HtmlResponse
import urllib.request

class ResponseProvider():

    def create_response_from_web(self, resourceUrl):
        web_request = urllib.request.urlopen(resourceUrl)
        byte_response = web_request.read()
        response_content =  byte_response.decode("utf8")
        return HtmlResponse(url=resourceUrl, body=response_content, encoding='utf-8')
    
    def create_response_from_file(self, htmlSource, resourceUrl):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_dir = '/'.join(test_dir.split('/')[0:3])
        html = open(test_dir + '/' + htmlSource, 'r', encoding='utf-8')
        file_content = html.read()
        html.close()
        return HtmlResponse(url=resourceUrl, body=file_content, encoding='utf-8')