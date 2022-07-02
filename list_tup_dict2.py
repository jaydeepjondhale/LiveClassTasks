import logging
logging.basicConfig(filename="ltd_task_logs2.log",level=logging.INFO)

class List_tup_dictT2:
    l1 = []



    '''
    This class is for all the previous tasks which are related to List, Tuples and Dictionary
       all the functions of this class are storing results to the log file..!
    '''
    def extract_list(self,list1):
        '''
        to extract all the list entity.

        :param list1:
        :return:
        '''
        logging.info("Extracting List...")
        try:
            for i in list1:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.error(e)


    def extract_tuple(self,list1):
        '''
                to extract all the tuple entity.

                :param list1:
                :return:
                '''
        logging.info("Extracting Tuple...")
        try:
            for i in list1:
                if type(i) == tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)


    def extract_dict(self,list1):
        '''
                to extract all the dict entity.

                :param list1:
                :return:
                '''
        logging.info("Extracting Dict...")
        try:
            for i in list1:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def extractAllNumeric(self,list1):
        '''
        to extract all the Numeric data it may be a part of dict key and values.

        :param list1:
        :return:
        '''
        logging.info("Extracting All Numeric data")

        try :
            for i in list1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            self.l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                self.l1.append(g)
            logging.info(self.l1)
        except Exception as e:
            logging.error(e)

    def sumOfAllNumeric(self):
        '''
        To sum all the Numeric data it may be a part of dict key and values
        :return:
        '''
        logging.info("Sum of Numeric data")
        try :
            logging.info(sum(self.l1))
        except Exception as e:
            logging.error(e)
    def odd_filter(self):
        '''
        to filter out all the odd values out all numeric datawhich is a part of a list.

        :param list1:
        :return:
        '''
        logging.info("Extracting odd numbers")

        odd=[]
        try:
            for i in self.l1:
                if i % 2 == 0:
                    pass
                else:
                    odd.append(i)
            logging.info(odd)
        except Exception as e:
            logging.error(e)

    def extract_Ineuron(self,list1):
        '''
        to extract "ineuron" out of this dataset.

        :param list1:
        :return:
        '''
        logging.info("Extracting Ineuron")
        l1=[]
        try :
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l1.append(g)
            logging.info(l1)
        except Exception as e:
            logging.error(e)




l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

ltd2 = List_tup_dictT2()
ltd2.extract_list(l)
ltd2.extract_tuple(l)
ltd2.extract_dict(l)
ltd2.extractAllNumeric(l)
ltd2.sumOfAllNumeric()
ltd2.odd_filter()
ltd2.extract_Ineuron(l)


