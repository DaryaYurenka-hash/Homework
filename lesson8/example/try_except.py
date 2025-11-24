a = '13'

# # raise ValueError("13 нельзя")

# int(a)
# b = 1/0


try:
    a = int(a)
    # a = a/0
    if a == 13:
        # raise ValueError("13 нельзя")
        raise KeyError("13 нельзя")
    
except ZeroDivisionError:
    print('--err0--')
except ValueError:
    print("--err2--")
except Exception as e:
    print('---err3---')
    print(e)
    print(e.with_traceback)

else:
    # выполняется когда в try не было ошибок
    print('no err')

finally:
    # выполняется всегда
    print('all')


# print('ok')


# while 1:
#     a = input("...: ")
#     try:
#         a = int(a)
#         break
#     except:
#         print('errr')

# print(a*10)
