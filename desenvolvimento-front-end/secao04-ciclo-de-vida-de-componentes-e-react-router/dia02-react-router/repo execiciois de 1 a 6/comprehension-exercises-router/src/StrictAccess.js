import React, { Component } from 'react'

export default class StrictAccess extends Component {
    render() {
        const { user } = this.props;
        return (
            <>
                <h1>StrictAccess</h1>
                <p>Welcome {user.name}</p>
            </>
        )
    }
}
