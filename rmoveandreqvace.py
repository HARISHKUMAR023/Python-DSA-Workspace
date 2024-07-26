class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                # Collect characters until we find a matching '('
                substr = []
                while stack and stack[-1] != '(':
                    substr.append(stack.pop())
                stack.pop()  # Remove the '('
                # Reverse the collected substring and push back to stack
                stack.extend(substr)
            else:
                # Push current character to the stack
                stack.append(char)

        return ''.join(stack)


# Example usage
sol = Solution()
# print(sol.reverseParentheses("(abcd)"))  # Output: "dcba"
print(sol.reverseParentheses("(u(love)i)"))  # Output: "iloveu"
print(sol.reverseParentheses("(ed(et(oc))el)"))  # Output: "leetcode"
