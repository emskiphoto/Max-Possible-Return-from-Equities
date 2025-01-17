parameters = dict(equity_starting = 100000,
                size_position_pct = 0.05,
                 position_max_pct_of_volume = 0.05)
parameters['size_position'] = parameters['equity_starting'] * parameters['size_position_pct']
parameters['min_ticker_dollar_volume'] = parameters['size_position'] / parameters['position_max_pct_of_volume']