from django.shortcuts import render
import requests
import yfinance as yf
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.models import HoverTool
def candlestick(request):
    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2021,4,2)
    df= data.DataReader(name='VZ', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value

    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    p=figure(x_axis_type='datetime', width=1000, height=500)
    p.title='Verizon Candlestick Chart'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    p.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    p.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    p.segment(df.index, df.High, df.index, df.Low, color='black')

    script, div = components(p)

    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2021,4,2)
    df= data.DataReader(name='T', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value

    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    plot=figure(x_axis_type='datetime', width=1000, height=500)
    plot.title='AT&T Candlestick Chart'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    plot.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    plot.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    plot.segment(df.index, df.High, df.index, df.Low, color='black')
    scripts, divs = components(plot)
    start = datetime.datetime(2021,1,1)
    end = datetime.datetime(2021,4,2)
    df= data.DataReader(name='TMUS', data_source = 'yahoo', start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value= 'increase'
        elif c < o:
            value='decrease'
        else:
            value="Equal"
        return value

    df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    df['Middle']=(df.Open+df.Close)/2
    df['Height']=abs(df.Open - df.Close)
    plots=figure(x_axis_type='datetime', width=1000, height=500)
    plots.title='T-mobile Candlestick Chart'
    # p.grid.grid_line_alpha=0.3
    hours= 12*60*60*1000
    plots.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
            hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')

    plots.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
            hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    plots.segment(df.index, df.High, df.index, df.Low, color='black')
    script1, div1 = components(plots)
    return render(request, 'graph_page.html', {'script':script, 'div':div, 'scripts': scripts, 'divs': divs,'script1':script1, 'div1':div1})


# def graph_page(request):
    # df = pd.read_csv('matplot\export_TMUS.csv')
    # df=df[['Close']]
    # future_days=5
    # df['Predicted Prices'] = df[['Close']].shift(-future_days)
    # x = np.array(df.drop(['Predicted Prices'], 1))[:-future_days]
    # y = np.array(df['Predicted Prices'])[:-future_days]
    # #splitting data into 75% training-set & 25% test-set
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # #creating decision tree model
    # tree = DecisionTreeRegressor().fit(x_train, y_train)
    # lr = LinearRegression().fit(x_train, y_train)
    # x_future = df.drop(['Predicted Prices'], 1)[:-future_days]
    # x_future = x_future.tail(future_days)
    # x_future = np.array(x_future)
    # tree_pred = tree.predict(x_future)
    # lr_pred = lr.predict(x_future)
    # preds = tree_pred
    # valid = df[x.shape[0]:]
    # valid['Predicted Prices']= preds
    # #tree predicted price= $126.30 -- lr pp= 124.67
    # plt.figure(figsize=(16,10))
    # plt.title('T-mobile: Decision Tree Model')
    # plt.xlabel('Days')
    # plt.ylabel('Close Price')
    # plt.plot(df['Close'])
    # plt.plot(valid[['Close', 'Predicted Prices']])
    # plt.show()
    # start = datetime.datetime(2021,1,1)
    # end = datetime.datetime(2021,4,2)
    # df= data.DataReader(name='VZ', data_source = 'yahoo', start=start, end=end)
    # def inc_dec(c, o):
    #     if c > o:
    #         value= 'increase'
    #     elif c < o:
    #         value='decrease'
    #     else:
    #         value="Equal"
    #     return value
    #
    # df['Status']=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
    # df['Middle']=(df.Open+df.Close)/2
    # df['Height']=abs(df.Open - df.Close)
    #
    #
    # p=figure(x_axis_type='datetime', width=1000, height=500)
    # p.title='verizon candlestick chart'
    # # p.grid.grid_line_alpha=0.3
    # hours= 12*60*60*1000
    # p.rect(df.index[df.Status=='increase'], df.Middle[df.Status=='increase'],
    #         hours, df.Height[df.Status=='increase'], fill_color='green', line_color='black')
    #
    # p.rect(df.index[df.Status=='decrease'], df.Middle[df.Status=='decrease'],
    #         hours, df.Height[df.Status=='decrease'], fill_color='red', line_color='black')
    # p.segment(df.index, df.High, df.index, df.Low, color='black')
    # output_file('candlestick.html')
    # show(p)
    #
    # # fig = p.gcf()
    # # buf = io.BytesIO()
    # # fig.savefig(buf, format='png')
    # # buf.seek(0)
    # # string = base64.b64encode(buf.read())
    # # uri = urllib.parse.quote(string)
    # return render(request, 'graph_page.html')
