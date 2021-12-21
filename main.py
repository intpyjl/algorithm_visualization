from tkinter import *
import tkinter.messagebox  as tkMessageBox
import numpy as np
import tool
import ctypes
try:
    temp=ctypes.windll.LoadLibrary( 'opencv_videoio_ffmpeg454_64.dll' )
except:
    pass
def Bubble():
    num = number.get()
    GetKey("bubble",num,label_data.get(),sort_speed.get())
    pass
def QuickSort():
    num = number.get()
    GetKey("qsort",num,label_data.get(),sort_speed.get())
    pass

def Choose():
    num = number.get()
    GetKey("choose",num,label_data.get(),sort_speed.get())
    pass

def Merge():
    num = number.get()
    GetKey("merge", num,label_data.get(),sort_speed.get())
    pass
def GetKey(sorting_method,num="0",data_type="随机数据",speed="1"):
    if num=="":
        tkMessageBox.showinfo("warning", 'Input can not be null!', parent=root)
        return
    if num.isdigit() is False:
        tkMessageBox.showinfo("warning", 'Input should be integer!', parent=root)
        return
    if int(num)>=10000:
        tkMessageBox.showinfo("warning", 'Input is too big!', parent=root)
        return
    number.delete(0, "end")
    if data_type=="随机数据":
        d = 1000 * np.random.rand((int(num)))
    if data_type=="顺序数":
        d=np.arange(int(num))
    if data_type=="逆序数":
        d=np.arange(int(num))
        for i in range(int(num)):
            d[i]=int(num)-1-i
    v=tool.Visual(d, sorting_method,int(speed))
    if sorting_method=="merge":
        v.scale=v.scale/2
    v.start()
    v.finish()
    pass
def generate_1():
    if str_f.get() != "xyxyyxxyyxyxyxyyyxxx" and str_s.get() != 'xyx':
        str_f.delete(0, "end")
        str_s.delete(0, "end")
        str_f.insert(0, "xyxyyxxyyxyxyxyyyxxx")
        str_s.insert(0, 'xyx')
def generate_2():
    if str_f.get() != "aabaabaababaabcaa" and str_s.get() != 'aabaa':
        str_f.delete(0, "end")
        str_s.delete(0, "end")
        str_f.insert(0, "aabaabaababaabcaa")
        str_s.insert(0, 'aabaa')
def generate_3():
    str_f.delete(0, "end")
    str_s.delete(0, "end")
    s = np.random.randint(0, 25, 6)
    len1 = np.random.randint(13, 26)
    for i in range(len1):
        j = np.random.randint(0, 6)
        str_f.insert(i, chr(97 + s[j]))
    len2 = np.random.randint(2, int(len1 / 2))
    for i in range(len2):
        j = np.random.randint(0, 6)
        str_s.insert(i, chr(97 + s[j]))
def generate_4():
    str_f.delete(0, "end")
    str_s.delete(0, "end")

class string_match:
    str_a=""
    str_b=""
    STR = []
    f_string=[]
    t=0
    out=[]
    Thread=[]
    inter_time = 200
    def __init__(self):
        pass
    def KMP(self):
        for i in self.Thread:
            cv.after_cancel(i)
        self.STR = []
        self.t = 0
        self.out = []
        self.str_a = str_f.get()
        self.str_b = str_s.get()
        self.inter_time=400
        cv.delete(ALL)
        l = 60
        if len(self.str_b)==0 and len(self.str_a)==0:
            return
        P=self.pre(self.str_b)
        for i in range(len(self.str_a)):
            self.f_string.append(cv.create_text(l,40,font=("黑体",24),text=self.str_a[i]))
            cv.create_line(l-10,25,l-10,60)
            cv.create_line(l-10,25,l+10,25)
            cv.create_line(l - 10, 60, l + 10, 60)
            cv.create_line(l + 10, 25, l + 10, 60)
            l+=20
        cv.create_text(90,140,font=("黑体",18),text="预处理π[i]")
        l=180
        for i in range(len(self.str_b)):
            cv.create_text(l,140,font=("Times New Roman",18),text=str(P[i+1]))
            l+=30
        ans=0
        j=0
        i=0
        for k in range(len(self.str_b)):
            self.move(4,k,self.str_b[k])
        self.t = self.t + self.inter_time
        for i in range(len(self.str_a)):
            self.move(5, i, self.str_b[j])
            self.move(6, i, self.str_a[i])
            self.t = self.t + self.inter_time
            if j>=0 and self.str_b[j]!=self.str_a[i]:
                while j>0 and self.str_b[j]!=self.str_a[i]:
                    self.move(1, i, '')
                    j=P[j]
                    for k in range(len(self.str_b)):
                        self.move(4,i-j+k,self.str_b[k])
                    for k in range(j):
                        self.move(2,i-1-k,self.str_b[j-1-k])
                    self.move(5,i,self.str_b[j])
                    self.move(6,i,self.str_a[i])
                    self.t = self.t + self.inter_time
                if j==0 and self.str_b[j]!=self.str_a[i]:
                    self.move(1, i, '')
                    for k in range(len(self.str_b)):
                        self.move(4, i +1 - j + k, self.str_b[k])
                    for k in range(j):
                        self.move(2, i+1 - 1 - k, self.str_b[j - 1 - k])
                    self.t = self.t + self.inter_time
                    continue
            if self.str_b[j]==self.str_a[i]:
                self.move(2,i,self.str_b[j])
                self.t = self.t + self.inter_time
                j=j+1
            if j==len(self.str_b):
                ans+=1
                j=P[j]
                self.move(1, i, '')
                for k in range(len(self.str_b)):
                    self.move(4, i+1 - j + k, self.str_b[k])
                for k in range(j):
                    self.move(2, i+1 - 1 - k, self.str_b[j - 1 - k])
                self.t = self.t + self.inter_time
                self.move(3,i,str(ans))
        self.move(1,i,"")
        self.move(3,i,str(ans))
        self.str_b=""
        self.str_a=""
        #cv.create_text(90,180,font=("黑体", 24), text=str(ans))
    def text(self,num,cv):
        for k in self.out:
            cv.delete(k)
        self.out.append(cv.create_text(90, 180, font=("黑体", 24), text=num))
    def match(self,i,num,cv):
        l=60+i*20
        self.STR.append(cv.create_text(l, 90, font=("黑体", 24), text=num))
        self.STR.append(cv.create_line(l - 10, 75, l - 10, 110))
        self.STR.append(cv.create_line(l - 10, 75, l + 10, 75))
        self.STR.append(cv.create_line(l - 10, 110, l + 10, 110))
        self.STR.append(cv.create_line(l + 10, 75, l + 10, 110))
    def move(self,op,i,num):
        if op== 1:
            self.Thread.append(cv.after(self.t,self.delete,cv))
        if op==2:
            self.Thread.append(cv.after(self.t,self.draw,i,cv,num))
        if op ==3:
            self.Thread.append(cv.after(self.t,self.text,num,cv))
        if op ==4:
            self.Thread.append(cv.after(self.t,self.match,i,num,cv))
        if op==5:
            self.Thread.append(cv.after(self.t,self.cmp1,i,num,cv))
        if op==6:
            self.Thread.append(cv.after(self.t,self.cmp2,i,num,cv))
    def cmp1(self,i,num,cv):
        l = 60 + i * 20
        self.STR.append(cv.create_polygon(l - 9, 76, l - 10, 110, l + 10, 110, l + 10, 76, fill="orange"))
        self.STR.append(cv.create_text(l, 90, font=("黑体", 24), text=num))
    def cmp2(self,i,num,cv):
        l = 60 + i * 20
        self.STR.append(cv.create_polygon(l - 9, 26, l - 10, 60, l + 10, 60, l + 10, 26, fill="orange"))
        self.STR.append(cv.create_text(l, 40, font=("黑体", 24), text=num))
    def delete(self,cv):
        for k in self.STR:
            cv.delete(k)
        self.STR.clear()
    def draw(self,i,cv,num):
        l=60+i*20
        self.STR.append(cv.create_line(l, 56, 80 + (i - 1) * 20, 80, fill="red",width=2))
        self.STR.append(cv.create_polygon(l - 9, 76, l - 10, 110,l+10,110,l+10,76,fill="yellow"))
        self.STR.append(cv.create_polygon(l - 9, 26, l - 10, 60, l + 10, 60, l + 10, 26, fill="yellow"))
        self.STR.append(cv.create_text(l, 90, font=("黑体", 24), text=num))
        self.STR.append(cv.create_text(l,40,font=("黑体",24),text=num))
        #self.STR.append(cv.)
        return
    def pre(self,B):
        p=[0,0]
        j=0
        m=len(B)
        for i in range(1,m):
            while j>0 and B[j]!=B[i]:
                j=p[j]
            if B[j]==B[i]:
                j+=1
            p.append(j)
        return p
def KMP_menu():
    tkMessageBox.showinfo("Information", '使用方法：可以选择数据生成方式，当选择“输入”时请自行输入主串和模式串\n'
                                     '! 注意：字符串长度请不要超出输入框。随机数据可能并不好，请多试几遍:)', parent=root)
def sorting_menu():
    tkMessageBox.showinfo("Information", '使用方法：输入数字(30~600视觉效果最佳)，选择数据类型和速度（1~10），再点击排序选项开始排序',
                                      parent=root)
root = Tk()
root.title('Algorithm')  # 窗口的标题
root.geometry('1000x700+100+10')  # 窗口的大小
root.configure(bg="white")
menubar = Menu(root)
Controller=string_match()
intro= Menu(menubar, tearoff=False)
menubar.add_cascade(label="使用事项", menu=intro)
intro.add_command(label="排序", command=sorting_menu)
intro.add_command(label="KMP",command=KMP_menu)
root.config(menu=menubar)
entry_number = Label(root, text="输入数据个数:", font=("宋体", 14),bg="white")
entry_number.place(relx=0.40, rely=0.2)
number = Entry(root, bd=5)
number.place(relx=0.54, rely=0.19,width=60)
cv=Canvas(root,bg="white")
cv.place(relwidth=1,rely=0.4,height=600)
label_name = Label(root,
                   text='算法可视化软件',
                   font=('FZFJK', 24),  # 字体和字体大小
                   width=20, height=1,
                   bg="white"# 标签长宽（以字符长度计算）
                   )
label_name.place(relx=0.35, rely=0)
label_sorting=Label(root,
                    text="·排序可视化",
                    font=('FZFJK',17),
                    bg="white"
                    )
label_sorting.place(rely=0.05)
label_rank = Label(root,
                   text='排序方式',
                   font=('黑体', 18),  # 字体和字体大小
                   height=2,
                   relief="solid",
                   bg="white"
                   )
label_rank.place(relx=0.05, rely=0.1)

bubble = Button(text="冒泡排序", font=('楷体', 20),
                command=Bubble,
                relief="raised"
                )
bubble.place(relx=0.2, rely=0.1)

quick_sort = Button(text="快速排序", font=('楷体', 20),
                    command=QuickSort,
                    relief="raised",
                    )
quick_sort.place(relx=0.4, rely=0.1)

choose = Button(text="选择排序", font=('楷体', 20),
                command=Choose,
                relief="raised"
                )

choose.place(relx=0.6, rely=0.1)

merge = Button(text="归并排序", font=('楷体', 20),
               command=Merge,
               relief="raised"
               )

merge.place(relx=0.8, rely=0.1)

label_data = Spinbox(root,
                   values=("随机数据","逆序数","顺序数"),
                   font=('黑体', 18),  # 字体和字体大小
                   relief="solid",
                   width=10,
                    wrap=True
                   )
label_data.place(relx=0.05, rely=0.2)
entry_speed = Label(root, text="排序速度:", font=("宋体", 14),bg="white")
entry_speed.place(relx=0.21, rely=0.2)
sort_speed = Spinbox(root,
                   from_=1,
                    to=10,
                   font=('黑体', 18),  # 字体和字体大小
                   relief="solid",
                   width=4,
                    wrap=True
                   )
sort_speed.place(relx=0.30, rely=0.2)
label_kmp=Label(root,
                    text="·KMP",
                    font=('FZFJK',17),
                    bg="white"
                    )
label_kmp.place(rely=0.27)
entry_father = Label(root, text="主串:", font=("宋体", 14),bg="white")
entry_father.place(relx=0.1, rely=0.3)
str_f = Entry(root, bd=5)
str_f.place(relx=0.15, rely=0.3,width=200)
entry_son = Label(root, text="模式串:", font=("宋体", 14),bg="white")
entry_son.place(relx=0.07, rely=0.35)
str_s = Entry(root, bd=5)
str_s.place(relx=0.15, rely=0.35,width=200)
example=IntVar()
example.set(4)
Radiobutton(root,text="样例1",command=generate_1,variable=example,value=1).place(relx=0.35,rely=0.3)
Radiobutton(root,text="样例2",command=generate_2,variable=example,value=2).place(relx=0.35,rely=0.35)
Radiobutton(root,text="随机",command=generate_3,variable=example,value=3).place(relx=0.42,rely=0.3)
Radiobutton(root,text="输入",command=generate_4,variable=example,value=4).place(relx=0.42,rely=0.35)

kmp = Button(text="Start KMP!", font=('FZFJK', 20),
                command=Controller.KMP,
                relief="raised"
                )
kmp.place(relx=0.6, rely=0.3)
root.mainloop()

