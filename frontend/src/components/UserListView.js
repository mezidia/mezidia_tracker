import User from "./User";

const UserListView = (props) => {
  return (
    <div>
      <ul>
        {props.userList.map(user => <User user={user} />)}
      </ul>
    </div>
  )
}

export default UserListView;
