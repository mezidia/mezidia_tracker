import React, {useEffect, useState} from "react";
import Config from "../config";
import ChatMessage from "./ChatMessage";

const ChatRoom = () => {
  const config = new Config();
  const ws = new WebSocket(`ws://localhost:8000/mezidia-tracker/111`);

  const addZeroToDate = date => (date < 10 ? '0' + date : date);

  const determineTime = (time, timezone) => {
    if (time) return ((+time.substr(0, 2) + timezone) + time.substr(2)).toString();
  }

  const date = new Date();
  const currentTimeZoneOffsetInHours = date.getTimezoneOffset() / 60;
  const hours = addZeroToDate(date.getHours() + currentTimeZoneOffsetInHours);
  const minutes = addZeroToDate(date.getMinutes());
  const utc_time = `${hours}:${minutes}`;

  const [messages, setMessages] = useState([{}]);
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);
  const [formValue, setFormValue] = useState('');

  const getMessages = async () => {
    const response = await fetch(`${config.BASE_URL}/chat/mezidia-tracker`);
    const data = await response.json();

    if (!response.ok) setError(error);
    else setMessages(data['messages']);
    setIsLoaded(true);
  }

  useEffect(() => {
    getMessages()
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
