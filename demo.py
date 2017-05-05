#coding=utf-8
import gateway

if __name__ == '__main__':
    DATA = {
        "method":"receipt.scan.authcode",
        "merchid": 1484901323,
        "devid": "123",
        "amount": 1,
        "authcode": "286579303676489102",
        "orderinfo": "111"
    }
    APPID = "12345"
    APPKEY = '12345'
    GATEWAYURL = "http://api.test.shuwang.info/receipt/rest"
    receipt = gateway.Gateway(GATEWAYURL, APPID, APPKEY)
    receipt.call_method(DATA)

