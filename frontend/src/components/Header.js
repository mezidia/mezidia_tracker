import React from 'react';

const Header = ({ title }) => {
  return (
    <header>
      <h1 style={{color: 'red', backgroundColor: 'blue'}}>{title}</h1>
    </header>
  )
}

Header.defaultProps = {
  title: 'Mezidia Tracker'
}

export default Header
