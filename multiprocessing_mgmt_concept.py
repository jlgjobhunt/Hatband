# Joshua Greenfield (j.l.g.jobhunt@gmail.com)
# 
# I have come to enjoy this approach to handing multiprocessing since Fall 2024,
# when this is what I came up with as an every hammer for most nails 
# and screws (eyeroll).
# This is the multiprocessing example where the work to be done goes through a work 
# divider that divides the work and then pipes it to a new process where the 
# calculation is done. Once the calculation is done in the other python process, the 
# answer is piped back to the main process connection, where it is combined before 
# being output.
#
# Experiment in multiprocessing such that an array was enumerated with a generator 
# called by multiple forked processes (10) enumerated from a worker process dividing 
# the work and returning the output to a single array.

from multiprocessing import Process, Pipe
import math

def generate_list(beginning: int, end: int) -> list:
    output = []
    for i in range(beginning, end):
        output.append(i)
    return output

def other_process(connection, beginning: int, end: int):
    output = generate_list(beginning, end)
    connection.send(output)
    connection.close()

def work_divider(connection, beginning: int, end: int):
    if beginning == 0:
        length = end + 1
    elif beginning >= 1:
        length = end - beginning

    if length > 10 and length % 10 == 0:
        worker_count = math.ceil(length / 10)
    else:
        worker_count = 1
    
    processes = dict()
    wd_cons = [0]
    op_cons = [0]
    combined = []
    for i in range(1, worker_count + 1):
        wd, op = Pipe()
        wd_cons.append(wd)
        op_cons.append(op)
        processes.update({i: Process(target=other_process, args=(op_cons[i], beginning, beginning + 10))})
        processes[i].start()
        combined.extend(wd_cons[i].recv())
        if i > 0:
            beginning += 10

    for i in range(1, worker_count + 1):
        processes[i].join()

    connection.send(combined)
    connection.close()
    

if __name__ == '__main__':
    main_connection, other_connection = Pipe()
    beginning = 1
    end = 101
    other = Process(target=work_divider, args=(other_connection, beginning, end))
    other.start()
    combined = main_connection.recv()
    other.join()
    print(f'This array came from multiple processes forked from a worker process forked from the main process:\n{combined}')
