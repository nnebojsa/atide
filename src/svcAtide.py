import web
from atide import atide

#from atide import *
#import urllib2
#import json
#import time

urls = ('/svcAtide', 'svcAtide')
    
class svcAtide:
    def GET(self):
        data = web.input()
        
        rev1 = float(data.inc1)
        rev2 = float(data.inc2)
        expens = float(data.expens)
        
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        a = atide(rev1, rev2, expens)
        
        #res = a.calcAtide()
        
        #return res
        return a.calcAtide()
        #return 'Hallo'
    
    
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    
