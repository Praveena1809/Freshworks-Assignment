import code as x 
x.create("Singapore",25)
x.create("Canada",70,3600) 
x.read("Singapore")

x.read("Canada")

x.create("Chennai",50)

x.modify("Chennai",55)

x.delete("Chennai")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()