# -*- coding: utf-8 -*-

"""
题目描述
打字
时间限制 :1sec / 空间限制: 256MB

题意：
牛妹在练习打字，现在按照时间顺序给出牛妹按下的键（以字符串形式给出,'<'代表回退backspace，其余字符均是牛妹打的字符，字符只包含小写字母与'<'），牛妹想知道最后在屏幕上显示的文本内容是什么。
在文本内容为空的时候也可以按回退backspace（在这种情况下没有任何效果）。

输入：
给定一个字符串s，代表牛妹所按下的按键。
1<s.length\leq10^51<s.length≤10
5

输出：
返回一个字符串代表最后在屏幕上显示的文本内容。

若为空则返回一个空串。



"""
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
