import React, { useState } from 'react';
import './reset.css'
export default function reset() {
    const [email, setEmail] = useState('');
  const [resetMessage, setResetMessage] = useState('');
  const [isResetRequested, setIsResetRequested] = useState(false);

  const handleResetPassword = () => {
    // You can add your password reset logic here, such as sending a request to your backend
    // For this example, we'll simply display a message.
    setResetMessage(
      "Please check your email. If your email is in the database, you will receive an email with a link to reset your password."
    );
    setIsResetRequested(true);
  };
  return (
    <div className='reset'>
      <h2 className='reset_header'>Password Reset</h2>
      <p className='reset_text'>Enter your email to reset your password.</p>

      {isResetRequested ? (
        <div className="reset-message">{resetMessage}</div>
      ) : (
        <div className='reset_input_con'>
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className='reset_input'
          />
          <button onClick={handleResetPassword} className='reset_btn'>Reset Password</button>
        </div>
      )}
    </div>
  )
}
