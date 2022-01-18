import React, {useState, useEffect} from "react";
import axios from "axios";

import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');

  useEffect(() => {
    axios.get('https://localhost:8080/api/todo')
      .then(res => {
        setTodoList(res.data);
      })
  })

  const addTodoHandler = () => {
    axios.post('https://localhost:8080/api/todo', {'title': title, 'description': desc})
      .then(res => console.log(res));
  };

  return (
    <div
      className='App list-group-item justify-content-center align-items-center mx-auto'
      style={{'width': '400px', 'backgroundColor': 'white', 'marginTop': '15px'}}
    >
      <h1 className='card text-white bg-primary mb-1' styleName={{'maxWidth': '20rem'}}>Task Manager</h1>
      <h6 className='card text-white bg-primary mb-3'>FastAPI - React - Mongo</h6>
      <div className='card-body'>
        <h5 className='card text-white bg-dark mb-3'>Add you task</h5>
        <span>
          <input type="text" className='mb-2 form-control titleIn' placeholder='Title'
                 onChange={event => setTitle(event.target.value)}/>
          <input type="text" className='mb-2 form-control desIn' placeholder='Description'
                 onChange={event => setDesc(event.target.value)}/>
          <button className='btn btn-outline-primary mx-2 mb-3' style={{'borderRadius': '50px', 'fontWeight': 'bold'}}
                  onClick={addTodoHandler}>
            Add task
          </button>
        </span>
        <h5 className='card text-white bg-dark mb-3'>Your tasks</h5>
        <div>

        </div>
      </div>
      <h6 className='card text-dark bg-warning py-1 mb-0'>Copyright 2022, All rights are reserved &copy;</h6>
    </div>
  )
}

export default App;
