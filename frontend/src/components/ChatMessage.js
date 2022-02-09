import React from "react";

const ChatMessage = (props) => {
  const date = new Date();
  const user_timezone = date.getTimezoneOffset() / 60 * (-1);
  const {user_id, content, created_at} = props.message;
  const messageClass = user_id === 1643983021344 ? 'left' : 'right';
  const time = props.dateFunc(created_at, user_timezone);
  return (<>
      <div style={{'text-align': messageClass}}>
        <p>{content}<sub>{time}</sub></p>
      </div>
    </>
  )
}

export default ChatMessage;