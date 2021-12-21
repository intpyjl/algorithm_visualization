import cv2
import numpy as np
import time
class Visual:
    data = []
    height = 500
    scale = 0
    unit_width = 20
    Max_value = 0
    inter_dis = 5
    inter_time = 100
    time_table=[100,40,30,20,10,7,5,3,2,1]
    name = ""
    figure = None
    UN_FINISH = (225,105,65)
    CHANGE=(0,69,255)
    blank = (255, 255, 255)
    sort_line=(19,69,139)
    FINISH = ()
    fontScale=1
    time_start=0
    priot=-1
    def __init__(self, Data, Name,Speed):
        self.Max = max(Data)
        self.data = Data
        self.scale = 0.75 * self.height / self.Max
        self.name = Name
        self.inter_time=self.time_table[Speed-1]
    def start(self):
        self.time_start = time.time()
        n = len(self.data)
        self.figure = np.zeros((self.height, n * (self.unit_width + self.inter_dis), 3), dtype=np.uint8) + 255
        cv2.namedWindow(self.name, 0)
        cv2.resizeWindow(self.name, min(n * (self.unit_width + self.inter_dis),1000), 400)
        cv2.moveWindow(self.name, 100, 330)
        for i in range(n):
            self.set_figure(i, self.data[i], self.UN_FINISH)
        self.show()
        if self.name == "bubble":
            self.Bubble()
        if self.name == "qsort":
            self.Qsort(0, n-1)
        if self.name == "choose":
            self.Choose()
        if self.name == "merge":
            self.height=int(self.height/2)
            self.Merge(self.data, 0, n - 1)
        pass

    def setValue(self, index, val, color=(0, 0,)):
        self.data[index] = val
        self.set_figure(index, val, color)
        self.show()
    def display(self,cart):
        for i in cart:
            self.set_figure(i, self.data[i], color=self.CHANGE)
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
    def half_display(self,cart):
        color=self.CHANGE
        for i in cart:
            index = i
            val = self.data[i]
            leftX = index * (self.unit_width + self.inter_dis)
            rightX = leftX + self.unit_width
            Y = int(-self.scale * val-1)
            self.figure[self.height:Y, leftX:rightX] = self.blank
            self.figure[Y:, leftX:rightX] = color
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
    def half_normal(self,cart):
        color = self.UN_FINISH
        for i in cart:
            index = i
            val = self.data[i]
            leftX = index * (self.unit_width + self.inter_dis)
            rightX = leftX + self.unit_width
            Y = int(-self.scale * val - 1)
            self.figure[Y:, leftX:rightX] = color
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
    def normal(self,cart):
        for i in cart:
             self.set_figure(i, self.data[i], color=self.UN_FINISH)
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
    def swap(self, i, j):
        if i == j:
            return
        self.set_figure(i, self.data[i], color=self.CHANGE)
        self.set_figure(j, self.data[j], color=self.CHANGE)
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.set_figure(i, self.data[i], color=self.CHANGE)
        self.set_figure(j, self.data[j], color=self.CHANGE)
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
        self.set_figure(i, self.data[i], color=self.UN_FINISH)
        self.set_figure(j, self.data[j], color=self.UN_FINISH)
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        self.show()
    def set_figure(self, index=0, val=0, color=(0, 0, 0)):
        leftX = index * (self.unit_width + self.inter_dis)
        rightX = leftX + self.unit_width
        Y = int(-self.scale * val - 1)
        self.figure[:Y, leftX:rightX] = self.blank
        self.figure[Y:, leftX:rightX] = color
        if self.priot>=0:
            self.draw()
    def set_high(self,index=0,val=0,color=(0,0,0)):
        leftX = index * (self.unit_width + self.inter_dis)
        rightX = leftX + self.unit_width
        Y=int(-self.scale*val-1-self.height)
        self.figure[:Y, leftX:rightX] = self.blank
        self.figure[Y:self.height, leftX:rightX] = color
    def show(self, flag=False):
        cv2.imshow(self.name, self.figure)
        if flag is False:
            cv2.waitKey(self.inter_time)
        else:
            cv2.waitKey(0)
    def draw(self):
        Y = int(-self.scale * self.priot - 1)
        self.figure[Y - 1:Y] = self.sort_line
        if cv2.getWindowProperty(self.name, 0) < 0:
            cv2.destroyAllWindows()
            return
        cv2.imshow(self.name, self.figure)
    def finish(self):
        time_end = time.time()
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 70)
        fontColor = (0,0,0)
        lineType = 2
        cv2.putText(self.figure, 'time='+str(round(time_end-self.time_start,2)),
                    bottomLeftCornerOfText,
                    font,
                    self.fontScale,
                    fontColor,
                    lineType)
        self.show(flag=True)
    def Bubble(self):
        n = len(self.data)
        for i in range(n):
            last = n - i - 1
            if last > 0:
                for j in range(last):
                    self.display([j,j+1])
                    if (self.data[j] > self.data[j + 1]):
                        self.swap(j, j + 1)
                    else:
                        self.normal([j,j+1])

    def Qsort(self, left, right):
        if left < right:
            i = left
            j = right
            self.priot = self.data[i]
            self.draw()
            while i != j:
                while j > i and self.data[j] > self.priot:
                    self.display([j])
                    self.normal([j])
                    j -= 1
                if j > i:
                    self.swap(i, j)
                    i += 1
                while i < j and self.data[i] < self.priot:
                    self.display([i])
                    self.normal([i])
                    i += 1
                if j > i:
                    self.swap(i, j)
                    j -= 1
            Y = int(-self.scale * self.priot - 1)
            self.figure[Y - 1:Y,:] = self.blank
            if cv2.getWindowProperty(self.name, 0) < 0:
                cv2.destroyAllWindows()
                return
            self.priot=-1
            for t in range(len(self.data)):
                self.set_figure(t, self.data[t], self.UN_FINISH)
            self.show()
            cv2.imshow(self.name, self.figure)
            self.Qsort(left, i - 1)
            self.Qsort(i + 1, right)

    def Choose(self):
        n = len(self.data)
        for i in range(n - 1):
            min = 1000
            index = i
            for j in range(i, n):
                self.display([j])
                if self.data[j] < min:
                    min = self.data[j]
                    index = j
                self.normal([j])
            self.swap(i, index)
    def Merge(self, x, left, right):
        if len(x) <= 1:
            return x
        mid = int(len(x) / 2)
        results = []
        L = self.Merge(x[:mid], left, left+mid - 1)
        R = self.Merge(x[mid:], left+mid, right)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            self.half_display([left+i,left+mid+j])
            if (L[i] < R[j]):
                results.append(L[i])
                self.set_high(left + k, L[i], color=self.UN_FINISH)
                if cv2.getWindowProperty(self.name, 0) < 0:
                    cv2.destroyAllWindows()
                    break
                self.show()
                self.half_normal([left + i, left+mid + j])
                i += 1
            else:
                results.append(R[j])
                self.set_high(left + k, R[j], color=self.UN_FINISH)
                if cv2.getWindowProperty(self.name, 0) < 0:
                    cv2.destroyAllWindows()
                    break
                self.show()
                self.half_normal([left + i, left+mid + j])
                j += 1

            k += 1
        if i == len(L):
            while (j < len(R)):
                self.half_display([left+mid + j])
                results.append(R[j])
                self.set_high(left + k, R[j], color=self.UN_FINISH)
                if cv2.getWindowProperty(self.name, 0) < 0:
                    cv2.destroyAllWindows()
                    break
                self.show()
                self.half_normal([left+mid+j])
                j += 1
                k += 1
        if j == len(R):
            while (i < len(L)):
                self.half_display([left + i])
                results.append(L[i])
                self.set_high(left + k, L[i], color=self.UN_FINISH)
                if cv2.getWindowProperty(self.name, 0) < 0:
                    cv2.destroyAllWindows()
                    break
                self.show()
                self.half_normal([left+i])
                i += 1
                k += 1
        for j in range(len(x)):
            self.data[j+left]=results[j]
            self.set_figure(j+left,results[j],color=self.UN_FINISH)
            if cv2.getWindowProperty(self.name, 0) < 0:
                cv2.destroyAllWindows()
                break
            self.show()
        return results
