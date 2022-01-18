import axios from "axios";
import React from "react";

const TodoItem = (props) => {
  const deleteTodoHandler = (name) => {
    axios.delete(`https://localhost:8080/api/todo/${name}`)
      .then(res => console.log(res.data))
  }
  return (
    <div>
      <p>
        <span style={{fontWeight: 'bold, underline'}}>{props.todo.name} : </span> {props.todo.surname}
        <button onClick={() => deleteTodoHandler(props.todo.name)} className='btn btn-outline-danger my-2 mx-2'
                style={{'borderRadius': '50px'}}>X
        </button>
        <hr/>
        <hr/>
      </p>
    </div>
  )
}

export default TodoItem;
