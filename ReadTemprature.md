Project to study the weather conditions of cities around the world
This program first receives the name of the city in question from the user
_______________________________________________________________________

city=input("Enter your city name: ")
_______________________________________________________________________
Then it enters the site wttr.in (Weather Report) through the desired URL
Through the entered city name, the program searches for the name of the user's desired city
Then it finds and receives parameters such as humidity and temperature and the weather conditions of the city
_______________________________________________________________________
temp=date["current_condition"][0]["temp_C"]
weather=date["current_condition"][0]["weatherDesc"][0]["value"]
humidity=date["current_condition"][0]["humidity"]
______________________________________________________________________

Then it prints the status of each parameter in the output
_______________________________________________________________________
print(f"\n city : {city}")
print(f" 🌡️ Temprature : {temp} °C")
print(f" 🌤️ Weater : {weather}")
print(f" 💧 Humidity : {humidity}")
_________________________________________________________________________
To carry out this project, the requests library is required
_________________________________________________________________________
pip install requests
_________________________________________________________________________
