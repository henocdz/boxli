import React from 'react'

import "./styles.less"

const _renderErrors = (errors) => {
  if (errors) {
    const errorsTxt = errors.join(' ')
    return <p>{errorsTxt}</p>
  }
}

export default function (props) {
  const { label, errors, ...inputProps } = props
  return (
    <div className="input-wrapper">
      <label htmlFor="{props.id}">{label}</label>
      <input {...inputProps} />
      {_renderErrors(errors)}
    </div>
  )
}
