import React, { useState, useRef, useEffect } from 'react';
import { MdClose } from 'react-icons/md';
import { FiMenu } from 'react-icons/fi';
import { Link } from 'react-router-dom';
import './Navbar.css'

const Navbar = () => {
  const [navbarOpen, setNavbarOpen] = useState(false);
  const ref = useRef();

  useEffect(() => {
    const handler = (event) => {
      if (navbarOpen && ref.current && !ref.current.contains(event.target)) {
        setNavbarOpen(false);
      }
    };

    document.addEventListener('mousedown', handler);

    return () => {
      // Cleanup the event listener
      document.removeEventListener('mousedown', handler);
    };
  }, [navbarOpen]);

  return (
    <>
      <nav ref={ref} className="navbar">
        <button
          className="toggle"
          onClick={() => setNavbarOpen((prev) => !prev)}
        >
          {navbarOpen ? (
            <MdClose style={{ width: '32px', height: '32px', color: 'red'}} />
          ) : (
            <FiMenu
              style={{
                width: '32px',
                height: '32px',
                color: 'red'
              }}
            />
          )}
        </button>
        <ul className={`menu-nav${navbarOpen ? ' show-menu' : ''}`}>
          <li>
            <Link to="/about" onClick={() => setNavbarOpen(false)} >
           About
            </Link>
          </li>
          <li>
            <Link to="/faq" onClick={() => setNavbarOpen(false)}>
              FAQ
            </Link>
          </li>
          <li>
            <Link to="/login" onClick={() => setNavbarOpen(false)}>
              Login/Signup
            </Link>
          </li>
        </ul>
      </nav>
      <div className="navbar-header-con">
            <h1 className='navbar-header'>ALX Journal</h1>
        </div>
    </>
  );
};

export default Navbar;
