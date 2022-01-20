import React, {useState, useEffect} from "react";
import axios from "axios";

import 'bootstrap/dist/css/bootstrap.min.css';
import UserListView from "./components/UserListView";

function App() {
  const [userList, setUserList] = useState([{}]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/users')
      .then(res => {
        setUserList(res.data);
      })
  })

  return (
    <div>
      <UserListView userList={userList}/>
    </div>
  )
}

export default App;
