import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './JournalPage.css';

export default function JournalPage() {
  const [inputText, setInputText] = useState('');
  const [chatLog, setChatLog] = useState([]);

  useEffect(() => {
    // GET request to retrieve all journal entries
    axios.get('http://52.3.241.176:5000/api/v1/username/entries')
      .then((response) => {
        setChatLog(response.data.entries || []);
      })
      .catch((error) => {
        console.error('Error fetching journal entries:', error);
      });
  }, []);

  const handleLogMessage = () => {
    if (inputText.trim() !== '') {
      // POST request to save journal entry
      axios.post('http://52.3.241.176:5000/api/v1/username/entries', { entry: inputText })
        .then(() => {
          setChatLog([...chatLog, inputText]);
          setInputText('');
        })
        .catch((error) => {
          console.error('Error saving journal entry:', error);
        });
    }
  };

  return (
    <div className="journal-page">
      <header className="menu-bar">
        <nav>
          <ul>
            <li>
            <Link to="/insight" >
           Insight
            </Link>
            </li>
            <li><Link to="" >
           All Journals
            </Link></li>
            <li><Link to="" >
           Settings 
            </Link></li>
          </ul>
        </nav>
      </header>

      <div className="chat-container">
        <div className="chat-log">
          {chatLog.map((message, index) => (
            <div className="chat-message" key={index}>
              {message}
            </div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            placeholder="Type your message..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
          <button onClick={handleLogMessage}>Log</button>
        </div>
      </div>
    </div>
  );
}
