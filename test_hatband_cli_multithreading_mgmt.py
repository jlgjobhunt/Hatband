import pytest
import threading
from hatband_cli_multithreading_mgmt import ReadWriteLock

def test_read_write_lock():
    lock = ReadWriteLock()
    read_threads = []
    write_threads = []
    read_results = []
    write_results = []

    def read_func():
        lock.acquire_read()
        read_results.append(1)
        lock.release_read()

    def write_func():
        lock.acquire_write()
        write_results.append(1)
        lock.release_write()

    for _ in range(5):
        read_threads.append(threading.Thread(target=read_func))
    write_threads.append(threading.Thread(target=write_func))

    for thread in read_threads:
        thread.start()
    write_threads[0].start()
    for thread in read_threads:
        thread.join()
    write_threads[0].join()

    assert sum(read_results) == 5
    assert sum(write_results) == 1