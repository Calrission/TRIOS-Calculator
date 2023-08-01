operations = input("Enter operations ('+' '-'  '*'  '/') separated by a space: ").split(" ")
nums = list(map(int, input("Enter numbers separated by spaces: ").split(" ")))
target = int(input("Enter target num: "))

def next_operation(lost_operations, lost_numbers, eval_str) -> str:
    global target
    if len(lost_operations) == 0 and len(lost_numbers) == 0:
        eval_ = eval(eval_str)
        if eval_ == target:
            return eval_str

    for new_operation in lost_operations:
        new_lost_operations = lost_operations[::]
        new_lost_operations.remove(new_operation)

        eval_expression = eval_str + new_operation
        for new_num in lost_numbers:
            new_eval_str = f"({eval_expression + str(new_num)})"

            new_lost_nums = lost_numbers[::]
            new_lost_nums.remove(new_num)

            res = next_operation(new_lost_operations, new_lost_nums, new_eval_str)
            if res is not None:
                return res


for num in nums:
    new_nums = nums[::]
    new_nums.remove(num)
    result = next_operation(operations, new_nums, str(num))
    if result is not None:
        print(result)
        break