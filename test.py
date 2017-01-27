import hashlib
import codecs
appkey='85eb6835b0a1034e'
secretkey = '2ad42749773c441109bdc0191257a664'
cid = str(13433643)
aid = 8167928
s = 'appkey=' + appkey + '&cid=' + cid + secretkey
print codecs.decode(b"4f6c6567", "hex_codec")
s.replace(' ','')
print s.encode("UTF-8")
sign = codecs.decode(s.encode("UTF-8"), 'hex_codec')

print sign
sign_this = hashlib.md5(sign).hexdigest()
url = 'http://interface.bilibili.com/playurl?appkey=' + appkey + '&cid=' + str(cid) + '&sign=' + sign_this

print url