#coding=utf-8
""" receipt
"""
import gateway

class Receipt(object):
    """ receipt
    """
    def __init__(self, gateway_url, appid, appsecret):
        self.gateway = gateway.Gateway(gateway_url, appid, appsecret)

    def scan_authcode(self, request):
        """ invoke method throud gateway
        """
        scan_authcode_request = {
            "method": "receipt.scan.authcode",
            "merchid": request["merchid"],
            "devid": request["devid"],
            "amount": request["amount"],
            "authcode": request["authcode"],
            "orderinfo": request["orderinfo"]
        }
        response = self.gateway.call_method(scan_authcode_request)
        return response

    def query_order(self, orderid):
        """ invoke method throud gateway
        """
        query_order_request = {
            "method": "receipt.scan.authcode",
            "orderid": orderid
        }
        response = self.gateway.call_method(query_order_request)
        return response
