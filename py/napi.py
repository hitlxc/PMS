#coding=utf-8

import cv2
import numpy
import argparse

import os
ddir = os.path.split(os.path.realpath(__file__))[0]


# /usr/bin/python /opt/lampp/htdocs/PMS/py/api.py root/332800f9-38e8-4a62-907f-599f692f2c7e.jpg -i 10 20 3
IMAGE_URL = './Public/photo'

def main(filename,args):
	url = IMAGE_URL + "/" + filename
	# url = ddir+'/'+filename
	print url
	image = cv2.imread(url)
	blur = cv2.bilateralFilter(image,args[0],args[1],args[2])
	# cv2.imwrite(ddir+"/new.jpg", blur)
	cv2.imwrite(ddir+"/tmp.jpg", blur)

def run():

	parser = argparse.ArgumentParser(description='图像处理api')
	parser.add_argument('file', help="输入图片文件名") 
	parser.add_argument('-i', metavar='N', type=int, nargs='+',
	                    help='输入三个参数,滤波领域直径,空间高斯函数标准差,灰度值相似性标准差')
	# 11 51 51
	args = parser.parse_args()
	main(args.file,args.i)

if __name__ == '__main__':
	run()