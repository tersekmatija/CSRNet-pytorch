import glob
import random

trains = glob.glob("/home/matijamasaibb/codesmatijamasa/CSRNet-pytorch/data/ShanghaiA/train_data/images/*.jpg")
tests = glob.glob("/home/matijamasaibb/codesmatijamasa/CSRNet-pytorch/data/ShanghaiA/test_data/images/*.jpg")

random.shuffle(trains)

import json

n = round(len(trains)*0.8)
print(n)

with open('part_A_train.json', 'w') as f:
  json.dump(trains[0:n], f)

with open('part_A_val.json', 'w') as f:
  json.dump(trains[n:], f)

with open('part_A_test.json', 'w') as f:
  json.dump(tests, f)