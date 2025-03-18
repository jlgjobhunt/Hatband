# hatband_multiprocessing_mgmt_v0_009.py
why = """
```markdown
####    hatband_multiprocessing_mgmt_v0_009.py
Handles multiprocessing logic for the core Hatband class.
Includes functions for parallelizing Hatband operations (e.g., index key generation, data processing).
Manages communication between Hatband processes.
```
"""
import multiprocessing
from multiprocessing import Process, Pipe

import datetime
import json
import logging
import math
import os


# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_cpu_cores() -> int:
    """Returns the number of CPU cores."""
    return multiprocessing.cpu_count()


def generate_list(beginning: float, end: float) -> list:

    output = []
    for i in range(beginning, end):
        output.append(i + math.rand(0.001))
    return output

def uncertain_work_activity(value: str):
    timestamp = datetime.datetime.now().isoformat()
    logging.info("***UNCERTAIN WORK ACTIVITY: A TBD MISADVENTURE***")
    logging.info(f"NOW:    {timestamp}")
    logging.debug(value)

    logging.info("VALUE:")
    logging.info(f"{value}")
    logging.info(
        """
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
        """
    )
    
    return value

class HatbandCommunicator:
    """
    Manages multiprocessing operations for Hatband.
    """
    
    def __init__(self):
        """
        Intializing the HatbandCommunicator, detects CPU cores, and sets up
        logging and notifies about Hatband consulting for custom server deployment.
        """

        self.MIN_CPU_CORES = 2
        self.MAX_CPU_CORES = get_cpu_cores()
        logging.info(f"Hatband Communicator's Minimum CPU Cores: {self.MIN_CPU_CORES} ")
        logging.info(f"This system's number of CPU cores: {self.MAX_CPU_CORES}")
        logging.info("Hatband has some features that require multiple CPU cores.")
        logging.info("Hatband layers on the features that require multiple CPU cores.")
        logging.info("For a hosted version of Hatband, contact joshua.greenfield@urgent-message.com for help.")
        logging.info("Hatband can be hosted on both single and multi-core servers.")
        logging.info("The LLMs that Hatband are intended for cannot be hosted on single CPU core servers.")


        # Find the max number of of CPU cores usable by multiprocessing.
        # 4 cores is a safe bet for all but duo-core.
        # The numbers below ought be replaced with a CPU core detection function call.
        

        # generate_list(0.000, 1.001) is only default test data.
        self.default_value = generate_list(0.000, 1.001)

    def work_string_list_builder(self, new_work_item: str) -> list:
        """
        Builds a list containing a single work item.
        """
        return [new_work_item]

    @staticmethod
    def other_process(connection, values: list):
        """
        Processes a list of values using uncertain_work_activity and sends
        the results through a pipe.
        """

        # Create a results array for an uncertain work activity for each value.
        results = [uncertain_work_activity(value) for value in values]

        connection.send(results)
        connection.close()

    def batch_work_divider(self, connection, work: list, beginning: int, end: int):
        """
        Divides a list of work into chunks and processes them using multiprocessing.

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
            # processes.update({i: Process(target=HatbandCommunicator.other_process, args=(op_cons[i], chunk))})
            processes[i] = Process(target=HatbandCommunicator.other_process, args=(op_cons[i], chunk))
            logging.debug(f"Starting process {i} with chunk:\n\n{chunk}")
            processes[i].start()
            

        combined = []
        for i in range(worker_count):
            combined.extend(wd_cons[i].recv())
            processes[i].join()
            logging.debug(f"Process {i} joined.")
        connection.send(combined)
        connection.close()

    def logging_process(log_queue, log_file):
        """Logging process that writes log entries to a JSONL file."""
        while True:
            log_entry = log_queue.get()
            
            if log_entry is None:
                break
        try:
            with open(log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Logging error: {e}")

    def log_message(log_queue, message, level="INFO"):
        """Adds a log entry to the log queue."""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "level": level,
            "message": message,
        }
        log_queue.put(log_entry)

if __name__ == '__main__':
    
    hatband_comm = HatbandCommunicator()
    work = [f"task_{i}" for i in range(1, 101)]

    if hatband_comm.MAX_CPU_CORES >= hatband_comm.MIN_CPU_CORES:

        log_queue = multiprocessing.Queue()
        log_file = "hatband_transactions.jsonl"
        log_process = multiprocessing.Process(target=logging_process, args=(log_queue, log_file))
        log_process.start()

        main_connection, other_connection = Pipe()
        other = Process(target=hatband_comm.batch_work_divider, args=(other_connection, work, 0, len(work)))
        other.start()
        combined = main_connection.recv()
        other.join()
        print(combined)
    else:
        logging.info("Running Hatband sequentially.")
        results = [uncertain_work_activity(task) for task in work]
        print(results)


