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

  const getUsers = async () => {
    const response = await fetch(`${config.BASE_URL}/users`);
    const data = await response.json();

    if (!response.ok) setError(error);
    else setUserList(data);
    setIsLoaded(true);
  }

  useEffect(() => {
    getUsers();
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
