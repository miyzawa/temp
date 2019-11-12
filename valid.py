r_file = open("Desktop/a.txt")
w_file = open("Desktop/out.txt", "wt")

def validParam():
    return param == 'query' or param == 'results' or param == 'appid'

with r_file as file:
    for row in file:
        line = row.rstrip('\n')
        urlParam = line.split("?")
        url = urlParam[0]
        param = urlParam[1]
        paramlist = param.split("&")
        resultRow= ""
        for p in paramlist:
            paramValue = p.split("=")
            param = paramValue[0]
            value = paramValue[1]
            if validParam():
                resultRow += (p + "&")
        resultRow = resultRow[:-1]
        w_file.write(url + '?' + resultRow + '\n')
