#Import common modules
import datetime
import os
import sys



# Import logging utils
import mlperf_logging_utils
import mlperf_logging.mllog.constants as mllog_constants
from mlperf_logging_utils import mllogger

if __name__ == "__main__":
    # Setup mllogger
    # mllogger = mllog.get_mllogger()
    mlperf_logging_utils.submission_info(mllogger=mllogger,
                                         submission_benchmark=mllog_constants.STABLE_DIFFUSION,
                                         submission_division=mllog_constants.CLOSED,
                                         submission_org="reference_implementation",
                                         submission_platform="DGX-A100",
                                         submission_poc_name="Ahmad Kiswani",
                                         submission_poc_email="akiswani@nvidia.com",
                                         submission_status=mllog_constants.ONPREM)

    mllogger.start(key=mllog_constants.INIT_START)

    # get the current time to create a new logging directory
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

    status = mllog_constants.ABORTED
    
    sys.path.append(os.getcwd())