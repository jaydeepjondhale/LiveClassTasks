import logging
logging.basicConfig(filename="str_task_logs.log", level=logging.INFO)
class String_task :
    '''
    This class is for the previous task which is related to the strings.
    the class is having 3 methods
    and all the methods are storing results to the log file..!
    '''
    def extract(self,str):
        '''to extract data from index one to index 300 with a jump of 3'''
        try:
            logging.info(str[1:300:3])
        except Exception as e:
            logging.error(e)

    def reverse(self,str):
        '''to reverse a string without using reverse function'''
        try:
            logging.info(str[::-1])
        except Exception as e:
            logging.error(e)
    def upper_split(self,str):
        '''to split a string after conversion of entire string in uppercase'''
        try:
            str = str.upper()
            logging.info(str.split())
        except Exception as e:
            logging.error(e)

str_task = String_task()
str1 = "this is My First Python programming class and i am learNING python string and its function"
str_task.extract(str1)
str_task.reverse(str1)
str_task.upper_split(str1)
