# Small Weather Project Using an API
<p>Welcome to my project. This is a weather app where you can find a couple of statistics.</p>
<p>You enter the city of your choice and you'll get the following:</p>
<ul>
<li>Country code</li>
<li>Name of choosen city</li>
<li>Coordinates</li>
<li>Temperature (degrees Celsius)</li>
<li>Feels like temperature (degrees Celsius)</li>
<li>Wind Speed (km/h)</li>
<li>Pressure (hPa)</li>
<li>Humidity (%)</li>
</ul>

## Screenshots
![image](https://github.com/user-attachments/assets/85fdd80e-2eeb-4276-a630-a668c92f9ef5)
![image](https://github.com/user-attachments/assets/0a615dbf-bfdf-48b9-bfc8-3a24b0b602db)

## Installation
1. Clone the Repository and go to directory:
```
git clone https://github.com/Jeffreybekker/WeatherProject.git
cd WeatherProject
```
2. Create a virtual environment:
```
python -m venv env
```
3. Start the virtual environment, depending on your system. You can get more information about this <a href="https://docs.python.org/3/tutorial/venv.html">here</a>.
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Create .env-file in the root of the project with the following:
```
SECRET_KEY='your_secret_key'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```
6. Create SECRET_KEY:
```
python
```
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Copy the secret key and use it in your .env file.<br>

7. Run the server:
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/weather-forecast in your browser.

## URL Endpoint
<p>http://127.0.0.1:8000/weather-forecast</p>
