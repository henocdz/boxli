import React from 'react'

import BaseContainer from '../BaseContainer'
import LinkForm from '../../components/LinkForm'

import './style.less'

export default class Home extends BaseContainer{
  render() {
    return (
      <section>
        <h1 className="logo">Boxli!</h1>
        <LinkForm />
      </section>
    )
  }
}
