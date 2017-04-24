// Needed for redux-saga es6 generator support
import 'babel-polyfill';
import 'sanitize.css/sanitize.css';

// Import root app
import Home from 'containers/Home'
import List from 'containers/List'
import SignUp from 'containers/SignUp'
import Login from 'containers/Login'

import React from 'react'
import { render } from 'react-dom'
import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom'

import './global.less'

export default class Root extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route exact path="/list" component={List} />
          <Route exact path="/signup" component={SignUp} />
          <Route exact path="/login" component={Login} />
        </div>
      </Router>
    )
  }
}

render(<Root />, document.querySelector('#app'));

