
def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attr for attr  in dir(obj) if callable(getattr(obj, attr))]
    
    # Получение методов объекта

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    # Создание словаря с информацией об объекте
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}


    return info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Sergey')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'Karasev'])
print(list_info)