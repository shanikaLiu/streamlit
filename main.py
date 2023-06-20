from src.date import QueryTime
from src.results import Results
from src.execute_query import ExecuteQuery
from src.log import logger

import datetime


days = int(datetime.datetime.today().strftime('%j'))

qt = QueryTime()

week_start_time = qt.start_time(n=days)
week_end_time = qt.end_time()
today_line = qt.formatted_today()['today_line']

db = 'eiz_test'
config_path = 'config/db.ini'
query = 'sql/week.sql'
par = {'start_time': week_start_time,
       'end_time': week_end_time}

eq = ExecuteQuery(
                    db = db,
                    config_path=config_path,
                    query=query,
                    par=par
                  )
df = eq.run()

save_to = f'data'
rs = Results(path=save_to)
rs.file_path()


log = logger(path=f'log/{today_line}')


rs.df_with_header(filename=today_line,df=df)

log.info(f'\n>>> {today_line} Exported from {week_start_time} to {week_end_time}\n')
print(f'>>> between "{week_start_time}" and "{week_end_time}" 导出完成.')