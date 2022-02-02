const BASE_URL = 'http://127.0.0.1:8000'

const fetchAllTasks = (url) => {
  return fetch(`${BASE_URL}/${url}`,
    {
      method: "GET",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    })
    .then((response) => response.json())
    .then((responseData) => {
      return responseData;
    })
    .catch(error => console.warn(error));
}

export default fetchAllTasks;
