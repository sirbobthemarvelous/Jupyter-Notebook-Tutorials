import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn') 

dates = [
    datetime(2020,9,20),
    datetime(2020,9,21),
    datetime(2020,9,22),
    datetime(2020,9,23),
    datetime(2020,9,24),
    datetime(2020,9,25),
    datetime(2020,9,26)
]
y = [0,1,3,4,6,5,7]

plt.plot_date(dates, y, linestyle='solid')
#linestyle solid makes the line visible

plt.gcf().autofmt_xdate()
#get current figure, autoformat

date_format = mpl_dates.DateFormatter('%b, %d %Y')
#use format string to format the dates

plt.gca().xaxis.set_major_formatter(date_format)
#get current axis, now you've formatted the dates as regular

# data['date'] = pd.to_datetime(data['Date'])
# data.sort_values('Date', inplace= True)   these two lines convert strings to a datetime

plt.title('Best Pie Chart')
plt.tight_layout() 
plt.show()