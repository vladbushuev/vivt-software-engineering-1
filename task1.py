# Импортируем необходимый модуль для глубокого копирования
import copy


class Vector:
    # Классовая переменная для подсчета количества объектов
    object_count = 0

    def __init__(self, size=None, value=None):
        """
        Конструктор класса Vector.
        Может быть вызван без параметров, с одним параметром (размер) или с двумя параметрами (размер и значение).
        """
        # Увеличиваем счетчик объектов при создании нового объекта
        Vector.object_count += 1

        # Инициализируем переменную состояния без ошибок
        self.state = 0

        # Если не передано параметров, выделяем место для одного элемента и инициализируем его в ноль
        if size is None and value is None:
            try:
                self.size = 1  # Устанавливаем размер вектора
                self.data = [0.0]  # Инициализируем единственный элемент вектора нулем
            except MemoryError:
                self.state = 1  # Устанавливаем код ошибки при нехватке памяти

        # Если передан только размер, выделяем место и инициализируем элементами их индексами
        elif value is None:
            try:
                self.size = size  # Устанавливаем размер вектора
                self.data = [float(i) for i in range(size)]  # Инициализируем элементы индексами
            except MemoryError:
                self.state = 1  # Устанавливаем код ошибки при нехватке памяти
            except TypeError:
                self.state = 1  # Устанавливаем код ошибки при неверном типе параметра

        # Если переданы размер и значение, выделяем место и инициализируем всеми элементами заданным значением
        else:
            try:
                self.size = size  # Устанавливаем размер вектора
                self.data = [float(value) for _ in range(size)]  # Инициализируем элементы заданным значением
            except MemoryError:
                self.state = 1  # Устанавливаем код ошибки при нехватке памяти
            except TypeError:
                self.state = 1  # Устанавливаем код ошибки при неверных типах параметров

    def __del__(self):
        """
        Деструктор класса Vector. Освобождает память.
        """
        # Уменьшаем счетчик объектов при удалении объекта
        Vector.object_count -= 1
        # Освобождаем данные
        del self.data

    def assign(self, index, value=0.0):
        """
        Присваивает элементу массива некоторое значение.
        По умолчанию значение равно 0.0.
        """
        # Проверяем, не выходит ли индекс за пределы массива
        if 0 <= index < self.size:
            self.data[index] = float(value)  # Присваиваем значение элементу
            self.state = 0  # Сбрасываем код ошибки
        else:
            self.state = 2  # Устанавливаем код ошибки при выходе за пределы массива

    def get(self, index):
        """
        Возвращает значение элемента массива по заданному индексу.
        """
        # Проверяем, не выходит ли индекс за пределы массива
        if 0 <= index < self.size:
            self.state = 0  # Сбрасываем код ошибки
            return self.data[index]  # Возвращаем значение элемента
        else:
            self.state = 2  # Устанавливаем код ошибки при выходе за пределы массива
            return None  # Возвращаем None при ошибке

    def print_vector(self):
        """
        Печатает элементы вектора.
        """
        print("Vector elements:", self.data)  # Выводим элементы вектора

    # Определение операции сложения с float
    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Создаем новый вектор как копию текущего
            result = Vector(self.size)
            result.data = [x + other for x in self.data]  # Складываем каждый элемент с other
            return result  # Возвращаем новый вектор
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    # Определение операции вычитания с float
    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Создаем новый вектор как копию текущего
            result = Vector(self.size)
            result.data = [x - other for x in self.data]  # Вычитаем из каждого элемента other
            return result  # Возвращаем новый вектор
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    # Определение операции умножения с float
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Создаем новый вектор как копию текущего
            result = Vector(self.size)
            result.data = [x * other for x in self.data]  # Умножаем каждый элемент на other
            return result  # Возвращаем новый вектор
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    # Определение метода сравнения "больше"
    def __gt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Сравниваем каждый элемент с other
            return all(x > other for x in self.data)
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    # Определение метода сравнения "меньше"
    def __lt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Сравниваем каждый элемент с other
            return all(x < other for x in self.data)
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    # Определение метода сравнения "меньше или равно"
    def __le__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            # Сравниваем каждый элемент с other
            return all(x <= other for x in self.data)
        else:
            return NotImplemented  # Если тип не поддерживается, возвращаем NotImplemented

    @classmethod
    def get_object_count(cls):
        """
        Возвращает количество созданных объектов класса Vector.
        """
        return cls.object_count  # Возвращаем количество объектов

    def __str__(self):
        """
        Возвращает строковое представление вектора.
        """
        return f"Vector(size={self.size}, data={self.data}, state={self.state})"


# Функция для проверки работы класса Vector
def test_vector():
    # Создаем вектор без параметров
    v1 = Vector()
    print("v1:", v1)  # Печатаем v1

    # Создаем вектор с одним параметром (размер)
    v2 = Vector(5)
    print("v2:", v2)  # Печатаем v2

    # Создаем вектор с двумя параметрами (размер и значение)
    v3 = Vector(3, 7.5)
    print("v3:", v3)  # Печатаем v3

    # Присваиваем значение элементу вектора v2
    v2.assign(2, 10.0)
    print("v2 после присваивания:", v2)  # Печатаем v2 после изменения

    # Получаем значение элемента из вектора v2
    value = v2.get(2)
    print("Значение v2[2]:", value)  # Печатаем полученное значение

    # Печатаем вектор v1
    v1.print_vector()

    # Выполняем операции сложения, вычитания и умножения
    v4 = v2 + 5.0
    print("v4 (v2 + 5.0):", v4)

    v5 = v2 - 2.0
    print("v5 (v2 - 2.0):", v5)

    v6 = v2 * 3.0
    print("v6 (v2 * 3.0):", v6)

    # Сравниваем векторы с числом
    print("v2 > 5.0:", v2 > 5.0)  # Проверяем, все ли элементы v2 больше 5.0
    print("v2 < 15.0:", v2 < 15.0)  # Проверяем, все ли элементы v2 меньше 15.0
    print("v2 <= 10.0:", v2 <= 10.0)  # Проверяем, все ли элементы v2 меньше или равны 10.0

    # Печатаем количество созданных объектов
    print("Количество объектов Vector:", Vector.get_object_count())

    # Удаляем объект v3 и проверяем количество объектов
    del v3
    print("Количество объектов Vector после удаления v3:", Vector.get_object_count())


# Вызываем функцию тестирования
if __name__ == "__main__":
    test_vector()
