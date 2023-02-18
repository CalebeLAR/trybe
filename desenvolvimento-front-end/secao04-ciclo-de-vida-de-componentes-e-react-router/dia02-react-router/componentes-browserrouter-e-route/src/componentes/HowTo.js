import React, { Component } from 'react'
import { Link } from 'react-router-dom'

export default class HowTo extends Component {
  render() {
    return (
      <>
        <h1>HowTo</h1>
        <p>pagina do HowTo</p>
        <span>how to how to hwoto</span>
        <Link to="/">
          <h1>Voltar à HomePage</h1>
        </Link>
      </>
    )
  }
}
