import React, { findDOMNode } from 'react'
import BaseComponent from '../BaseComponent'

// import validation from 'react-validation-mixin'
// import strategy from 'react-validatorjs-strategy'

import Validator from 'validatorjs'

import request from '../../utils/request'
import ENV from '../../env'

import './style.less'

export default class LinkForm extends BaseComponent {
  constructor(props) {
    super(props)
    this.state = {
      link: '',
      errors: {}
    }
    this.rules = {
      link: 'required|url'
    }
    this._bind('_onSubmit', '_onChange', '_submit', '_validate', '_renderError')
  }

  _submit() {
    const url = ENV.API_URL + ENV.CREATE_LINK_URL
    request(url, {
      method: 'POST',
      body: {
        url: this.state.link
      }
    })
    .then((response) => {
      this.setState({ link: response.short_url, errors: {} })
    })
    .catch(err => err.response.json().then(console.log))
  }

  _validate(success) {
    const validator = new Validator(this.state, this.rules)
    const isValid = validator.passes()
    if (!isValid) {
      this.setState({ errors: { ...validator.errors.errors } })
      return
    } else if (typeof success === 'function') {
      success()
    }
  }

  _onSubmit(e) {
    e.preventDefault()
    this._validate(this._submit)
  }

  _renderError(field) {
    if (field in this.state.errors) {
      const errorsTxt = this.state.errors[field].join(' ')
      return <p>{errorsTxt}</p>
    }
    return null
  }

  _onChange(e) {
    this.setState({
      link: e.target.value
    })
  }

  render() {
    return (
      <form onSubmit={this._onSubmit} className="link-form">
        <div className="input-wrapper">
          <input
            value={this.state.link}
            onChange={this._onChange}
            className="input"
            ref="link"
            placeholder="Ingresa una URL"
            onBlur={this._validate}
          />
          <button>Crear</button>
        </div>
        {this._renderError('link')}
      </form>
    )
  }
}
