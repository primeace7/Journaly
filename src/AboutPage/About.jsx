import React from 'react';
import { Link} from 'react-router-dom';
import './About.css'

export default function About() {
  return (
    <div className='About'>
      <section className='about-section'>
        <h1 className='about-header'>Welcome to Journaly</h1>
        <p className='about-text'>
          Journaly is an amazing platform for journaling and organizing your thoughts. It provides a simple and efficient way to keep track of your daily experiences.
        </p>
      </section>

      <Link to="/login">
        <button className='about-btn'>Get Started Now</button>
      </Link>
    </div>
  )
}
