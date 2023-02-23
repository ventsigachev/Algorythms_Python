list_ = [1, 2, 3, 4, 5]
last_ind = len(list_) - 1

for ind in range(len(list_) // 2):
    list_[ind], list_[last_ind - ind] = list_[last_ind - ind], list_[ind]

print(list_)
