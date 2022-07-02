import logging as lg
lg.basicConfig(filename="ltd_task_logs.log", level=lg.INFO)
class List_tup_dictT1:
    '''
    This class is for all the previous tasks which are related to List, Tuples and Dictionary
       all the functions of this class are storing results to the log file..!
    '''

    def reverse_list(self,list1):
        '''
        this fuction reverse the list without using any inbuild function
        '''
        try:
            lg.info(list1[::-1])
        except Exception as e:
            lg.error(e)
    def accessing_element(self,list1):
        '''
        to access 234 and 456 from the list
        :param list1:
        :not returns anything, just stores results to log file:
        '''
        try:
            lg.info(list1[7][1])
            lg.info(list(list1[8].keys())[1])
            lg.info(list1[5][1])
        except Exception as e:
            lg.error(e)

    def extract_list(self,list1):
        '''
        to extract only a list collection form list l

        :param list1:
        :result stored in log file:
        '''
        try:
            lg.info(list1[5:7])
        except Exception as e:
            lg.error(e)
    def extract_keys_values(self,list1):
        '''
        to list all the key and all the values in dict element avaible in list
        :param list1:
        :return:
        '''
        try :
            lg.info(list(list1[8].keys()))
            lg.info(list(list1[8].values()))
        except Exception as e:
            lg.error(e)

l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

ltd = List_tup_dictT1()
ltd.reverse_list(l)
ltd.extract_list(l)
ltd.accessing_element(l)
ltd.extract_list(l)