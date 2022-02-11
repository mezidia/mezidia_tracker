import User from "./User";

const UserListView = ({userList}) => {
  return (
    <div>
      <ul>
        {userList.map(user => <User user={user} />)}
      </ul>
    </div>
  )
}

export default UserListView;
