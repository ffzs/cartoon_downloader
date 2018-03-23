import os

html_head = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>\n'
html_end = '</body></html>'

path = '一拳超人/'

list = os.listdir(path)
print(len(list))
for item in list:
    html_body = '<h1 align="center">{}</h1>\n'.format(item)
    new_path = path + item
    pic_list = os.listdir(new_path)
    for pic in pic_list[:-1]:
        new_name = "0" + pic if len(pic) == 6 else pic
        os.rename(new_path + "/" + pic, new_path + "/" + new_name)
    pic_list = os.listdir(new_path)
    with open(new_path + '/render.html', 'w', encoding='utf-8') as f:
        f.write(html_head)
        f.write(html_body)
        for pic in pic_list[:-1]:
            num = pic.split('.')[0]
            html_img = '<center><img src="{}" alt="{}"></center>\n'.format(pic, num)
            f.write(html_img)
        f.write(html_end)

with open(path+path.split("/")[0]+'.html','w',encoding='utf-8') as f:
    f.write(html_head)
    for item in list:
        href =item + '/render.html'
        html_a = '<dt><a href="{}" target="_blank">{}</a></dt>\n'.format(href, item)
        f.write(html_a)
    f.write(html_end)


