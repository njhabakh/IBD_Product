##### import the backend function

def get_financial_report(test=False, ticker=None):
    
    if test:
        #### import sample json file
        import os
        import json
        
        assert(ticker=='AAPL', f'do not support sample {ticker}')
        with open(os.path.join(os.path.dirname(__file__), '..', 'samplejson', 'AAPL.json')) as jsfile:
            res = json.load(jsfile)
        
        ## formatting: drop unfinished sentence
        for k, v in res.items():
            res[k] = '\n'.join(v.split('\n')[:-1]) if '\n' in v and v[-2:]!='\n' else v
        return res

    else:
        #### call the real function here
        # result = MockBackendFunction()
        # res = MockFormatResult()
        # return res

        return {}

if __name__ == '__main__':
    print(get_financial_report(True, 'AAPL'))