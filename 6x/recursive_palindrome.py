# Uses python3
# Recursive palindrome

def isPalindrome(s):
	def formatString(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans += c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	return isPal(formatString(s))
