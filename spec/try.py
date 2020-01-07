# try:
#     n = 1
#     try:
#         s = 's' > 1
#     except:
#         print('inner')
#         raise Exception('from inner')
#     finally:
#         print('ok')
# except:
#     print('outer')
# finally:
#     print('The End')
#
#






# try:
#
#     txt = input('введите что-нибудь: ')
#     num = int(txt)
# except (EOFError, KeyboardInterrupt)as e:
#     if type(e) == EOFError:
#         print('Вы сделали мне EOF')
#     else:
#         print('Отмена операции')
# except ValueError as e:
#     print(f"ошибка {e}")
# except:
#     print('Что то случилов')
# else: #выполняется только если в трай нет ошибки
#     print(f'Вы ввели: {txt}')
# finally: #выполняется в любом случае
#     print('The End')
# try:
#     age = input('Введите свой возраст: ')
#     age = int(age)
#     if age < 18:
#         raise Exception('Не походите по возрасту') #бросаем исключение
#     print('Все хорошо')
# except (EOFError, KeyboardInterrupt)as e:
#     if type(e) == EOFError:
#         print('Вы сделали мне EOF')
#     else:
#         print('Отмена операции')
# except ValueError as e:
#     print(f"ошибка {e}")
# except Exception as e:
#     print('Возраст не подхоидт')
# except:
#     print('Что то случилов')
# else: #выполняется только если в трай нет ошибки
#     print(f'Вы ввели:')
# finally: #выполняется в любом случае
#     print('The End')
    # long = 20
    # short = 2
    # total = long*3 + shodrt * 2
    # x = 'a' > 1
    # print(total)


# except (NameError, TypeError):
# # except NameError:
#     print('Name Error')
# except TypeError:
#     print('Type Error')
# print('The end')

# def one():
# #     s = 'a' + 'b'
# #     raise Exception('Test')
# # def two():
# #     n = 'a' > 1
# # def three():
# #     pass
# #
# # try:
# #     one()
# #     two()
# #     three()
# # except:
# #     print('!!!')

# def a():
#     b()
# def b():
#     d()
#     if True:
#         raise Exception('Ошибка в b')
# def d():
#     # if True:
#     #     raise Exception('Ошибка в d')
#     pass
#
#
# try:
#     x = a()
# except Exception as e:
#     print(e)
# except:
#     print('!!!')