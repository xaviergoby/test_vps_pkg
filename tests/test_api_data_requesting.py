import requests




# https://digiconomist.net/wp-json/mo/v1/bitcoin/stats/20220718:

url = "https://digiconomist.net/wp-json/mo/v1/bitcoin/stats/20220718:"

querystring = {"url":"https://example.com"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "scrapers-proxy2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)