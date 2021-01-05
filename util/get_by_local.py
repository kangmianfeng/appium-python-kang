#coding=utf-8
#把定位方法封装到ini文件里


from util.read_init import ReadIni


class GetByLocal:
	def __init__(self,driver):
		self.driver = driver
	def get_element(self,section,key):
		read_ini = ReadIni()
		# "id > cn.com.open.mooc: id / login_lable"
		local = read_ini.get_value(section,key)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				elif by == 'uiautomator':
					# print('转换前：'+local_by) #打印输出发现中文乱码
					return self.driver.find_element_by_android_uiautomator(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				#self.driver.save_screenshot("../jpg/test02.png")
				return None
		else:
			return None


