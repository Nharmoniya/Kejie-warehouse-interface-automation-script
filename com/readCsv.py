import csv
import os


class READCSV():
    def __init__(self,file='testdata.csv'):
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.file = os.path.join(path, 'conf', file)
        print(self.file)

    def readAll(self, start, end):
        res = []
        with open(self.file, 'r') as f:
            data = csv.reader(f)
            for i in data:
                # print(i)
                res.append(i)
            print(res[start:end])
            return res

    def readRow(self, i=1):
        with open(self.file, 'r') as f:
            data = csv.reader(f)
            res = list(data)
            print(res[i])

    def readLine(self, i=1):
        with open(self.file, 'r') as f:
            data = csv.reader(f)
            for line in data:
                print(line[i])


if __name__ == '__main__':
    cs = READCSV()
    cs.readAll(1,7)
    all =READCSV(file='update_goods_data.csv')
    all.readAll(1,7)
