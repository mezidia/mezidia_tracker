import React, {useState, useEffect} from "react";

import 'bootstrap/dist/css/bootstrap.min.css';

import UserListView from "./components/UserListView";
import RegisterForm from "./components/Forms/RegisterForm";
import Config from "./config";

function App() {
  const config = new Config();

  const [userList, setUserList] = useState([{}]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${config.BASE_URL}/users`)
      .then(response => {
        if (response.ok) {
          return response.json()
        }
        throw response;
      })
      .then(users => {
        setUserList(users);
      })
      .catch(error => {
        console.error('Error while fetching data: ', error);
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      })
  })

  if (loading) return 'Loading...';
  if (error) return 'Error!';

  return (
    <div>
      <UserListView userList={userList}/>
      <RegisterForm/>
    </div>
  )
}

export default App;
