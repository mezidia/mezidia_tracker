import React, {useState, useEffect} from "react";
import axios from "axios";

import 'bootstrap/dist/css/bootstrap.min.css';
import UserListView from "./components/UserListView";
import RegisterForm from "./components/Forms/RegisterForm";
import fetchAllTasks from "./utils";

function App() {
  const [userList, setUserList] = useState([{}]);

  useEffect(() => {
    fetchAllTasks('users').then(resp => setUserList(resp));
    // axios.get('http://127.0.0.1:8000/users')
    //   .then(res => {
    //     setUserList(res.data);
    //   })
  })

  return (
    <div>
      <UserListView userList={userList}/>
      <RegisterForm/>
    </div>
  )
}

export default App;
