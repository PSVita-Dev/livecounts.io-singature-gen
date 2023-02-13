import time
import hashlib
import http.client

class Gen:
    def __init__(this):
        this.ts = round(time.time() * 1000)
        this.rip = hashlib.new('ripemd160')
        this.s2 = hashlib.new('sha256')
        this.s3 = hashlib.new('sha384')
        this.ajay = ""
        this.midas = ""
        
    def generate(this):

        this.rip.update(str(this.ts).encode())
        this.ajay = this.rip.hexdigest()
        
        this.s2.update((str(this.ts) + "64").encode())

        
        this.s3.update(this.s2.digest())
        this.midas = this.s3.hexdigest()
        
        return {"x-midas":this.midas,"x-ajay":this.ajay,"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0","x-catto": str(this.ts),"x-test": "x","Referer": "https://tokcount.com/",
    "Origin": "https://tokcount.com"}
        
if __name__ == "__main__":
    heads = Gen().generate()
    print(heads)
    conn = http.client.HTTPSConnection("tiktok.livecounts.io")

    conn.request("GET", "/user/stats/127905465618821121", "", heads)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
