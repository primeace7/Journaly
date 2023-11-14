import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import LandPage from './LandPage/LandPage';
import About from './AboutPage/About'
import Login from './Login/Login'; 
import FAQ from './FaqPage/faq';
import SIGNUP from './Signup/signup';
import JOURNAL from './JournalPage/JournalPage';
import INSIGHT from './InsightPage/Insight'

export default function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<LandPage />} />
      <Route path="/about" element={<About />} />
      <Route path="/login" element={<Login />} />
      <Route path="/faq" element={<FAQ />} />
      <Route path="/signup" element={<SIGNUP />} />
      <Route path="/journal" element={<JOURNAL />} />
      <Route path="/insight" element={<INSIGHT />} />
      {/* Define other routes here */}
    </Routes>
  </BrowserRouter>
  )
}
