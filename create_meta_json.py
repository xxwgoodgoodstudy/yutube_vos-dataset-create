# --------------------------------------------------------
# SiamMask
# Licensed under The MIT License
# Written by Qiang Wang (wangqiang2015 at ia.ac.cn)
# --------------------------------------------------------
import json
import os

# print('load json (raw ytb_vos info), please wait 10 seconds~')
# ytb_vos = json.load(open('H:/dataset/object_tracker/yutube_vos/train/instances_train.json', 'r'))
directory = 'G:/dataset/object_tracker/sonar/train/JPEGImages'
snippets = dict()
folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
print(folders)
video = dict()
for f in folders:
    video_name = dict()
    objects = dict()
    id = dict()
    id["category"] = f.rstrip('0123456789')
    img_path = os.path.join(directory, f)
    image_names = [os.path.splitext(file)[0] for file in os.listdir(img_path)]
    print(image_names)
    id["frames"] = image_names
    objects["1"] = id
    video_name["objects"] = objects
    video[f] = video_name

snippets["videos"] = video

train = snippets
print(train)

json.dump(train, open('G:/dataset/object_tracker/sonar/meta.json', 'w'), indent=4, sort_keys=True)
print('done!')


