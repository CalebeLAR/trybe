import React from 'react'
import { Link } from 'react-router-dom'

export default class Home extends React.Component {
    render() {
        return (
            <>
                <h1>Minha Home Page</h1>
                <Link to="/about">
                    <h1>About</h1>
                </Link>
                <Link to="/profile">
                    <h1>profile</h1>
                </Link>
                <Link to="/howto">
                    <h1>howto</h1>
                </Link>
            </>
        )
    }
}
