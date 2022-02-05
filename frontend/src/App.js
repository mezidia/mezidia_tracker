import React, {useState, useEffect} from "react";

import 'bootstrap/dist/css/bootstrap.min.css';

import UserListView from "./components/UserListView";
import RegisterForm from "./components/Forms/RegisterForm";
import Config from "./config";
import ChatRoom from "./components/Chat";

function App() {
  const config = new Config();

  const [userList, setUserList] = useState([{}]);
  const [isLoaded, setIsLoaded] = useState(false);
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
          setIsLoaded(true);
          setUserList(users);
        },
        (error => {
          setIsLoaded(true);
          console.error('Error while fetching data: ', error);
          setError(error);
        }))
  }, [])

  if (error) return <div>Error: {error.message}</div>;
  if (!isLoaded) return <div>Loading...</div>;

  return (
    <div>
      <UserListView userList={userList}/>
      <RegisterForm/>
      <hr/>
      <ChatRoom />
    </div>
  )
}

export default App;
