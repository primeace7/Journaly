import React from 'react';
import { Link } from 'react-router-dom'; 
import './Login.css'

export default function Login() {
  return (
    <div className="login-container">
    <h2>Login</h2>
    <form>
      <div className="login-form-group">
        <label htmlFor="username">Username or Email:</label>
        <input type="text" id="username" name="username" placeholder="Enter your username or email" className='login_input'/>
      </div>
      <div className="login-form-group">
        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" className='login_input'/>
      </div>
      <button type="submit" className='login-btn'>Login</button>
    </form>
    <p className="password-reset-link">
      <Link to="/reset">Forgot your password? Reset it here.</Link>
    </p>
  </div>
  )
}
