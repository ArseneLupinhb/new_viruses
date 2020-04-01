from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import datetime
import json

# 读原始数据文件
today = datetime.date.today().strftime('%Y%m%d')   #20200315
datafile = 'data/'+ today + '.json'
with open(datafile, 'r', encoding='UTF-8') as file:
    json_array = json.loads(file.read())

# 分析全国实时确诊数据：'confirmedCount'字段
china_data = []
for province in json_array:
    china_data.append((province['provinceShortName'], province['confirmedCount']))
china_data = sorted(china_data, key=lambda x: x[1], reverse=True)

china_data
labels = [data[0] for data in china_data]
counts = [data[1] for data in china_data]

c = (
    Pie(init_opts=opts.InitOpts(width='650px', height='600px'))
    .add("", [list(z) for z in zip(labels, counts)])
    .set_global_opts(title_opts=opts.TitleOpts(),
                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="85%"),

                     )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"),
                     legend_opts=opts.LegendOpts(is_show=False),)
    .render(path='data/新增确饼图.html')
)