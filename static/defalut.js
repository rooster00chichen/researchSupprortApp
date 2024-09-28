async function post_json(url, data) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: data
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(`An error has occurred: ${message}`);
  }

  const response_data = await response.json();
  return response_data
}