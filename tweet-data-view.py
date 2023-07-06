import os
import re
from pyecharts import options as opts
from pyecharts.charts import Bar,Grid,Timeline

dir_path="D:\\Desktop\\Archive"  #change the file location of your data set

paths=[os.path.join(dir_path,i) for i in os.listdir(dir_path)]
t=(
    Timeline()
    .add_schema(is_auto_play=True)
)
index=0
for i in paths:
    index+=1
    f=open(i,'r',encoding='utf-8')
    data=f.read()
    f.close()
    city=re.findall(r'Location: (.*?)\n',data)
    positive_tweet_percentage=re.findall(r'Positive tweet percentage: (.*?)\n',data)
    negative_tweet_percentage=re.findall(r'Negative tweet percentage: (.*?)\n',data)
    neutral_tweet_percentage=re.findall(r'Neutral tweet percentage: (.*?)\n',data)
    bar1 = (
        Bar()
        .add_xaxis(city)
        .add_yaxis("positive", [round(float(i),2) for i in positive_tweet_percentage[::2]])
        .add_yaxis("negative", [round(float(i),2) for i in negative_tweet_percentage[::2]])
        .add_yaxis("neutral", [round(float(i),2) for i in neutral_tweet_percentage[::2]])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="pro-russian"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}%")
            )
        )
    )
    bar2 = (
        Bar()
        .add_xaxis(city)
        .add_yaxis("positive", [round(float(i),2) for i in positive_tweet_percentage[1::2]])
        .add_yaxis("negative", [round(float(i),2) for i in negative_tweet_percentage[1::2]])
        .add_yaxis("neutral",[round(float(i),2) for i in neutral_tweet_percentage[1::2]])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="pro-ukrainin", pos_top="48%"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} %")
            )
        )
    )
    grid = (
        Grid()
        .add(bar1, grid_opts=opts.GridOpts(pos_bottom="60%"))
        .add(bar2, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    t.add(grid,str(index)).render("tweet.html")  #the path and file name of the saved pages
