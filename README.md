# weather-bot
# Weather Bot Documentation

## Overview
The Weather Bot is a Telegram bot that provides users with weather updates and photos of the specified country's current weather conditions. Users input a country name, and the bot retrieves and sends relevant weather data along with an image representing the weather.

## Features
- Accepts a country name as input.
- Fetches real-time weather data.
- Sends an image representing the weather condition.
- Uses APIs to gather accurate weather information and images.

## Technologies Used
- **Python**: Core programming language for bot logic.
- **Telegram Bot API**: For handling user interactions.
- **Weather API**: For retrieving real-time weather data.
- **Image API (e.g., Unsplash, OpenWeatherMap)**: To fetch weather-related images.
- **Requests Library**: For API communication.
- **JSON**: For handling data.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-bot
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up API keys for:
   - Telegram Bot API
   - Weather API (e.g., OpenWeatherMap)
   - Image API (if applicable)

## Usage
1. Start the bot by running:
   ```bash
   python bot.py
   ```
2. Send a message in Telegram with a country name.
3. The bot will fetch and return the current weather conditions along with an image.

## Example Interaction
**User:** `Germany`

**Bot Response:**
- Weather: `Cloudy, 10°C`
- Image: *(A picture of cloudy weather in Germany)*

## Code Structure
```
weather-bot/
│-- bot.py               # Main bot logic
│-- config.py            # Configuration and API keys
│-- requirements.txt     # Dependencies
│-- utils.py             # Helper functions (API requests, image fetching)
```

## API Integration
### Weather API Request
Example request to fetch weather data:
```python
import requests

API_KEY = "your_weather_api_key"
COUNTRY = "Germany"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={COUNTRY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
print(data)
```

### Image API Request
Example request to fetch a weather image:
```python
import requests

IMAGE_API_KEY = "your_image_api_key"
WEATHER_TYPE = "cloudy"
URL = f"https://api.unsplash.com/photos/random?query={WEATHER_TYPE}&client_id={IMAGE_API_KEY}"

response = requests.get(URL)
data = response.json()
print(data["urls"]["regular"])
```

## Future Enhancements
- Add support for multiple languages.
- Implement more detailed weather insights (humidity, wind speed, etc.).
- Allow users to subscribe to daily weather updates.

## License
This project is licensed under the MIT License.
