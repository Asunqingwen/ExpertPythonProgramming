'''参数检查'''
# rpc_info = {}
#
#
# def xmlrpc(in_=(), out=(type(None),)):
# 	def _xmlrpc(function):
# 		# 注册签名
# 		func_name = function.__name__
# 		rpc_info[func_name] = (in_, out)
#
# 		def _check_types(elements, types):
# 			'''用来检查类型的子函数'''
# 			if len(elements) != len(types):
# 				raise TypeError('argument count is wrong')
# 			typed = enumerate(zip(elements, types))
# 			for index, couple in typed:
# 				arg, of_the_right_type = couple
# 				if isinstance(arg, of_the_right_type):
# 					continue
# 				raise TypeError('arg #%d should be %s' % (index, of_the_right_type))
#
# 		# 包装过的函数
# 		def __xmlrpc(*args):  # 没有允许的关键词
# 			# 检查输入的内容
# 			checkable_args = args[1:]  # 去掉self
# 			_check_types(checkable_args, in_)
# 			# 运行函数
# 			res = function(*args)
# 			# 检查输出的内容
# 			if not type(res) in (tuple, list):
# 				checkable_res = (res,)
# 			else:
# 				checkable_res = res
# 			_check_types(checkable_res, out)
#
# 			# 函数及其类型检查成功
# 			return res
#
# 		return __xmlrpc
#
# 	return _xmlrpc
#
#
# class RPCView:
# 	@xmlrpc((int, int))  # two int -> None
# 	def meth1(self, int1, int2):
# 		print('received %d and %d' % (int1, int2))
#
# 	@xmlrpc((str,), (int,))  # string -> int
# 	def meth2(self, phrase):
# 		print('received %s' % phrase)
# 		return 12
# print(rpc_info)
# my = RPCView()
# my.meth1(1,2)
# my.meth2(2)

'''缓冲'''
# import hashlib
# import pickle
# import time
#
# cache = {}
#
#
# def is_obsolete(entry, duration):
# 	return time.time() - entry['time'] > duration
#
#
# def compute_key(function, args, kw):
# 	key = pickle.dumps((function.__name__, args, kw))
# 	return hashlib.sha1(key).hexdigest()


# def memoize(duration=10):
# 	def _memoize(function):
# 		def __memoize(*args, **kw):
# 			key = compute_key(function, args, kw)
#
# 			# 是否已经拥有它了？
# 			if (key in cache and not is_obsolete(cache[key], duration)):
# 				print('we got a winner')
# 				return cache[key]['value']
# 			# 计算
# 			result = function(*args, **kw)
# 			# 保存结果
# 			cache[key] = {
# 				'value': result,
# 				'time': time.time()
# 			}
# 			return result
#
# 		return __memoize
#
# 	return _memoize


# @memoize()
# def very_very_very_complex_stuff(a, b):
# 	# 如果在执行这个计算时计算机过热
# 	# 请考虑终止程序
# 	return a + b
# print(very_very_very_complex_stuff(2,2))
# print(very_very_very_complex_stuff(2,2))
# @memoize(1)
# def very_very_very_complex_stuff(a, b):
# 	# 如果在执行这个计算时计算机过热
# 	# 请考虑终止程序
# 	return a + b
#
#
# print(very_very_very_complex_stuff(2, 2))
# print(very_very_very_complex_stuff(2, 2))
# print(cache)
# time.sleep(2)
# print(very_very_very_complex_stuff(2, 2))

'''代理'''

# class User(object):
# 	def __init__(self, roles):
# 		self.roles = roles
#
#
# class Unauthorized(Exception):
# 	pass
#
#
# def protect(role):
# 	def _protect(function):
# 		def __protect(*args, **kw):
# 			user = globals().get('user')
# 			if user is None or role not in user.roles:
# 				raise Unauthorized("I won't tell you")
# 			return function(*args, **kw)
#
# 		return __protect
#
# 	return _protect
# tarek = User(('admin','user'))
# bill=User(('user',))
# class MySecrets(object):
# 	@protect('admin')
# 	def waffle_recipe(self):
# 		print('use tons of butter!')
# these_are = MySecrets()
# user = tarek
# print(these_are.waffle_recipe())
# user = bill
# print(these_are.waffle_recipe())

'''上下文提供者'''
from threading import RLock

lock = RLock()


def synchronized(function):
	def _synchronized(*args, **kw):
		lock.acquire()
		try:
			return function(*args, **kw)
		finally:
			lock.release()
		return _synchronized


@synchronized
def thread_safe():  # 确保锁定资源
	pass
