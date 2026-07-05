try:
    import requests 
    city=input("Enter your city name: ")
    url=f"https://wttr.in/{city}?format=j1"
    date=requests.get(url).json()
    temp=date["current_condition"][0]["temp_C"]
    weather=date["current_condition"][0]["weatherDesc"][0]["value"]
    humidity=date["current_condition"][0]["humidity"]
    print(f"\n city : {city}")
    print(f"  Temprature : {temp} °C")
    print(f"  Weater : {weather}")
    print(f"  Humidity : {humidity}")
except:
    print("Please Enter incorrect name")
