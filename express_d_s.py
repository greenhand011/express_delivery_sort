#快递信息进行分拣
import json
import pprint
with open("data.json",'r',encoding="utf-8")as f:
    data_list=json.load(f)

#["张*", "上海市徐汇区桂林路402号 诚达创意园76幢407室 银基科技"],


sort_dict={}
for data in data_list:
    province=data[1][0:2]
    if province in ["上海","北京","湖北","山东","安徽","陕西","河南","浙江"]:
        sort_dict.setdefault(province,[]).append(data)
pprint.pprint(sort_dict)