import os

html_head = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>\n'
html_end = '</body></html>'

path = '一拳超人/'
list = os.listdir(path)
with open(path[:-1] + '.html', 'w', encoding='utf-8') as f:
    f.write(html_head)
    for item in list:
        if not any(i in item for i in ['.', '卷']):
        # if not "." in item:
            html_body = '<h1 align="center">{}</h1>\n'.format(item)
            f.write(html_body)
            new_path = path + item
            pic_list = os.listdir(new_path)
            for pic in pic_list:
                pic_path = new_path + "/" + pic
                num = pic.split('.')[0]
                if len(num) == 2:
                    newname = new_path + "/0" + pic
                    os.rename(pic_path, newname)
                    pic_path = newname
                html_img = '<center><img src="{}" alt="{}"></center>\n'.format(pic_path, num)
                f.write(html_img)
    f.write(html_end)