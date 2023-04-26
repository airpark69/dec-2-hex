import multiprocessing

def dec_to_hex(dec):
    return hex(dec)[2:]

def parallel_dec_to_hex(dec_list):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = pool.map(dec_to_hex, dec_list)
    pool.close()
    pool.join()
    return result

# TO-DO
# test code 추가할 필요 있음
dec_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
hex_list = parallel_dec_to_hex(dec_list)
print(hex_list)
