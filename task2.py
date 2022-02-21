'''Write a program that reads in a sequence of characters,
and determines whether it's parentheses, braces, and curly brackets are "balanced."'''
import stack_module

open_list = ["{", "[", "("]
close_list = ["}", "]", ")"]


def check_parentheses(my_check_str):
    stack = stack_module.Stack()
    for i in my_check_str:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check_parentheses(string))
