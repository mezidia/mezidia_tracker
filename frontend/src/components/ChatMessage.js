import React from "react";

const ChatMessage = ({message, id}) => {
  const date = new Date();
  const user_timezone = date.getTimezoneOffset() / 60 * (-1);

  const determineTime = (time, timezone) => {
    if (time) return ((+time.substr(0, 2) + timezone) + time.substr(2)).toString();
  }

  const {user_id, content, created_at} = message;
  const messageClass = user_id === 1643983021344 ? 'left' : 'right';
  const time = determineTime(created_at, user_timezone);
  return (<>
      <div style={{'text-align': messageClass}}>
        <p>{content}<sub>{time}</sub></p>
      </div>
    </>
  )
}

export default ChatMessage;