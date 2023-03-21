for _ in range(int(input())):
    str_arr = input().split()
    int_arr = [int(num) for num in str_arr]
    user_response = sum_array(int_arr)  # type: ignore
    print("{STDOUT_PREFIX}", user_response)
