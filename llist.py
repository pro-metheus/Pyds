class node():
    def __init__(self,data=None,link=None):
        self.data=data
        self.link=link
    def get_data(self):
        return(self.data)


if __name__=='__main__':
    cur=node()
    root=node()
    while 1:
        op=input("enter option code :")
        if op=='1':#add to link list
            if root.data==None:
                root.data=input("enter data :")
                cur=root
            else:
                new=node()
                new.data=input("enter data :")
                cur.link=new
                cur=new
        if op=='2':
            cur=root
            while cur.data:
                print(cur.get_data())
                cur=cur.link
        
