async function fetchData() {
    // Clear previous data
    document.getElementById('output').textContent = '';
    document.getElementById('avatar').src = '';

    let username = document.getElementById('username').value;
    username = username.trim(); // Remove leading and trailing spaces
    const response = await fetch(`https://api.chess.com/pub/player/${username}`);
    const data = await response.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
    document.getElementById('avatar').src = data.avatar;
}

// Fetch data for the default username on page load
window.onload = fetchData;