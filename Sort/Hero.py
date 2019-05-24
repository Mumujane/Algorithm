class Hero:
    def __init__(self, name):
        #print('__init__方法被调用')
        self.name = name

    def __del__(self):
        print("__del__方法被调用")
        print("%s 被 GM 干掉了..." % self.name)

del Hero
X = Hero("呵呵")
del Hero

del(X)
#print(type(Hero))

#del Hero



# #
# class Hero:
#     def eat(self):
#         print("吃饭吧")
#
#     def __del__(self):
#         print("删除__")
#
#     def fly(self):
#         pass
#
#
# print(id(Hero))
# hero = Hero()
# del Hero
#
# print("结束")
