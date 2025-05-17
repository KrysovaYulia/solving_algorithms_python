stack = []
class Stack:

    
    def push_n(self, n):
        stack.append(n)
      
        print("ok")
    def pop(self):
        print(stack.pop()) if  len(stack) != 0 else print("error")
    def back(self):
        print(stack[-1]) if len(stack) != 0 else print("error")
    def size(self):
        print(len(stack))
    
    def clear(self):
        stack.clear()
        print("ok")
    def exit(self):
        print("bye")
command = []
s = " "
while s != "":
    s = input()
    command.append(s.split())
    if s == 'exit':
        break
   
for i in command: 

    if i[0] == 'push':
        st = Stack()
        st.push_n(i[-1])
    elif i[0] == 'pop':
        st = Stack()
        st.pop()
    elif i[0] == 'back':
        st = Stack()
        st.back()
    elif i[0] == 'size':
        st = Stack()
        st.size()
    elif i[0] == 'clear':
        st = Stack()
        st.clear()
    elif i[0] == 'exit':
        st = Stack()
        st.exit()