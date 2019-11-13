r_file = open("query_all.tsv")
w_file = open("out.txt", "wt")

def validParam(param):
    return param == 'query' or param == 'results' or param == 'bbox' or param == 'debug'

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
            if validParam(param):
                resultRow += (p + "&")
        resultRow = resultRow[:-1]
        if 'query=' in resultRow:
            w_file.write('/v1' + url + '?' + resultRow + '\n')
