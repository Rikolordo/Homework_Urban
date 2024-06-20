immutable_var = 1, 2.2, 3, 4, "Hello", True
# immutable_var[2]=23 Кортеж является неизменяемой ячейкой памяти для компактного хранения неизменяемых данных
print("Immutable tuple: ", immutable_var, type(immutable_var))
mutable_list = [12, 23, 'coconut']
mutable_list[1]="string"
print("Mutable list: ", mutable_list, type(mutable_list))
