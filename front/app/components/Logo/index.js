import React from 'react'

import { Link } from 'react-router-dom'

import './style.less'

const Logo = () => {
  return (
    <Link to="/">
      <h1 className="logo">Boxli!</h1>
    </Link>
  )
}

export default Logo
