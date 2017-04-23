import React from 'react'

import BaseContainer from '../BaseContainer'
import request from '../../utils/request'
import Logo from '../../components/Logo'

import ENV from '../../env'

import './style.less'

export default class List extends BaseContainer{

  constructor(props) {
    super(props)
    this.state = {links: []}
    this._bind('_fetchLinks', '_renderLink')
  }

  componentDidMount(){
    this._fetchLinks()
  }

  async _fetchLinks(){
    const url = ENV.API_URL + ENV.CREATE_LINK_URL
    const response = await request(url)

    this.setState({links: response})
  }

  _renderLink(link, idx){
    return (
      <li key={idx}>
        <a href={link.short_url} target="_blank">{link.short_url}</a> => <a href={link.url} target="_blank">{link.url}</a>
      </li>
    )
  }

  render() {
    return (
      <section>
        <Logo />
        <ul>
          {this.state.links.map(this._renderLink)}
        </ul>
      </section>
    )
  }
}
