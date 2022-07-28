## SteelEye API Developer Technical Test

To access all deals, trades by id, and some advanced search filters from the trade database for SteelEye's technical test, I developed this REST API. The pagination and sorting features are also included.

## Installation
```console
$ pip install pipenv
$ pipenv shell --python 3.8
$ pipenv install fastapi
$ pipenv install fastapi-pagination
$ pipenv install uvicorn
```

## Run it
Run the server with:

```console
$ python main.py

INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
In order to demonstrate the rest API. I have developed for this assessment, I am using the FASTAPI Swagger documentation.

![image](https://user-images.githubusercontent.com/88226781/177190789-da426622-8775-46b2-add5-6ac9ad311947.png)

## Get All Trades
To access all the trades kept in the database, I created the endpoint URL `/all_trades/`. The dictionary array in which I had the trade details has been returned.

![image](https://user-images.githubusercontent.com/88226781/177191117-8c21c00d-79b8-4276-8aea-a517d9b0af0e.png)

## Get A Single Trade by Trade Id
To obtain a deal that matches the Trade ID kept in the Trade Database, I have introduced the endpoint URL `/tradeById/{tradeId}`. From there, I ran a for-loop to find the trade that has the same trade id as the trade specified in the query parameter, and I returned that specific trade as a dictionary.

![image](https://user-images.githubusercontent.com/88226781/177191300-36cb7671-78f6-4382-8902-d68d99608e28.png)

## Get All by Searching trades 
To retrieve all deals where the counterparty, instrumentId, instrumentName, and trader registered in the Trade database are equal, I added the endpoint URL `/searchTrade`. As a result, I've performed a for-loop to gather all the deals where at least one of the values in the trade details matches the search criteria specified in the query parameter, and I've returned all of those trades as a list of dictionaries.
![image](https://user-images.githubusercontent.com/88226781/177191499-be4a716a-5003-4342-a463-f62be529c08d.png)
![image](https://user-images.githubusercontent.com/88226781/177191540-10e38f70-9966-43f5-8bfd-ae368c2cf099.png)

## Get All Trades by Advanced Filtering 
To retrieve all deals from the Trade database where the precise value supplied in the query parameter matches, I added the endpoint URL `/advanceSearchTrade`. I've read every deal in the trades dictionary in loop fashion. Every time the loop executes, a condition that only applies if the trade falls inside the parameters specified in the query argument will cause it to be added to the result and return all of the trades in the form of a list of dictionaries.

![image](https://user-images.githubusercontent.com/88226781/177191904-f1e96d4e-d70d-4819-93b7-5c6ecec9596e.png)
![image](https://user-images.githubusercontent.com/88226781/177191932-6a2c6821-4eee-4aae-bcdf-b0bdd2d43a21.png)

## Pagination Feature 
I used the built-in library from the fastapi for this. A function called `/add pagiantion/` has been developed to enable the pagination capability. Following that, whenever I have to return the dictionary list. The function `/paginate/` has been added.

## Sorting Faeture 
I developed a class for enums. to make it simple for the user to choose the order in which they wish to sort the data. I sorted the list of dictionaries using the user-provided argument using the Python `/sorted/` package.

![image](https://user-images.githubusercontent.com/88226781/177192159-6db79793-725e-4a84-b074-69666f8627c5.png)
![image](https://user-images.githubusercontent.com/88226781/177192206-de7ef559-37fb-468f-a7e5-71826dfa21a1.png)

