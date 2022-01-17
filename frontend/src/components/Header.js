import React from 'react';
import Button from "./Button";

const Header = ({title}) => {
  const onClick = (e) => {
    console.log('clicked')
  }
  return (
    <header className='header'>
      <h1>{title}</h1>
      <Button color='green' text='Add' onClick={onClick} />
    </header>
  )
}

Header.defaultProps = {
  title: 'Mezidia Tracker'
}

export default Header
