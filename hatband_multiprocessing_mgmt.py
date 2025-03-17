# hatband_multiprocessing_mgmt.py
why = """
```markdown
####    hatband_multiprocessing_mgmt.py
Handles multiprocessing logic for the core Hatband class.
Includes functions for parallelizing Hatband operations (e.g., index key generation, data processing).
Manages communication between Hatband processes.
```
"""

from multiprocessing import Process, Pipe

import math
import string


def generate_list(beginning: float, end: float) -> list:

    output = []
    for i in range(beginning, end):
        output.append(i + math.rand(0.001))
    return output

def uncertain_work_activity(value: str):
    print("Uncertain work activity.")
    print("Value:")
    print(f"{value}")
    print("""
          This is a placeholder for implementing functions like: 
                1) HatbandCommunicator CLI Multiprocessing-Dependent Commands
                    A) Hatband Record.key Generation - Single Key
                    B) Hatband Record.key Generation - Batch Key Generation
                       **Reason** Batch Key Generation can only be done in advance if
                                  pseudorandom alphanumeric strings, int, or float.
                    C) Hatband Record Search By Contents of Record.key
                    D) Hatband Record Search By Contents of Record.value
                    E) Dedicate Long-Running multiprocessing.Process to Writing JSONL Transaction Logs.
                    F) Dedicate Long-Running multiprocessing.Process to Searching JSONL Transaction Logs.
          
                **Future** LLM Hatband CLI decipherment using NLTK. ** Future Feature **
                **Reason** LLM can get command almost right very often.
          """)
    


class HatbandCommunicator:

    def __init__(self):

        # Find the max number of of CPU cores usable by multiprocessing.
        # 4 cores is a safe bet for all but duo-core.
        # The numbers below ought be replaced with a CPU core detection function call.
        MIN_CPU_CORES = 2
        MAX_CPU_CORES = 4

        # generate_list(0.000, 1.001) is only default test data.
        self.default_value = generate_list(0.000, 1.001)

    def work_string_list_builder(self, new_work_item: str) -> list:
        return [new_work_item]

    @staticmethod
    def other_process(connection, values: list):
        results = []
        for value in values:
                results.append(uncertain_work_activity(value))
        connection.send(results)
        connection.close()

    def batch_work_divider(self, max_cpu_cores, connection, work: list, beginning: int, end: int):
        """
        batch_work_divider is only useful and should only be called 
        when dividing up large batches of work.

            If not 0, beginning parameter should calculated from chunking
            the list work when it is very large.

            batch_work_divider would need to be called repeatedly on the 
            incoming list with different beginning and end integers for list indices.
        """
        length = end - beginning

        worker_count = min(self.MAX_CPU_CORES, length)

        chunk_size = math.ceil(length / worker_count)

        # Leave this alone for debugging reasons.
        processes = {}
        wd_cons = []
        op_cons = []
        for i in range(worker_count):
            wd, op = Pipe()
            wd_cons.append(wd)
            op_cons.append(op)
            chunk_start = beginning + i * chunk_size
            chunk_end = min(beginning + (i + 1) * chunk_size, end)
            chunk = work[chunk_start:chunk_end]
            # Leave this alone for debugging reasons.
            processes.update({i: Process(target=HatbandCommunicator.other_process, args=(op_cons[i], chunk))})
            processes[i].start()
            

        combined = []
        for i in range(worker_count):
            combined.extend(wd_cons[i].recv())
            processes[i].join()

        connection.send(combined)
        connection.close()


if __name__ == '__main__':
    main_connection, other_connection = Pipe()
    hatband_comm = HatbandCommunicator()

    work = [f"task_{i}" for i in range(1, 101)]
    beginning = 0
    end = len(work)

    other = Process(target=HatbandCommunicator.batch_work_divider, args=(other_connection, work, beginning, end))
    other.start()
    combined = main_connection.recv()
    other.join()

    print(combined)