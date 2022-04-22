import os
import random


def gene_file(name, length):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(path)
    filename = os.path.join(path, 'datas', name)
    print(filename)
    lis = ["我", "是", "中", "国", "人", "a", "b", "c"]
    with open(filename, 'w', encoding='uft-8') as f:
        for i in range(length):
            rand = random.randint(0, len(lis) - 1)
            f.write(lis[rand])


gene_file("备注.txt", 300)
