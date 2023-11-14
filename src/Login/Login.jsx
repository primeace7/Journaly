import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Login.css';

export default function Login() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const [loginError, setLoginError] = useState(null);

  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();
    
    // Send a POST request to your login endpoint with the form data
    axios.post('http://52.3.241.176:5000/api/v1/login', formData)
      .then((response) => {
        // Successful login, handle the response (e.g., store user data or token)
        // Redirect to the user's dashboard or another page
        navigate('/journal');
      })
      .catch((error) => {
        // Handle login error (e.g., display error message)
        setLoginError('Invalid username or password.');
        console.error(error);
      });
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLoginSubmit}>
        <div className="login-form-group">
          <label htmlFor="username">Username or Email:</label>
          <input
            type="text"
            id="username"
            name="username"
            placeholder="Enter your username or email"
            className="login_input"
            value={formData.username}
            onChange={handleInputChange}
          />
        </div>
        <div className="login-form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            className="login_input"
            value={formData.password}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit" className="login-btn">
          Login
        </button>
      </form>
      {loginError && <p className="error-message">{loginError}</p>}
    </div>
  );
}
