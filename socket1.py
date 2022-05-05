import socket

def getWebData():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    raw = ""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        raw += data.decode()
    mysock.close()
    raw = raw.splitlines()
    headerDict = getHTTPHeaders(raw)
    
    print('Headers:')
    for key, value in headerDict.items():
        print(f'{key} : {value}')
    
    print("\nData:")
    data = getData(raw)
    for line in data:
        print(line)


def getData(rawData):
    data = []
    dataBool = False

    for line in rawData:
        if line == "":
            dataBool = True
            data.append(line)
        elif dataBool == True:
            data.append(line)
        else: 
            continue
    return data


def getHTTPHeaders(rawData):
    retDict = {}
    for line in rawData:
        if line == "":
            break
        if ":" not in line:
            continue
        retDict[(line.split(':', 1)[0].strip())] = line.split(':', 1)[-1].strip()
    
    return retDict

if __name__ == "__main__":    
    getWebData()