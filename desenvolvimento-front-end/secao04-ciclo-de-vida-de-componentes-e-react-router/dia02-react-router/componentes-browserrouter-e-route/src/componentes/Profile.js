import React, { Component } from 'react';
import clonePerfil from './clonePerfil.png';
import { Link } from 'react-router-dom';

export default class Profile extends Component {
    render() {
        return (
            <>
                <h1>Profile</h1>
                <p>profile profile profile</p>
                <div>
                    <img src={clonePerfil} alt="clone"/>
                <Link to="/">
                    <h1>Voltar à HomePage</h1>
                </Link>
                </div>
            </>
        )
    }
}
