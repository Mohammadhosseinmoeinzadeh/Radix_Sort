def get_word_ascii_codes(text):
    words = text.split()
    word_count = len(words)
    word_ascii_codes = [[] for _ in range(word_count)]

    for i, word in enumerate(words):
        ascii_codes = [ord(char) for char in word]
        word_ascii_codes[i] = ascii_codes

    return word_ascii_codes


input_text = input("لطفاً متن را وارد کنید: ")

word_ascii_codes = get_word_ascii_codes(input_text)

output_list = []

for i, codes in enumerate(word_ascii_codes):
    output_list.append(codes)

print("لیست حاوی کدهای ASCII برای هر کلمه:")
print(output_list)

#---------------------------------------------------------------------------
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i][0] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i][0] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(max(sublist) for sublist in arr)

    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# لیست اصلی
my_list = output_list

# مرتب‌سازی لیست بر اساس خانه اول هر لیست
radix_sort(my_list)
print("کد های مرتب شده بر اساس خانه اول هر لیست:")
print(my_list)



#---------------------------------------------------------------------------



def convert_nested_ascii_to_text(nested_list):
    text_list = []
    for sublist in nested_list:
        text = ''.join(chr(code) for code in sublist)
        text_list.append(text)
    return text_list


# ورودی: لیست چند بعدی حاوی کدهای ASCII
input_list = my_list

# تبدیل کدهای ASCII به متن
output_list = convert_nested_ascii_to_text(input_list)

# چاپ لیست حاوی متن تبدیل شده
print("لیست تبدیل شده به متن:")
print(output_list)
