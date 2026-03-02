import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    # Safety check: if there is no traceback, provide defaults
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
    # The error message is constructed to include the file name, line number, and the original error message. This provides a comprehensive context for debugging when the exception is raised.
    error_message = f"Error occurred in script: [{file_name}] at line: [{line_number}] message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # 1. super() will call the __init__ method of the parent class (Exception) to ensure that the exception is properly initialized with the error message.
        super().__init__(error_message)
        
        # 2. error_message_detail() is called to create a detailed error message that includes the file name, line number, and the original error message. This detailed message is stored in the instance variable self.error_message for later use when the exception is printed or logged.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
