__author__ = 'shaun'

# ! /usr/bin/python <br> # -*- coding: utf8 -*-
import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并储存响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code : ", r.status_code)

# 处理有关每篇文章的信息
submisssion_ids = r.json()
submisssion_dicts = []
plot_dicts = []
names = []
for submisssion_id in submisssion_ids[:10]:
    # 对每一篇文章都执行一个API调用
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submisssion_id) + '.json'
    submisssion_r = requests.get(url)
    # print("Status Code: ",submisssion_r.status_code)
    response_dict = submisssion_r.json()
    submisssion_dict = {
        'label': response_dict['title'],
        'xlink': response_dict['url'],
        # 'link': "http://news.ycombinator.com/item?id="+str(submisssion_id)+"",
        'value': response_dict.get('descendants', 0),  # 指定的键存在时返回相应的值，不存在时返回0
    }
    names.append(submisssion_dict['label'])

    submisssion_dicts.append(submisssion_dict)

submisssion_dicts = sorted(submisssion_dicts, key=itemgetter('value'), reverse=True)
result = list(map(lambda x: x['value'], submisssion_dicts))
print(result)
#
# my_comfig = pygal.Config()
# my_comfig.title = 'Top 10 Stories From Hacker-News'
# my_comfig.x_label_rotation = 45
# my_comfig.width = 1000
#
# my_style = LS('#883333', base_style=LCS)
# chart = pygal.Bar(my_comfig, style=my_style)
# chart.x_labels = names
# chart.add('stories', submisssion_dicts)
# chart.render_to_file('Top stories.svg')
