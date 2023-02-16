import React, { Component } from 'react'
import { Link } from 'react-router-dom'

export default class About extends Component {
  render() {
    return (
      <div style={{ backgroundColor: '#92F38C'}}>
        <h1>Página About</h1>
        <ul>lista de coisas do about
            <li>about: 1</li>
            <li>about: 2</li>
            <li>about: 3</li>
            <li>about: 4</li>
            <li>about: 5</li>
        </ul>
        <Link to="/">
          <h1>voltar à HomePage</h1>
        </Link>
      </div>
    )
  }
}
