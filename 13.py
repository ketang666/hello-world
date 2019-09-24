import easygui as g
#list1=g.multenterbox('','')=========不要这样写，把代码写得又臭又长
choise=['*用户','*true name','telenumbebr','*phonenumber','QQ','*e-mail']
msg='用户\ntruename\ne-mail'
while True:
    list1=g.multenterbox(msg,'center',choise)
    requir1=list1[0]=='' or list1[1]=='' or list1[3]=='' or list1[5]==''
    requir2=list1[0].isspace or list1[1].isspace or list1[3].isspace or list1[5].isspace
    if requir1 or requir2:
        g.msgbox('write your imformation')
    else:
        break
    
    
