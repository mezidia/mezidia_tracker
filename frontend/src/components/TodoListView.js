import TodoItem from "./Todo";

const TodoListView = (props) => {
  console.log(props.todoList);
  return (
    <div>
      <ul>
        {props.todoList.map(todo => <TodoItem todo={todo} />)}
      </ul>
    </div>
  )
}

export default TodoListView;
