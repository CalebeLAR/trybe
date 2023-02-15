import React, { Component } from 'react'

export default class ComponentePai extends Component {
  render() {
    const { prop } = this.props;
    return (
      <div>
        {this.props.children}
        {prop}
      </div>
    )
  }
}
