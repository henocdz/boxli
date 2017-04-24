import React from 'react'
import BaseComponent from '../BaseComponent'

import request from '../../utils/request'
import ENV from '../../env'

import './style.less'

export default class LinkForm extends BaseComponent {
  constructor(props) {
    super(props)
    this.state = {
      link: ''
    }
    this._bind('_onSubmit', '_onChange')
  }

  _onSubmit(e) {
    e.preventDefault()
    const url = ENV.API_URL + ENV.CREATE_LINK_URL
    request(url, {
      method: 'POST',
      body: {
        url: this.state.link
      }
    })
    .then((response) => {
      this.setState({ link: response.short_url })
    })
    .catch(err => err.response.json().then(console.log))
  }

  _onChange(e) {
    this.setState({
      link: e.target.value
    })
  }

  render() {
    return (
      <form onSubmit={this._onSubmit} className="link-form">
        <input value={this.state.link} onChange={this._onChange} className="input" placeholder="Ingresa una URL" />
        <button>Crear</button>
      </form>
    )
  }
}
