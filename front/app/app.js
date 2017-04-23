// Needed for redux-saga es6 generator support
import 'babel-polyfill';
import 'sanitize.css/sanitize.css';

// Import root app
import Home from 'containers/Home'

import React from 'react'
import { render } from 'react-dom'
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'

export default class Root extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Route pattern="/" component={Home} />
        </div>
      </Router>
    )
  }
}

render(<Root />, document.querySelector('#app'));

