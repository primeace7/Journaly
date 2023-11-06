import React from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../Navbar/Navbar';
import './Landpage.css'

export default function LandPage() {
    const navigate = useNavigate(); // Use useNavigate hook

  const handleGetStarted = () => {
    navigate('/signup'); // Navigate to the '/signup' page
  };

  const handleLearnMore = () => {
    navigate('/journal'); // Navigate to the '/faq' page
  };
  return (
    <>
    <Navbar/>

        <p className='content-text'>
        A journal is a record of events, ideas, or reflections kept regularly for private use.
        It is a personal document that can be used to track your progress towards goals, document your experiences, or simply reflect on your thoughts and feelings.
      </p>
      <div className="content-btn">
      <button className="get-started-button" onClick={handleGetStarted}>
        Get Started
      </button>
      <button className="learn-more-button" onClick={handleLearnMore}>
        Learn More
      </button>
      </div>
      
        <div className="footer-content">
        <h1 className="Footer-text">Do Hard Things</h1>
        </div>
    </>
  
  )
}
