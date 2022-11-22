import utils
import pandas as pd
import cv2 
from scipy.spatial import distance
import re


def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s
def get_sum_distance(x,**kwargs):
    top = kwargs["kwargs"]["top"]
    bot = kwargs["kwargs"]["bot"]
    bc =(x[0],x[1])
    tc =(x[0],x[1]-150)
    a = distance.euclidean(top,bc)
    b = distance.euclidean(bot,tc)
    return a+b
class procedure_data:
    def __init__(self, path_data = "DSHS.xlsx"):
        self.data = pd.read_excel(path_data,index_col = "STT")
        # print(self.data.head(10))
        # self.data["Có mặc"] = "y"
        self.data["absent"] = 1

    def get_out(self,x1,y1,x2,y2):

        data_copy = self.data.copy()
        data_copy["result"] = data_copy[["X","Y"]].apply(get_sum_distance, kwargs = {"top":(x1,y1),"bot":(x2,y2)},axis=1)
 
        out = data_copy[data_copy["result"] == data_copy["result"].min()]
        name = out["Tên"].values[0]

        name = no_accent_vietnamese(name).replace(" ", "_")


        self.data["absent"].values[int(out.index[0])-1] = 0

        return name
    def to_excel(self):
        self.data.to_excel("Result/Diemdanh.xlsx")
        