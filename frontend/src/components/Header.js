import React from 'react';

const Header = ({ title }) => {
  return (
    <header className='header'>
      <h1>{title}</h1>
      <button className='btn'>Add</button>
    </header>
  )
}

Header.defaultProps = {
  title: 'Mezidia Tracker'
}

export default Header
