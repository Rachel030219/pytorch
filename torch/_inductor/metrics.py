# counter for tracking how many kernels have been generated
generated_kernel_count = 0
generated_cpp_vec_kernel_count = 0


# reset all counters
def reset():
    global generated_kernel_count
    global generated_cpp_vec_kernel_count

    generated_kernel_count = 0
    generated_cpp_vec_kernel_count = 0
