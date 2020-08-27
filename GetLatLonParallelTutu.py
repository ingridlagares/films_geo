API = 'https://nominatim.openstreetmap.org/search?q=%s&format=json&addressdetails=1'
def getlatlon(x):
    try:
        js = x.json()
        latlon = (js[0]['lat'], js[0]['lon'])
        return latlon
    except:
        return None

results = []
BATCHSIZE = 10
for x in range(0,len(director_locations),BATCHSIZE):
    chunks = (grequests.get(API % u[1]) for u in dls[x:x+BATCHSIZE])
    print(x)
    ans = grequests.map(chunks)
    chunkslist = list(map(getlatlon, ans))
    for z in range(len(chunkslist)):
        results.append((dls[x+z][0], dls[x+z][1], chunkslist[z]))
        print(results[-1])