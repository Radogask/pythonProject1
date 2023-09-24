#№21-667
#Вариант 0
def reverse_string(string):
    string_list = list(string)
    start = 0
    end = len(string_list) - 1

    while start < end:
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1

    return "".join(string_list)

input_string = "Ликвидация задолженности"
reversed_string = reverse_string(input_string)
print("Новая строка:", reversed_string)