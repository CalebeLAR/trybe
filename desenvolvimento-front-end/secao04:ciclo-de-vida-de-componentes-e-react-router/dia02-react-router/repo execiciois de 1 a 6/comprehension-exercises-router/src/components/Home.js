import React, { Component } from 'react';

class Home extends Component {
  render() {
    return (
      <div>
        <h2>Home</h2>
        <p> My awesome Home component {this.props.nome} </p>
        {this.props.children}
      </div>
    );
  }
}

export default Home;
