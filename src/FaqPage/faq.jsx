import React, { useState } from 'react';
import './faq.css'

export default function faq() {
    const faqData = [
        {
          question: 'What is ALX Journal?',
          answer: 'ALX Journal is a web application designed for creating and managing journal entries. It allows users to write, save, and organize their thoughts and ideas.'
        },
        {
          question: 'How do I create a journal entry?',
          answer: 'To create a new journal entry, click on the "New Entry" button in the app. You can then enter your title and content for the journal entry.'
        },
        {
          question: 'Can I edit my journal entries?',
          answer: 'Yes, you can edit your journal entries at any time. Just select the entry you want to edit, and click on the "Edit" button.'
        },
        {
          question: 'Is my data secure?',
          answer: 'Yes, we take data security seriously. Your journal entries are stored securely and are accessible only by you.'
        }
      ];
    
      const [activeIndex, setActiveIndex] = useState(null);
    
      const handleDropdownClick = (index) => {
        setActiveIndex(activeIndex === index ? null : index);
      };
  return (
    <div className="faq-container">
      <h2>Frequently Asked Questions</h2>
      <ul className="faq-list">
        {faqData.map((faq, index) => (
          <li key={index} className={`faq-item ${activeIndex === index ? 'active' : ''}`}>
            <div className="faq-question" onClick={() => handleDropdownClick(index)}>
              <span>{faq.question}</span>
              <div className="dropdown-icon">{activeIndex === index ? '-' : '+'}</div>
            </div>
            <div className="faq-answer">{faq.answer}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
