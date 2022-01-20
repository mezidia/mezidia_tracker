import React from "react";

const User = (props) => {
  return (
    <div>
      <p>
        <ul>
          <li>{props.user.name}</li>
          <li>{props.user.surname}</li>
          <li>{props.user.email}</li>
          <li>{props.user.github_nickname}</li>
          <li>{props.user.gitlab_nickname}</li>
          <li>{props.user.bitbucket_nickname}</li>
          <li>{props.user.password}</li>
        </ul>
      </p>
    </div>
  )
}

export default User;
