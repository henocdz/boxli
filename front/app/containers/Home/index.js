import React from 'react'

import BaseContainer from '../BaseContainer'
import LinkForm from '../../components/LinkForm'
import Logo from '../../components/Logo'
import { Link } from 'react-router-dom'
import { isAuthenticated, logout } from '../../utils/auth'

import './style.less'

export default class Home extends BaseContainer{
  constructor(props) {
    super(props);
    this.state = {
      isAuthenticated: isAuthenticated()
    }
    this._bind('_logout')
  }

  _logout() {
    logout()
    this.setState({isAuthenticated: isAuthenticated()})
  }

  render() {
    return (
      <section>
        <Logo />
        <LinkForm />
        <div className="link-to-list">
          <p>&nbsp;</p>
          <Link to="/list">Lista</Link> &nbsp;
          { isAuthenticated() ? null : <Link to="/signup">Registro</Link>} &nbsp;
          { isAuthenticated() ? null : <Link to="/login">Acceso</Link> }
          { isAuthenticated() ? <Link to="#" onClick={this._logout}>Salir</Link> : null }
        </div>
      </section>
    )
  }
}
