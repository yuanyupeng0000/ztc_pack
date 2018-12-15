import os
import time
import xml.dom.minidom as xmldom

SEED_XML_DIR = '/data/wxjs/Annotations/'
SEED_IMG_DIR = '/data/wxjs/JPEGImages/'
SEED_CHG_DIR = '/data/wxjs/Changed_Annotations/'
TEST_DIR = '/data/wxjs/test/'
start_time = time.time()

seed_xml_names = os.listdir(SEED_XML_DIR)
seed_img_names = os.listdir(SEED_IMG_DIR)
seed_chg_names = os.listdir(SEED_CHG_DIR)

for xml in seed_chg_names:
    dom = xmldom.parse(SEED_XML_DIR + xml)
    root = dom.documentElement #
    obj_elements = root.getElementsByTagName('object')
    if(len(obj_elements) > 0):
        for obj_element in obj_elements:
            name = obj_element.getElementsByTagName('name')
            if(len(name) > 0):
                name_data = name.item(0).firstChild.data
                #print('name_data: ' + name_data)
            cover = obj_element.getElementsByTagName('cover')
            if(len(cover) > 0):
                cover_data = cover.item(0).firstChild.data
                #print('cover_data: ' + cover_data)
            spray = obj_element.getElementsByTagName('spray')
            if(len(spray) > 0):
                spray_data = spray.item(0).firstChild.data
                #print('spray_data: ' + spray_data)
            name.item(0).firstChild.data = name_data[:7] + "_" + str(cover_data) + str(spray_data)
    try:
        with open(SEED_CHG_DIR + str(i) + '_' + xml,'w',encoding='UTF-8') as fh:           
	    # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
	    # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
            dom.writexml(fh,indent='',addindent='\t',newl='\n',encoding='UTF-8')
            print('写入xml OK!')
    except Exception as err:
        print('错误信息：{0}'.format(err))
