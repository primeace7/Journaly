import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './signup.css'

export default function signup() {
  const [formData, setFormData] = useState({
    email: '',
    firstName: '',
    lastName: '',
    username: '',
    password: '',
  });

  const [isUsernameAvailable, setUsernameAvailable] = useState(true);

  useEffect(() => {
    if (formData.username) {
      checkUsernameAvailability(formData.username);
    }
  }, [formData.username]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const navigate = useNavigate();

  const handleSignupSubmit = () => {
    // Send a POST request to your API endpoint with the form data
    axios.post('http://52.3.241.176:5000/api/v1/register', formData)
      .then((response) => {
        // Handle the response as needed
        const userData = response.data;

        // Store the user data in local storage
        localStorage.setItem('userData', JSON.stringify(userData));

        // Navigate to the login page
        navigate('/login');
      })
      .catch((error) => {
        // Handle errors
        console.error(error);
      });
  };

  const checkUsernameAvailability = async (username) => {
    // You can make an API request to check username availability here

    // For this example, we'll simulate it with a timeout
    setTimeout(() => {
      if (username === 'available') {
        setUsernameAvailable(true);
      } else {
        setUsernameAvailable(false);
      }
    }, 1000); // Simulating a delay
  };
  return (
    <div className="signup-container">
    <h2 className='signup-header'>Sign Up</h2>
    <div className='input-con'>
      <label>Email:</label>
      <input
        type="email"
        name="email"
        value={formData.email}
        onChange={handleInputChange}
      />
    </div>
    <div className='input-con'>
      <label>First Name:</label>
      <input
        type="text"
        name="firstName"
        value={formData.firstName}
        onChange={handleInputChange}
      />
    </div>
    <div className='input-con'>
      <label>Last Name:</label>
      <input
        type="text"
        name="lastName"
        value={formData.lastName}
        onChange={handleInputChange}
      />
    </div>
    <div className='input-con'>
      <label>Username:</label>
      <input
        type="text"
        name="username"
        value={formData.username}
        onChange={handleInputChange}
      />
      {formData.username && (
        <p className={`username-availability ${isUsernameAvailable ? 'available' : 'not-available'}`}>
          Username {isUsernameAvailable ? 'is available' : 'is not available'}
        </p>
      )}
    </div>
    <div className='input-con'>
      <label>Password:</label>
      <input
        type="password"
        name="password"
        value={formData.password}
        onChange={handleInputChange}
      />
    </div>

    <button className="submit-button" onClick={handleSignupSubmit}>
     Submit
    </button>
  </div>
  )
}
