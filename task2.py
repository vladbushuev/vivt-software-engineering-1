# Определение класса Matrix для работы с матрицами
class Matrix:
    # Классовая переменная для подсчета количества объектов класса Matrix
    object_count = 0

    def __init__(self, rows=None, cols=None, value=None):
        """
        Конструктор класса Matrix.
        Может быть вызван без параметров, с одним параметром (размер, подразумевается квадратная матрица),
        или с двумя параметрами (количество строк и столбцов).
        """
        # Увеличиваем счетчик объектов при создании нового объекта
        Matrix.object_count += 1

        # Инициализируем переменную состояния без ошибок
        self.state = 0

        # Если не передано параметров, создаем матрицу 1x1 с элементом 0.0
        if rows is None and cols is None and value is None:
            try:
                self.rows = 1  # Устанавливаем количество строк
                self.cols = 1  # Устанавливаем количество столбцов
                self.data = [[0.0]]  # Инициализируем матрицу одним элементом 0.0
            except MemoryError:
                self.state = 1  # Код ошибки при нехватке памяти

        # Если передан только один параметр, создаем квадратную матрицу размером rows x rows
        elif cols is None and value is None:
            try:
                self.rows = rows  # Устанавливаем количество строк
                self.cols = rows  # Устанавливаем количество столбцов (квадратная матрица)
                # Инициализируем матрицу элементами, равными сумме индексов строки и столбца
                self.data = [[float(i + j) for j in range(self.cols)] for i in range(self.rows)]
            except MemoryError:
                self.state = 1  # Код ошибки при нехватке памяти
            except TypeError:
                self.state = 1  # Код ошибки при неверном типе параметра

        # Если переданы два параметра, создаем матрицу размером rows x cols
        else:
            try:
                self.rows = rows  # Устанавливаем количество строк
                self.cols = cols  # Устанавливаем количество столбцов
                # Если задано значение, инициализируем все элементы этим значением
                if value is not None:
                    self.data = [[float(value) for _ in range(self.cols)] for _ in range(self.rows)]
                else:
                    # Инициализируем матрицу элементами, равными сумме индексов строки и столбца
                    self.data = [[float(i + j) for j in range(self.cols)] for i in range(self.rows)]
            except MemoryError:
                self.state = 1  # Код ошибки при нехватке памяти
            except TypeError:
                self.state = 1  # Код ошибки при неверных типах параметров

    def __del__(self):
        """
        Деструктор класса Matrix. Освобождает память.
        """
        # Уменьшаем счетчик объектов при удалении объекта
        Matrix.object_count -= 1
        # Освобождаем данные матрицы
        del self.data

    def get_element(self, i, j):
        """
        Возвращает значение элемента матрицы по индексам (i, j).
        """
        # Проверяем, что индексы находятся в пределах матрицы
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.state = 0  # Сброс кода ошибки
            return self.data[i][j]  # Возвращаем значение элемента
        else:
            self.state = 2  # Код ошибки при выходе за пределы матрицы
            return None  # Возвращаем None в случае ошибки

    def get_address(self, i, j):
        """
        Возвращает адрес элемента матрицы по индексам (i, j).
        В Python понятие адреса элемента не применяется, поэтому возвращаем информацию о позиции.
        """
        # Проверяем, что индексы находятся в пределах матрицы
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.state = 0  # Сброс кода ошибки
            return (i, j)  # Возвращаем кортеж с индексами как "адрес"
        else:
            self.state = 2  # Код ошибки при выходе за пределы матрицы
            return None  # Возвращаем None в случае ошибки

    def print_matrix(self):
        """
        Печатает элементы матрицы.
        """
        print("Matrix elements:")
        for row in self.data:
            print(row)  # Печатаем каждую строку матрицы

    def __add__(self, other):
        """
        Перегрузка оператора сложения для сложения двух матриц.
        """
        # Проверяем, является ли другой объект экземпляром Matrix и совпадают ли размеры
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                try:
                    # Создаем новую матрицу для результата сложения
                    result = Matrix(self.rows, self.cols)
                    # Сложение соответствующих элементов
                    for i in range(self.rows):
                        for j in range(self.cols):
                            result.data[i][j] = self.data[i][j] + other.data[i][j]
                    return result  # Возвращаем результирующую матрицу
                except Exception:
                    # В случае исключения устанавливаем код ошибки
                    result = Matrix()
                    result.state = 1  # Код ошибки при возникновении исключения
                    return result
            else:
                # Если размеры не совпадают, устанавливаем код ошибки и возвращаем None
                self.state = 3  # Код ошибки несоответствия размерностей
                return None
        else:
            # Если другой объект не Matrix, устанавливаем код ошибки и возвращаем None
            self.state = 4  # Код ошибки неверного типа операнда
            return None

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания для вычитания двух матриц.
        """
        # Проверяем, является ли другой объект экземпляром Matrix и совпадают ли размеры
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.cols == other.cols:
                try:
                    # Создаем новую матрицу для результата вычитания
                    result = Matrix(self.rows, self.cols)
                    # Вычитание соответствующих элементов
                    for i in range(self.rows):
                        for j in range(self.cols):
                            result.data[i][j] = self.data[i][j] - other.data[i][j]
                    return result  # Возвращаем результирующую матрицу
                except Exception:
                    # В случае исключения устанавливаем код ошибки
                    result = Matrix()
                    result.state = 1  # Код ошибки при возникновении исключения
                    return result
            else:
                # Если размеры не совпадают, устанавливаем код ошибки и возвращаем None
                self.state = 3  # Код ошибки несоответствия размерностей
                return None
        else:
            # Если другой объект не Matrix, устанавливаем код ошибки и возвращаем None
            self.state = 4  # Код ошибки неверного типа операнда
            return None

    def __mul__(self, other):
        """
        Перегрузка оператора умножения для умножения матрицы на матрицу или на число.
        """
        # Умножение матрицы на число (скалярное умножение)
        if isinstance(other, (float, int)):
            try:
                # Создаем новую матрицу для результата умножения
                result = Matrix(self.rows, self.cols)
                # Умножение каждого элемента на число
                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] * other
                return result  # Возвращаем результирующую матрицу
            except Exception:
                # В случае исключения устанавливаем код ошибки
                result = Matrix()
                result.state = 1  # Код ошибки при возникновении исключения
                return result

        # Умножение матрицы на другую матрицу (матричное умножение)
        elif isinstance(other, Matrix):
            # Проверяем, можно ли умножить матрицы (число столбцов первой равно числу строк второй)
            if self.cols == other.rows:
                try:
                    # Создаем новую матрицу для результата умножения
                    result = Matrix(self.rows, other.cols, 0.0)
                    # Выполняем умножение
                    for i in range(self.rows):
                        for j in range(other.cols):
                            for k in range(self.cols):
                                result.data[i][j] += self.data[i][k] * other.data[k][j]
                    return result  # Возвращаем результирующую матрицу
                except Exception:
                    # В случае исключения устанавливаем код ошибки
                    result = Matrix()
                    result.state = 1  # Код ошибки при возникновении исключения
                    return result
            else:
                # Если размеры не соответствуют для умножения, устанавливаем код ошибки и возвращаем None
                self.state = 3  # Код ошибки несоответствия размерностей
                return None
        else:
            # Если другой объект не число и не Matrix, устанавливаем код ошибки и возвращаем None
            self.state = 4  # Код ошибки неверного типа операнда
            return None

    def __rmul__(self, other):
        """
        Перегрузка оператора умножения для умножения числа на матрицу.
        """
        return self.__mul__(other)  # Вызов метода __mul__

    @classmethod
    def get_object_count(cls):
        """
        Возвращает количество созданных объектов класса Matrix.
        """
        return cls.object_count  # Возвращаем количество объектов

    def __str__(self):
        """
        Возвращает строковое представление матрицы.
        """
        return f"Matrix(rows={self.rows}, cols={self.cols}, data={self.data}, state={self.state})"

# Функция для проверки работы класса Matrix
def test_matrix():
    # Создаем матрицу без параметров (1x1 с элементом 0.0)
    m1 = Matrix()
    print("m1:", m1)  # Печатаем m1

    # Создаем квадратную матрицу размером 3x3, элементы инициализированы суммой индексов
    m2 = Matrix(3)
    print("m2:", m2)  # Печатаем m2

    # Создаем матрицу 2x4, все элементы инициализированы значением 5.0
    m3 = Matrix(2, 4, 5.0)
    print("m3:", m3)  # Печатаем m3

    # Присваиваем значение элементу матрицы m2
    m2.data[1][1] = 10.0  # Изменяем элемент на позиции (1,1)
    print("m2 после изменения:", m2)  # Печатаем m2 после изменения

    # Получаем значение элемента из матрицы m2
    value = m2.get_element(1, 1)
    print("Значение m2[1][1]:", value)  # Печатаем полученное значение

    # Печатаем адрес элемента матрицы m2 (в данном случае кортеж индексов)
    address = m2.get_address(1, 1)
    print("Адрес m2[1][1]:", address)  # Печатаем "адрес" элемента

    # Печатаем матрицу m1
    m1.print_matrix()

    # Создаем матрицу m4 для сложения с m2
    m4 = Matrix(3)
    print("m4:", m4)  # Печатаем m4

    # Сложение матриц m2 и m4
    m5 = m2 + m4
    if m5 is not None:
        print("m5 (m2 + m4):", m5)  # Печатаем результат сложения
    else:
        print("Сложение m2 и m4 завершилось с ошибкой. Код ошибки:", m2.state)

    # Вычитание матриц m2 и m4
    m6 = m2 - m4
    if m6 is not None:
        print("m6 (m2 - m4):", m6)  # Печатаем результат вычитания
    else:
        print("Вычитание m2 и m4 завершилось с ошибкой. Код ошибки:", m2.state)

    # Умножение матриц m2 и m4 (совместимые размеры)
    # Для корректного умножения, количество столбцов m2 должно быть равно количеству строк m4
    m7 = m2 * m4
    if m7 is not None:
        print("m7 (m2 * m4):", m7)  # Печатаем результат умножения
    else:
        print("Умножение m2 и m4 завершилось с ошибкой. Код ошибки:", m2.state)

    # Умножение матрицы m2 на число 2.0
    m8 = m2 * 2.0
    if m8 is not None:
        print("m8 (m2 * 2.0):", m8)  # Печатаем результат умножения на число
    else:
        print("Умножение m2 на число завершилось с ошибкой. Код ошибки:", m2.state)

    # Умножение числа 3.0 на матрицу m2 (используя __rmul__)
    m9 = 3.0 * m2
    if m9 is not None:
        print("m9 (3.0 * m2):", m9)  # Печатаем результат умножения числа на матрицу
    else:
        print("Умножение числа на m2 завершилось с ошибкой. Код ошибки:", m2.state)

    # Печатаем количество созданных объектов Matrix
    print("Количество объектов Matrix:", Matrix.get_object_count())

    # Удаляем объект m3 и проверяем количество объектов
    del m3
    print("Количество объектов Matrix после удаления m3:", Matrix.get_object_count())

    # Попытка доступа к элементу за пределами матрицы
    invalid_value = m2.get_element(5, 5)  # Необходимо установить код ошибки
    print("Значение m2[5][5]:", invalid_value)  # Должно быть None
    print("Состояние m2 после неуспешного доступа:", m2.state)  # Должно быть 2

    # Попытка сложения матриц с несовпадающими размерами
    m10 = Matrix(2, 3)
    m11 = m2 + m10  # Должно вернуть None и установить код ошибки
    if m11 is not None:
        print("m11 (m2 + m10):", m11)
    else:
        print("Сложение m2 и m10 завершилось с ошибкой. Код ошибки:", m2.state)

# Запуск функции тестирования
if __name__ == "__main__":
    test_matrix()
