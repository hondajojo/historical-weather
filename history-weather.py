#coding:utf-8
import urllib2
import re
import sys

url = 'http://www.tianqihoubao.com/lishi/hangzhou/%s.html' % sys.argv[1]
html = urllib2.urlopen(url).read()
#print html
search = r'<b>(\d{1,2}).*?</b></td>'
#search = r'<b>(.*?)</b></td>'

temp = re.findall(search,html)
#print tem


#print type(sys.argv[1])
print sys.argv[1]+'\n'+'最高温度:'.decode('u8')+temp[0]+'℃'.decode('u8')+'\n'+'最低温度:'.decode('u8')+temp[1]+'℃'.decode('u8')
#for i in temp:
    #print i.decode('gbk')  #正常显示中文
print u'最高温度',temp[0]