import uvicorn

import datetime as dt
import enum

from starlette.responses import RedirectResponse
from fastapi_pagination import Page, add_pagination, paginate
from fastapi import FastAPI, Query

from typing import Optional
from pydantic import BaseModel, Field


# TradeDetails Database Model
class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")

# Trade Database Model
class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")

# Sample Data 
sample_trade = [
    {
        "assetClass": "Equity",
        "counterparty": "Huan",
        "instrumentId": "fb8b0116-dead-4f90-99c0-a15ac5430262",
        "instrumentName": "Debentures",
        "tradeDateTime": "2022-07-04 15:36:07.790831",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 5.36,
            "quantity": 45
        },
        "tradeId": "cdf05119-727e-498f-bb6c-3d83043d06e4",
        "trader": "Chase"
    },
    {
        "assetClass": "Bond",
        "counterparty": "Chukwuemeka",
        "instrumentId": "c37d1f1e-aeae-4d0f-bcf4-624b406ad82a",
        "instrumentName": "Preference Shares",
        "tradeDateTime": "2022-07-04 15:36:26.701417",
        "tradeDetails": {
            "buySellIndicator": "SELL",
            "price": 6.69,
            "quantity": 34
        },
        "tradeId": "6af38926-c49e-4b29-8c0e-a76e2f87c1dd",
        "trader": "Lalita"
    },
    {
        "assetClass": "Equity",
        "counterparty": "Sujatha",
        "instrumentId": "4ec3e871-85d3-46b9-ae0b-b599abcd36cd",
        "instrumentName": "Debentures",
        "tradeDateTime": "2022-07-04 15:36:40.179282",
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 25.36,
            "quantity": 21
        },
        "tradeId": "56b2110b-1810-4c58-9c8a-bb551770f08b",
        "trader": "Eugenios"
    },
    {
        "assetClass": "Bond",
        "counterparty": "David",
        "instrumentId": "bade6b0f-af77-4676-a9ef-b9dacefa0610",
        "instrumentName": "Mutual Funds",
        "tradeDateTime": "2022-07-04 15:36:51.077014",
        "tradeDetails": {
            "buySellIndicator": "BUY",
            "price": 15.25,
            "quantity": 12
        },
        "tradeId": "415ceec4-705a-4806-a056-42bcc76b4590",
        "trader": "Lisa"
    }
]

app = FastAPI()

class sort_choice(str, enum.Enum):
    asc = "asc"
    desc = "desc"

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# 1 Get a list of all trade.
@app.get("/all_trades/", status_code=200, response_model=Page[Trade])
def fetchAllTrades(*, trade_datetime_sort: sort_choice = Query(None), buy_sell_indicator_sort: sort_choice = Query(None), asset_class_sort: sort_choice = Query(None), counterparty_sort: sort_choice = Query(None), instrument_id_sort: sort_choice = Query(None), instrument_name_sort: sort_choice = Query(None), trade_id_sort: sort_choice = Query(None), trader_sort: sort_choice = Query(None), price_sort: sort_choice = Query(None), quantity_sort: sort_choice = Query(None)) -> list:
    """
    Get a list of all trade.
    """
    result_response = sample_trade
    if asset_class_sort == "asc":
        result_response = sorted(sample_trade, key=lambda t: t['assetClass']) 
    
    if asset_class_sort == "desc":
        result_response = sorted(sample_trade, key=lambda t: t['assetClass'], reverse=True)
    
    if counterparty_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['counterparty']) 
    
    if counterparty_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['counterparty'], reverse=True)

    if instrument_id_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['instrumentId']) 
    
    if instrument_id_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['instrumentId'], reverse=True)
    
    if instrument_name_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['instrumentName']) 
    
    if instrument_name_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['instrumentName'], reverse=True)

    if trade_datetime_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['tradeDateTime']) 
    
    if trade_datetime_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['tradeDateTime'], reverse=True)

    if buy_sell_indicator_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['buySellIndicator']) 
    
    if buy_sell_indicator_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['buySellIndicator'], reverse=True)
    
    if quantity_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['quantity']) 
    
    if quantity_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['quantity'], reverse=True)
    
    if trader_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['trader']) 
    
    if trader_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['trader'], reverse=True)

    if trade_id_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['tradeId']) 
    
    if trade_id_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['tradeId'], reverse=True)
    
    if price_sort == "asc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['price']) 
    
    if price_sort == "desc":
        result_response = sorted(result_response, key=lambda t: t['tradeDetails']['price'], reverse=True)

    return paginate(result_response)

# 2 Get a trade using its ID.
@app.get("/tradeById/{tradeId}", status_code=200, response_model=Trade)
def fetchTradeBYID(*, tradeId: str) -> dict:
    """
    Get a trade using its ID.
    """

    result_response = [t for t in sample_trade if t["tradeId"] == tradeId]
    if result_response:
        return result_response[0]

# 3 Get a list of transactions by looking for trades by counterparty, instrumentId, instrumentName and trader.
@app.get("/searchTrade", status_code=200, response_model=Page[Trade])
def searchTrade(*, search: str = Query(None)) -> list:
    """
    Get a list of transactions by looking for trades by counterparty, instrumentId, instrumentName and trader.
    """
    result_response = []
    for trade in sample_trade:
        if search.lower() == trade["instrumentId"].lower() or search.lower() == trade["counterparty"].lower() or search.lower() == trade["trader"].lower() or search.lower() == trade["instrumentName"].lower():
            result_response.append(trade)

    return paginate(result_response)

# 4 Get a listing of trades will looking out for trades by assetClass, end, maxPrice, minPrice, start and tradeType.
@app.get("/advanceSearchTrade", status_code=200, response_model=Page[Trade])
def advanceSearchTrade(*, max_price: float = Query(None), min_price: float = Query(None), asset_class: str = Query(None) , trade_type: str = Query(None), end: dt.datetime = Query(None), start: dt.datetime = Query(None)) -> list:
    """
    Get a listing of trades will looking out for trades by assetClass, end, maxPrice, minPrice, start and tradeType.
    """
    results_response = []

    for t in sample_trade:
        flag_asset_class = True
        flag_trade_type = True
        flag_min_price = True
        flag_max_price = True
        flag_start = True
        flag_end = True

        if max_price != None:
            flag_max_price = False
        if start != None:
            flag_start = False
        if end != None:
            flag_end = False
        if asset_class != None:
            flag_asset_class = False
        if trade_type != None:
            flag_trade_type = False
        if min_price != None:
            flag_min_price = False
        

        if asset_class != None:
            if asset_class.lower() in t["assetClass"].lower():
                flag_asset_class = True
        if min_price != None:
            if t["tradeDetails"]["price"] >= min_price:
                flag_min_price = True
        
        if max_price != None:
            if t["tradeDetails"]["price"] <= max_price:
                flag_max_price = True

        if start != None:
            if str(start) >= t["tradeDateTime"]:
                flag_start = True
        if end != None:
            if str(end) <= t["tradeDateTime"]:
                flag_end = True
        if trade_type != None:
            if trade_type.lower() in t["tradeDetails"]["buySellIndicator"].lower():
                flag_trade_type = True

        if flag_asset_class and flag_trade_type and flag_min_price and flag_max_price and flag_start and flag_end:
            results_response.append(t)

    return paginate(results_response)

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)
    