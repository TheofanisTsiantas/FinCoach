from enum import Enum

class Error_Messages(Enum):
    INVALID_FORMAT = "The input format is invalid."
    MULTI_DATA = "The provided file contains data for more than one month."
    EMPTY_IMPORT_DATA = "The provided file contains no data."
    EMPTY_SAVE_DATA = "There is no data to be saved. Action aborted."

class Warning_Messages(Enum):
    FILE_IMPORT_EXISTS = "The specified file has been read already. Do you want to replace the data?"
    FILE_SAVE_EXISTS = "The specified file already contains data. Do you want to replace it?"
    DATA_EXISTS = "All existing data will be overwritten. Do you want to continue?"

class Success_Messages(Enum):
    FILE_READ = "File successfully read."
    DATA_READ = "Data successfully read."
    FILE_SAVE = "File saved successfully."
