import requests
params={
  "amount":10,
  "difficulty":"medium",
  "type":"boolean",

}
response=requests.get(url="https://opentdb.com/api.php",params=params)
response=response.json()
question_data=response["results"]

