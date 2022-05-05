import socket

def getWebData():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    response = ''
    

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        line =(data.decode())
        response += line
    mysock.close()
    response = response.splitlines()

    header_dictionary = build_header_dictionary(response)
    for key, value in header_dictionary.items():
        print(f'{key} : {value}')
    #print(response)
    data_list = build_data_list(response)
    for line in data_list: 
        print(line)

def build_header_dictionary(response_list):
    header_dictionary = {}

    for line in response_list: 
        if ":" in line:
            splitline = line.split(": ")
            key,value = splitline[0],splitline[1]
            header_dictionary[key]=value
    return header_dictionary     

def build_data_list(response_list):
    data_list = []
    atData = False 
    
    for line in response_list: 
        #print(line)
        
        if line == '': 
            atData = True
            data_list.append(line)
        elif atData == True:
            data_list.append(line)
        else: 
            #print(line)
            continue
    return data_list


# getWebData()