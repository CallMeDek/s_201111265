
#coding: utf-8

def convert_url_os_path_join(params):
    params_c = ''
    for char in params:
        if char == '\\':
            params_c += '/'
        else:
            params_c += char
    return params_c

def convert_urllib_urlencode(params):
    params_c = ''
    i = 0
    while(i < len(params)-2):
        if(params[i] == '%'):
            if((params[i+1]=='2') and(params[i+2] == '5')):
                params_c += '%'
                i += 3
                continue
        params_c += params[i]
        i += 1
    params_c += params[-2]
    params_c += params[-1]
    return params_c