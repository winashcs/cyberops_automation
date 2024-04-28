import keyboard
f=open("record.txt",'a')
r=keyboard.record(until="escape")
t=keyboard.get_typed_strings(r)
x="".join(t)
f.write(x+'\n')
f.close()
