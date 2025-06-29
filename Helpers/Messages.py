from enum import Enum

class Error_Messages(Enum):
    INVALID_FORMAT = "The input format is invalid."
    MULTI_DATA = "The provided file contains data for more than one month."
    EMPTY_DATA = "The provided file contains no data."

class Warning_Messages(Enum):
    FILE_EXISTS = "The specified file has been read already. Do you want to replace the data?"
    