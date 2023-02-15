import React, { Component } from 'react';

class Users extends Component {
  render() {
    const { greetingsMessage } = this.props
    return (
      <div>
        <h2>Users</h2>
        <p> { greetingsMessage }, My awesome Users component </p>
        <p> valor recebido pelo parametro dentro da URL:</p>
        <h4>{this.props.match.params.UsersID}</h4>
      </div>
    );
  }
};

export default Users;