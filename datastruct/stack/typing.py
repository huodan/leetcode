# -*- coding: utf-8 -*-

# 使用堆栈特性 先进后出
#
# @param s string字符串
# @return string字符串
#
class Solution:

	def Typing(self, s):
		# write code here
		import string
		temp_stack = []
		for i in range(len(s)):
			if s[i] not in string.ascii_lowercase + "<":
				raise Exception("输入数据不符合要求，请输入小写字母或'<'")
			if s[i] != "<":
				temp_stack.append(s[i])
			elif s[i] == "<":
				if len(temp_stack) == 0:
					continue
				else:
					temp_stack.pop()

		return "".join(temp_stack)


# ----------------------------------------
# 测试

from testbase import TestCase
from testbase import datadrive


test_data = [
	("acv<", "ac"),
	("fakdjhfi<<<<<sfada<fda<", "faksfadfd"),
	("<fadf<<<<<afeafda<<","afeaf")
]

@datadrive.DataDrive(case_data=test_data)
class TestTyping(TestCase):
	"""测试typing
	"""
	owner = "dan.huo"
	status = TestCase.EnumStatus.Ready
	priority = TestCase.EnumPriority.Normal
	timeout = 1

	def run_test(self):
		typing = self.casedata[0]
		expect = self.casedata[1]
		actual = Solution().Typing(typing)

		self.assert_("", actual == expect)


if __name__ == '__main__':

	TestTyping().debug_run()
