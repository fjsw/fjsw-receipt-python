""" gateway
"""
import urllib
import urllib2
import time
import hmac
import hashlib

class Gateway(object):
    """ gateway
    """
    def __init__(self, gateway_url, appid, appsecret):
        self._gateway_url = gateway_url
        self._appid = appid
        self._appsecret = appsecret

    def call_method(self, data):
        """ invoke method throud gateway
        """
        data["appid"] = self._appid
        data["timestamp"] = str(int(time.time()))
        # prepare sign
        items = data.items()
        items.sort()
        presign_str = ""
        for value in items:
            presign_str += str(value[0])
            presign_str += str(value[1])
        #print presign_str
        # signature
        signature = hmac.new(self._appsecret, presign_str, hashlib.md5).hexdigest().upper()
        #print signature
        data["sign"] = signature
        print data
        self._call(data)

    def _call(self, data):
        """ invoke method throud gateway
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Content-Type': "application/x-www-form-urlencoded"
        }
        try:
            formdata = urllib.urlencode(data)
            #print formdata
            req = urllib2.Request(url=self._gateway_url, data=formdata, headers=headers)
            print req
            f = urllib2.urlopen(req)
            response_str = f.read()
        except Exception, e:
            print Exception,":",e
