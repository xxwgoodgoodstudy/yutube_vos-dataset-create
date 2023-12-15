# yutube_vos-dataset-create
制作yutube-vos格式的目标跟踪训练集
步骤：
1、运行rename.py修改图片名称（1.png改成00001.jpg）
2、运行imagecut.py改变图片大小（yutube-vos大小为1280*720）
3、用eiseg标注图片，生成mask眼膜图片
4、运行create_meta_json.py生成meta.json
5、运行parse_sonar_vos.py生成instance_train.json（输入为meta.json和掩膜图片）
6、运行par_crop.py裁剪rgb图片和掩膜图片，生成crop文件夹
7、运行gen_json.py生成train.json

