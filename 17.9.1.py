x = input('ведите последовательность чисел через пробел: ')
element = int(input('Введите число: '))
sequence = []

def check_sequence(x):
    s = x.split()
    for i in s:
        try:
            i = int(i)
        except Exception:
            return print('Вводите только целые числа')
        else:
            sequence.append(i)
    return sequence
    
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
    
def search_list(array, element, left, right):
    if left > right:
        return False
    
    middle = (left + right) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return search_list(array, element, left, middle-1)
    else:
        return search_list(array, element, middle+1, right)

def len_sequence(x):
    seq = len(sequence)
    return seq-1

  
check_element = search_list(insertionSort(check_sequence(x)), element, 0, len_sequence(x))
print(check_element)
