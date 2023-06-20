import os

class Results():

    def __init__(self,path):
        
        self.path = path


    def file_path(self):

        if os.path.exists(self.path):

            print(f'>>> csv path {self.path} existed.')

        else:

            print(f'>>> csv path {self.path} created.')

            os.makedirs(self.path)


    def df_without_header(self,filename,df):

        path = f'{self.path}/{filename}.csv'

        df.to_csv(path,mode='w',header=False,index=False)


    def df_with_header(self,filename,df):

        path = f'{self.path}/{filename}.csv'

        df.to_csv(path,mode='w',header=True,index=False)
