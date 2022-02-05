import React, {useEffect, useState} from "react";
import Config from "../config";
import ChatMessage from "./ChatMessage";

const ChatRoom = () => {
  const config = new Config();

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


  const sendMessage = async (e) => {
    e.preventDefault();

    console.log(formValue);
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
