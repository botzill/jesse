from jesse.config import config
from jesse.enums import exchanges, timeframes
from jesse.routes import router
from jesse.store import store


def test_routes():
    # re-define routes
    router.set_routes([
        {'exchange': exchanges.BITFINEX, 'symbol': 'ETH-USD', 'timeframe': timeframes.HOUR_3, 'strategy': 'Test19'},
        {'exchange': exchanges.SANDBOX, 'symbol': 'BTC-USD', 'timeframe': timeframes.MINUTE_15, 'strategy': 'Test19'},
    ])

    router.set_extra_candles([
        {'exchange': exchanges.BITFINEX, 'symbol': 'EOS-USD', 'timeframe': timeframes.HOUR_3},
        {'exchange': exchanges.BITFINEX, 'symbol': 'EOS-USD', 'timeframe': timeframes.HOUR_1},
    ])

    # reset store for new routes to take affect
    store.reset(True)

    # now assert it's working as expected
    assert set(config['app']['trading_exchanges']) == {exchanges.SANDBOX, exchanges.BITFINEX}
    assert set(config['app']['trading_symbols']) == {'BTC-USD', 'ETH-USD'}
    assert set(config['app']['trading_timeframes']) == {timeframes.HOUR_3, timeframes.MINUTE_15}
    assert set(config['app']['considering_exchanges']) == {exchanges.SANDBOX, exchanges.BITFINEX}
    assert set(config['app']['considering_symbols']) == {'BTC-USD', 'ETH-USD', 'EOS-USD'}
    assert set(config['app']['considering_timeframes']) == {
        timeframes.MINUTE_1, timeframes.HOUR_3, timeframes.MINUTE_15, timeframes.HOUR_1}
