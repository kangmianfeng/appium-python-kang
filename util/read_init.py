#coding=utf-8
#读取.ini格式文件的工具类

import configparser


class ReadIni:
	def __init__(self,file_path=None):
		#判断是否用默认参数变量
		if file_path == None:
			self.file_path = '../config/base_install_mooc.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path)
		return read_ini

	#通过key获取对应的value
	def get_value(self,section,key):
		if section == None:
			section = 'login_element'
		else:
			section == section
		#捕获处理异常处理
		try:
			value = self.data.get(section,key)		
		except:
			value = None
		return value


if __name__ == '__main__':
	read_ini = ReadIni()  #python获得一个class的实例化对象，类名后面必须要有()
	print(read_ini.get_value("login_element","username"))
	print(read_ini.get_value("install_mooc","swipe_left_times"))
