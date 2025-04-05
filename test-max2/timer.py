# Apr-05-2025
# timer.py

import time

global timer_start


def init_timer():
    global timer_start
    timer_start = time.time()


def show_elapsed_time_sec():
    global timer_start
    timer_end = time.time()
    seconds = round((timer_end - timer_start), 3)
    print(f'\nElapsed time = {seconds} sec\n')


def show_elapsed_time_min_sec():
    global timer_start
    timer_end = time.time()
    seconds = int(timer_end - timer_start)
    m, s = divmod(seconds, 60)
    print(f'\nElapsed time = {m:02d} min  {s:02d} sec\n')


def show_elapsed_time_hour_min_sec():
    global timer_start
    timer_end = time.time()
    seconds = int(timer_end - timer_start)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print(f'\nElapsed time = {h:02d} hour(s)  {m:02d} min  {s:02d} sec\n')


def get_elapsed_time_sec():
    global timer_start
    timer_end = time.time()
    seconds = timer_end - timer_start
    return seconds


def get_elapsed_time_min_sec():
    global timer_start
    timer_end = time.time()
    seconds = int(timer_end - timer_start)
    m, s = divmod(seconds, 60)
    return m, s


def get_elapsed_time_hour_min_sec():
    global timer_start
    timer_end = time.time()
    seconds = int(timer_end - timer_start)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s


def save_elapsed_time_hour_min_sec(path_time):
    global timer_start
    timer_end = time.time()
    seconds = int(timer_end - timer_start)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    string_time = f'Elapsed time = {h:02d} hour(s)  {m:02d} min  {s:02d} sec\n'
    with open(path_time, 'w') as fp:
        fp.write(string_time)
    print(f'\nElapsed time = {h:02d} hour(s)  {m:02d} min  {s:02d} sec')
