import React from "react";

const User = ({user}) => {
  return (
    <div>
      <p>
        <ul>
          <li>{user.name}</li>
          <li>{user.surname}</li>
          <li>{user.email}</li>
          <li>{user.github_nickname}</li>
          <li>{user.gitlab_nickname}</li>
          <li>{user.bitbucket_nickname}</li>
          <li>{user.password}</li>
        </ul>
      </p>
    </div>
  )
}

export default User;
