async function getWeather() {
    const city = document.getElementById('city').value;
    const resultElement = document.getElementById('result');

    if (!city) {
        resultElement.innerText = 'Please enter a city name.';
        return;
    }

    try {
        const response = await fetch(`/weather?city=${city}`);
        const data = await response.json();

        if (response.ok) {
            resultElement.innerText = `City: ${data.city}\nTemperature: ${data.temperature}°C\nDescription: ${data.description}`;
        } else {
            resultElement.innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        resultElement.innerText = 'Error fetching weather data.';
    }
}