import React, {useEffect, useState} from "react";
import Config from "../config";
import ChatMessage from "./ChatMessage";

const ChatRoom = () => {
  const config = new Config();
  const ws = new WebSocket(`ws://localhost:8000/mezidia-tracker/111`);

  const addZeroToMinutes = minutes => {
    if (minutes < 10) {
      minutes = '0' + minutes;
    }
    return minutes;
  }

  const determineTime = (time, timezone) => {
    if (time) return ((+time.substr(0, 2) + timezone) + time.substr(2)).toString();
  }

  const date = new Date();
  const currentTimeZoneOffsetInHours = date.getTimezoneOffset() / 60;
  const utc_time = `${date.getHours() + currentTimeZoneOffsetInHours}:${addZeroToMinutes(date.getMinutes())}`;

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
    const data = e.data.split(',')
    setMessages(
      [
        ...messages,
        {
          'user_id': '1643983021344',
          'content': data[0],
          'created_at': data[1],
        }
      ]
    );
  }

  const sendMessage = async (e) => {
    e.preventDefault();
    ws.send(`${formValue},${utc_time}`)
    setFormValue('');
  }

  return (<>
    <main>
      {messages && messages.map(msg => <ChatMessage key={msg.id} message={msg} dateFunc={determineTime}/>)}
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
