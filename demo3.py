import demo3 as np
# import matplotlib as mp
import time
ls=[i for i in range(1000)]
# print(ls)
star =time.time()
sum(ls)
end = time.time()
print("列表求和时间为：{}".format(end-star))

np.array(ls)
star =time.time()
sum(ls)
end = time.time()
print("列表求和时间为：{}".format(end-star))