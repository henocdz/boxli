import React from 'react'

import { Redirect } from 'react-router-dom'
import Validator from 'validatorjs'

import BaseContainer from '../BaseContainer'
import request from '../../utils/request'
import Logo from '../../components/Logo'
import Input from '../../components/Input'
import Button from '../../components/Button'
import { saveToken } from '../../utils/auth'

import ENV from '../../env'

import './style.less'

export default class SignUp extends BaseContainer{

  constructor(props) {
    super(props)
    this.state = {
      data: {},
      errors: {},
      redirectElement: null
    }
    this.rules = {
      first_name: 'required',
      password: 'required',
      email: 'required|email'
    }
    this._bind('_onSubmit', '_onChange', '_renderNonFieldErrors', '_validate', '_submit')
  }

  _validate(success) {
    const validator = new Validator(this.state.data, this.rules)
    const isValid = validator.passes()
    if (!isValid) {
      this.setState({ errors: { ...validator.errors.errors } })
      return
    } else if (typeof success === 'function') {
      success()
    }
  }

  _submit() {
    const url = ENV.API_URL + ENV.SIGNUP_URL
    request(url, {
      method: 'POST',
      body: this.state.data
    })
    .then((response) => {
      saveToken(response.token)
      this.setState({ redirectElement: <Redirect to="/" /> })
    })
    .catch((error) => {
      error.response.json().then((errorData) => this.setState({errors: errorData}))
    })
  }

  _onSubmit(e){
    e.preventDefault()
    this._validate(this._submit)
  }

  _onChange(e) {
    this.setState({
      data: {
        ...this.state.data,
        [e.target.name]: e.target.value
      }
    })
  }

  _renderNonFieldErrors() {
    if (this.state.errors.non_field_errors) {
      const errorsTxt = this.state.errors.non_field_errors.join(' ')
      return <p>{errorsTxt}</p>
    }
    return null
  }

  render() {
    return (
      <section>
        {this.state.redirectElement}
        <Logo />
        <form onSubmit={this._onSubmit}>
          <Input
            id="first_name"
            name="first_name"
            label="Nombre"
            errors={this.state.errors.first_name}
            onChange={this._onChange} />
          <Input
            id="email"
            name="email"
            label="Correo electrónico"
            errors={this.state.errors.email}
            onChange={this._onChange} />
          <Input
            id="password"
            name="password"
            label="Contraseña"
            type="password"
            errors={this.state.errors.password}
            onChange={this._onChange} />
          {this._renderNonFieldErrors}
          <Button>Go!</Button>
        </form>
      </section>
    )
  }
}
