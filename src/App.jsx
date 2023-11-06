import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LandPage from './LandPage/LandPage';
import About from './AboutPage/About'
import Login from './Login/Login'; 
import FAQ from './FaqPage/faq';
import RESET from './resetpasswordPage/reset';
import SIGNUP from './Signup/signup';
import JOURNAL from './JournalPage/JournalPage'

export default function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<LandPage />} />
      <Route path="/about" element={<About />} />
      <Route path="/login" element={<Login />} />
      <Route path="/faq" element={<FAQ />} />
      <Route path="/reset" element={<RESET />} />
      <Route path="/signup" element={<SIGNUP />} />
      <Route path="/journal" element={<JOURNAL />} />
      {/* Define other routes here */}
    </Routes>
  </BrowserRouter>
  )
}
