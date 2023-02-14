pool_capacity = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours_absent = float(input())

pool_fill = first_pipe_debit * hours_absent + second_pipe_debit * hours_absent
fill_percentage = pool_fill / pool_capacity * 100
first_pipe_percentage = (first_pipe_debit * hours_absent)/pool_fill * 100
second_pipe_percentage = (second_pipe_debit * hours_absent)/ pool_fill * 100

if pool_fill <= pool_capacity:
    print(f"The pool is {fill_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    print(f"For {hours_absent:.2f} hours the pool overflows with {(pool_fill - pool_capacity):.2f} liters.")
    