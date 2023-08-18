class SuperList(list):
    def __init__(self, arg):
        super().__init__(arg)

    def __len__(self):
        return 1000


my_s_list = SuperList([1, 2, 3])
print(len(my_s_list))
print(my_s_list)
my_s_list.append(33)
print(my_s_list)
print(len(my_s_list))
