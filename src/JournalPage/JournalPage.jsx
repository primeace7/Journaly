import React, { useState } from 'react';
import './JournalPage.css'

export default function JournalPage() {
    const [inputText, setInputText] = useState('');
  const [chatLog, setChatLog] = useState([]);

  const handleLogMessage = () => {
    if (inputText.trim() !== '') {
      setChatLog([...chatLog, inputText]);
      setInputText('');
    }
  };
  return (
    <div className="journal-page">
      <header className="menu-bar">
        <nav>
          <ul>
            <li><a href="#insights">Insights</a></li>
            <li><a href="#all-journals">All Journals</a></li>
            <li><a href="#settings">Settings</a></li>
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
  )
}
