my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    number_ = my_list[count]
    count = count + 1
    if count == len(my_list):
        print(number_)
    elif number_ == 0:
        continue
    elif number_ < 0:
        break
    else:
        print(number_)
