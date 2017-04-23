import React from 'react'

import BaseContainer from '../BaseContainer'
import LinkForm from '../../components/LinkForm'
import Logo from '../../components/Logo'
import { Link } from 'react-router-dom'

import './style.less'

export default class Home extends BaseContainer{
  render() {
    return (
      <section>
        <Logo />
        <LinkForm />
        <div className="link-to-list">
          <Link to="/list">Lista</Link>
        </div>
      </section>
    )
  }
}
