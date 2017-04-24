import React from 'react'

import "./styles.less"

export default function (props) {
  return (
    <button  {...props} className="wize-button">
      {props.children}
    </button>
  )
}
