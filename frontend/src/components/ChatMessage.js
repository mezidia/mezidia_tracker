import React from "react";

const ChatMessage = (props) => {
  const {user_id, content} = props.message;
  const messageClass = user_id === 1643983021344 ? 'left' : 'right';

  return (<>
    <div style={{'text-align': messageClass}}>
      <p>{content}</p>
    </div>
  </>)
}

export default ChatMessage;