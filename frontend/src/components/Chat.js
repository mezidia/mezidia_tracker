import React, {useEffect, useState} from "react";
import Config from "../config";
import ChatMessage from "./ChatMessage";

const ChatRoom = () => {
  const config = new Config();
  const ws = new WebSocket(`ws://localhost:8000/mezidia-tracker/111`);

  function addZeroToMinutes(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
  }

  function determineTime(time, timezone) {
    return ((+time.substr(0, 2) + timezone) + time.substr(2)).toString();
  }

  const date = new Date();
  const currentTimeZoneOffsetInHours = date.getTimezoneOffset() / 60;
  const utc_time = `${date.getHours() + currentTimeZoneOffsetInHours}:${addZeroToMinutes(date.getMinutes())}`;

  const user_timezone = date.getTimezoneOffset() / 60 * (-1);

  const [messages, setMessages] = useState([{}]);
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);
  const [formValue, setFormValue] = useState('');

  useEffect(() => {
    fetch(`${config.BASE_URL}/chat/mezidia-tracker`)
      .then(response => {
        if (response.ok) {
          return response.json()
        }
        throw response;
      })
      .then(messages => {
          setIsLoaded(true);
          setMessages(messages['messages']);
        },
        (error => {
          setIsLoaded(true);
          console.error('Error while fetching data: ', error);
          setError(error);
        }))
  }, [])

  if (error) return <div>Error: {error.message}</div>;
  if (!isLoaded) return <div>Loading...</div>;

  ws.onmessage = function (e) {
    setMessages(
      [
        ...messages, 
        {
          'user_id': '1643983021344', 
          'content': e.data['content'], 
          'created_at': determineTime(e.data['created_at'], user_timezone),
        }
      ]
    );
  }

  const sendMessage = async (e) => {
    e.preventDefault();
    ws.send({'content': formValue, 'created_at': utc_time})
    setFormValue('');
  }

  return (<>
    <main>
      {messages && messages.map(msg => <ChatMessage key={msg.id} message={msg}/>)}
    </main>

    <form onSubmit={sendMessage}>

      <input
        value={formValue}
        onChange={(e) => setFormValue(e.target.value)}
        placeholder="say something nice"
      />

      <button type="submit" disabled={!formValue}>🕊️</button>

    </form>
  </>)
}

export default ChatRoom
