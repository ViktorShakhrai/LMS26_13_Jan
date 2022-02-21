'''Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found - raise ValueError with proper info Message'''
'''Розширте стек, щоб включити метод під назвою get_from_stack, який шукає та повертає елемент e зі стека. 
Будь-який інший елемент повинен залишатися в стеку з дотриманням їх порядку. 
Розглянемо випадок, коли елемент не знайдено - підняти ValueError за допомогою правильного інформаційного повідомлення'''

import stack_module


class New_stack(stack_module.Stack):
    def get_from_stack(self, index):
        for i in New_stack:
            if i.data == index:
                a = New_stack.pop()


