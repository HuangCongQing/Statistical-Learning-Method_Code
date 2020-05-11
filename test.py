'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-05-05 22:31:57
@LastEditors: HCQ
@LastEditTime: 2020-05-05 23:00:31
'''
distList = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(distList)
topKList=[1, 4,5 ]
for index in topKList:
        #trainLabelMat[index]：在训练集标签中寻找topK元素索引对应的标记
        #int(trainLabelMat[index])：将标记转换为int（实际上已经是int了，但是不int的话，报错）
        #labelList[int(trainLabelMat[index])]：找到标记在labelList中对应的位置
        #最后加1，表示投了一票
        print(index)
